from database import movies

def main():
  # Example: Insert a new movie
  # movie_data = {
  #   "rating": "PG",
  #   "url": "https://www.rottentomatoes.com/m/some_movie",
  #   # ... other fields
  # }
  # movies.insert_movie(movie_data)
  
  # Example: Get the latest movie
  latest_movie = movies.get_latest_movie()
  print(latest_movie)

if __name__ == "__main__":
    main()
