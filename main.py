import sys
import constants as const
from database import movies
from scraper import fetch_box_office_list, fetch_movie_details

def mainLoop(endMovieYear):
  nextMovieDetails = movies.get_next_movie_year_and_box_office_rank()
  print(f'Next movie to be scraped: {nextMovieDetails}\n')
  nextMovieYear = nextMovieDetails['year']
  nextMovieRank = nextMovieDetails['box_office_rank']

  yearsPastInitialYear = 0
  while (nextMovieYear + yearsPastInitialYear) < endMovieYear:

    startingMovieRank = nextMovieRank if yearsPastInitialYear == 0 else 1

    movie_list = fetch_box_office_list((nextMovieYear + yearsPastInitialYear), startingMovieRank, 200)

    for movie in movie_list:
      movie_details = fetch_movie_details(movie['name'], (nextMovieYear + yearsPastInitialYear))

      if not movie_details:
        continue

      movieToInsert = {
        **movie_details,
        'box_office_rank': movie['rank'],
      }
      movies.insert_movie(movieToInsert)
    
    yearsPastInitialYear = yearsPastInitialYear + 1
  

def main():
  if len(sys.argv) < 2:
    print(f"Usage: python {sys.argv[0]} {const.ARG_DELETE_COPIES} {const.ARG_SCRAPE}:<endMovieYear>")
    return

  scriptInstructions = {
    const.ARG_DELETE_COPIES: False,
    const.ARG_SCRAPE: False
  }
  endMovieYear = None  # Default value

  for i in range(1, len(sys.argv)):
    arg = sys.argv[i]
    if arg == const.ARG_DELETE_COPIES:
      scriptInstructions[const.ARG_DELETE_COPIES] = True
    elif const.ARG_SCRAPE in arg:
      parts = arg.split(':')
      if len(parts) != 2:
        print(f"Invalid argument format for {const.ARG_SCRAPE}. Please provide in format {const.ARG_SCRAPE}:<endMovieYear>")
        return
      try:
        endMovieYear = int(parts[1])
      except ValueError:
        print("Invalid endMovieYear. Please provide a valid year as an integer.")
        return
      scriptInstructions[const.ARG_SCRAPE] = True
    else:
      print(f"Invalid argument: {arg}")
      return

  if scriptInstructions[const.ARG_DELETE_COPIES]:
    movies.delete_movies_with_duplicate_titles()

  if scriptInstructions[const.ARG_SCRAPE] and endMovieYear is not None:
    mainLoop(endMovieYear)


if __name__ == "__main__":
    main()
