from bs4 import BeautifulSoup
import requests


def fetch_box_office_list(year, start_rank, end_rank):
  print(f"Fetching box office list for {year}", "\n=============================")

  URL = f'https://www.boxofficemojo.com/year/{year}/?grossesOption=totalGrosses'
  response = requests.get(URL)
  soup = BeautifulSoup(response.content, 'html.parser')

  # Extract the table
  table = soup.find('table', {'class': 'a-bordered'})

  # Extract rows
  movieNameTds = table.findAll('td', {'class': 'mojo-field-type-release'})

  # Iterate over rows and extract required data
  movies = []
  for index, movieNameTd in enumerate(movieNameTds[start_rank - 1:]):  # Start from 1 to skip the header row
    rank = start_rank + index
    if rank > end_rank:
      break

    name_cell = movieNameTd.find('a', {'class': 'a-link-normal'})

    if name_cell:  # Making sure the cell exists
      name = name_cell.a.text.strip() if name_cell.a else name_cell.text.strip()
      movies.append({'name': name, 'rank': rank})
  
  return movies

