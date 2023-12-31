# Rotten Scraper

`rotten_scraper` is a Python-based web scraping tool designed to collect data from a popular movie review aggregate website. The extracted data is stored in a MongoDB database for further analysis and insights.

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/andrewuebe/rotten_scraper.git
cd rotten_scraper
```

### 2. Create and activate a virtual environment

To create a virtual environment:

`python -m venv venv`

To activate the virtual environment:

`source venv/bin/activate`

### 3. Activate dependencies

`pip install -r requirements.txt`

## Usage

To run the script, you can use the following command, replacing `[OPTIONS]` with the options flags below:
`python main.py [OPTIONS]`

### Options flags:
1. `--delete-copies`: this will identify and remove movies with duplicate titles from your database.
2. `--scrape:<endMovieYear`: This option will start the scraping process for movies up to the specified year. Replace `<endMovieYear` with the desired end year. For example, to scrape movies up to the year 2020 (not including that year), you would use `--scrape:2020`.

You can use both options together, and in any order, but the scripts will run in the order they appear in the list above.

`python main.py --delete-copies --scrape:2020`

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

## Contribution

Feel free to fork this repository and submit pull requests for any enhancements.
