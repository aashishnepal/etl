# ETL Task: Extracting Comedy Movies from Shows Dataset

## Overview

This document outlines the process of extracting comedy movies from a dataset named "shows.csv", available on Kaggle, which contains movies and shows up until 2023 according to their IMDb rating. The extracted comedy movies are then processed and stored in a MySQL database under a table named "movie_comedy".

## Process Steps

### 1. Dataset Preparation

- **Source**: Kaggle dataset "shows.csv"
- **Content**: Movies and shows up until 2023, categorized by IMDb rating.

### 2. Separation Based on Runtime

- **Action**: The dataset was split into two categories:
  - Short movies with runtime less than 1 hour.
  - Shows/movies with runtime greater than or equal to 1 hour.

### 3. Data Combination and Selection

- **Files Combined**: Two CSV files were combined into a single DataFrame.
- **Columns Selected**: Only the following columns were retained:
  - Name
  - Year
  - Runtime
  - Ratings
  - Genre

### 4. Filtering for Comedy Genres

- **Criteria**: Movies were filtered based on the presence of 'comedy' in the genre field, accounting for variations in spelling or casing.

### 5. Handling Missing Values

- **Ratings**: Any `NaN` values in the 'ratings' column were replaced with 0.
- **Genre**: An empty 'genre' column was filled with rounded star values derived from the 'ratings' column, effectively renaming the column to 'stars'.

### 6. Removing Duplicates

- **Method**: Duplicate entries were removed based on the 'name' column, retaining the first occurrence.

### 7. Sorting

- **Order**: The resulting DataFrame was sorted by 'ratings' in ascending order.

### 8. Saving to CSV

- **File**: The processed data was saved to a CSV file named "unique_comedy_movies.csv".

### 9. Storing in MySQL

- **Database**: A MySQL server was connected to.
- **Table Creation**: A table named "movie_comedy" was created within the database.
- **Insertion**: The contents of "unique_comedy_movies.csv" were inserted into the "movie_comedy" table.

## Conclusion

This ETL task efficiently extracts and processes comedy movies from a comprehensive dataset, enhancing the usability of the data for further analysis or application development. By leveraging Python for data manipulation and MySQL for storage, this process provides a robust foundation for exploring the characteristics and popularity of comedy movies.

Citations:
