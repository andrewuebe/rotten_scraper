from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

def search_aggregate_for_movie(movie_name, movie_year):
  print(f"Searching for {movie_name} on site...")

  encoded_movie_name = quote(movie_name.encode('utf-8'))
  URL = f'https://www.rottentomatoes.com/search?search={encoded_movie_name}'
  response = requests.get(URL)
  soup = BeautifulSoup(response.content, 'html.parser')

  foundMovieList = soup.find_all('search-page-media-row')
  for movie in foundMovieList:
    movieName = movie.find('a', {'data-qa': 'info-name'}).text.strip()

    # Check for the existence of the releaseyear attribute
    movieYearFromRow = movie.get('releaseyear')
    if not movieYearFromRow:
      continue

    movieYear = int(movieYearFromRow)

    if movieName == movie_name and movieYear == movie_year:
      linkElement = movie.find('a', {'data-qa': 'info-name'})
      return linkElement['href']

def fetch_movie_details(movie_name, movie_year):
  # Logic to fetch movie details for a specific movie
  pageUrl = search_aggregate_for_movie(movie_name, movie_year)
  if not pageUrl:
    print('Movie not found on site')
    return None
  
  pageResponse = requests.get(pageUrl)
  pageSoup = BeautifulSoup(pageResponse.content, 'html.parser')

  scoreboard = pageSoup.find('score-board')
  if not scoreboard:
    print('"score-board" not found, trying "score-board-deprecated"...')
    scoreboard = pageSoup.find('score-board-deprecated')
    if not scoreboard:
      print('"score-board-deprecated" not found')
      return None
    
  rating = scoreboard['rating']
  if not rating:
    print('"rating" not found')
    return None
  
  rtScore = scoreboard['tomatometerscore']
  if not rtScore:
    print('"tomatometerscore" not found')
    return None
  
  audienceScore = scoreboard['audiencescore']
  if not audienceScore:
    print('"audiencescore" not found')
    return None
  
  genreSpanContent = pageSoup.find('span', {'class': 'genre', 'data-qa': 'movie-info-item-value'})
  if not genreSpanContent:
    print("Genre not found")
    return None
  
  strippedGenreSpanContent = genreSpanContent.text.strip()

  if "," not in strippedGenreSpanContent:
    genres = [strippedGenreSpanContent]
  else:
    genres = [genre.strip() for genre in strippedGenreSpanContent.split(",")]

  directorElement = pageSoup.find('a', {'data-qa': 'movie-info-director'})
  if not directorElement:
    print("Director not found")
    return None
  
  director = directorElement.text.strip()

  castNamesElements = pageSoup.find_all('a', {'data-qa': 'cast-crew-item-link'})[:3]
  if not castNamesElements:
    print("Cast names not found")
    return None
  
  castNames = [castNameElement.find('p').text.strip() for castNameElement in castNamesElements]

  return {
    'title': movie_name,
    'year': str(movie_year),
    'url': pageUrl,
    'rt_score': rtScore,
    'audience_score': audienceScore,
    'rating': rating,
    'genre': genres,
    'director': director,
    'cast_names': castNames,
  }
