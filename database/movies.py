from . import db

movies_collection = db.movies

def get_next_movie_year_and_box_office_rank():
  print("Getting next movie", "\n=============================")
  moviesCollection = db['movies']
  latestYearMovie = moviesCollection.find_one(sort=[("year", -1)])
  if not latestYearMovie:
    # No movies in the database
    return 'EMPTY_DB'
  
  latestYear = latestYearMovie['year']

  lowestRankedMovie = moviesCollection.find_one({"year": latestYear}, sort=[("box_office_rank", -1)])
  if not lowestRankedMovie:
    # No movies in the database
    return 'EMPTY_DB'
  
  rank = lowestRankedMovie['box_office_rank']
  latestYearInt = int(latestYear)

  response = {
    "year": latestYearInt if rank < 200 else latestYearInt + 1,
    "box_office_rank": rank + 1 if rank < 200 else 1
  }

  return response

def insert_movie(movie_data):
  # Implementation here to insert a new movie document
  print(f"Inserting {movie_data['title']} ({movie_data['year']}) - rank: {movie_data['box_office_rank']}", "\n=============================")
  result = movies_collection.insert_one(movie_data)
  if result.acknowledged:
      print(f"Movie inserted with ID: {result.inserted_id}\n")
  else:
      print("Error inserting movie")


def update_movie(movie_id, updated_movie_data):
  # Implementation here to update a movie document
  print("Updating movie", "\n=============================")

def delete_movies_with_duplicate_titles():
  moviesCollection = db['movies']
  documents = list(moviesCollection.find().sort("title"))

  i = 0
  while i < len(documents) - 1:
    # If the current document's title matches the next document's title
    if documents[i]['title'] == documents[i+1]['title']:
        # Compare box_office_rank
        if documents[i]['box_office_rank'] < documents[i+1]['box_office_rank']:
            moviesCollection.delete_one({'_id': documents[i]['_id']})
        else:
            moviesCollection.delete_one({'_id': documents[i+1]['_id']})
        # Refresh the list after a deletion
        documents = list(moviesCollection.find().sort("title"))
    else:
        i += 1