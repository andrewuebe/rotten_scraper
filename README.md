# Rotten Scraper

`rotten_scraper` is a Python-based web scraping tool designed to extract movie data from box office rankings and a popular movie review aggregate website. The extracted data is stored in a MongoDB database for further analysis and insights.

## Project Overview

### 1. MongoDB Interaction:
- Connect to a local MongoDB database called 'rotten_data'.
- Interact with the `rotten_data.movies` collection.
- Retrieve the movie with the most recent year.
- Find the movie in the most recent year with the highest box office rank.

### 2. Box Office Website Scraping:
- Navigate to the website with box office rankings for the most recent year in the database.
- Scrape movie names and their ranks.
- Continue scraping subsequent years if needed.

### 3. Popular Movie Review Aggregate Website Scraping:
- Search for the movie on the popular movie review aggregate website.
- Navigate to the specific movie page and extract data such as rating, genre, director, year, title, rt_score, audience score, box office rank, cast names, and more.

### 4. Maintenance:
- A separate script to periodically update older movies' rt_scores in the database.

## Usage

Detailed instructions on setting up and running the scraper will be added as the project develops.

## Contribution

Feel free to fork this repository and submit pull requests for any enhancements.
