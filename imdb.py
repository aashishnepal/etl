import pandas as pd
import mysql.connector
from mysql.connector import Error


# Connect to MySQL
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="unique_comedy_movies"
    )
    if connection.is_connected():
        db_info = connection.get_server_info()
        print(f"Connected to MySQL Server version {db_info}")
except Error as e:
    print(f"Error connecting to MySQL Platform '{e}'")



def map_ratings_to_stars(rating):
    try:
        rating_value = float(rating)
        
      
        num_stars = max(1, round(rating_value))
        

        return '★' * num_stars
    except ValueError:
        print(f"Warning: Unable to convert '{rating}' to a float.")
        return rating 



short_movies_df = pd.read_csv('short_movies.csv')
movies_shows_df = pd.read_csv('movies_shows.csv')

combined_df = pd.concat([short_movies_df, movies_shows_df])

selected_columns = combined_df[['name', 'year', 'runtime', 'ratings','genre']]

selected_columns['genre'] = selected_columns['genre'].fillna('Unknown')

comedy_movies = selected_columns[selected_columns['genre'].str.lower().str.contains('comedy')]

comedy_movies_sorted = comedy_movies.sort_values(by='ratings', ascending=False)


unique_comedy_movies = comedy_movies_sorted.drop_duplicates(subset='name', keep='first')



unique_comedy_movies['ratings'] = unique_comedy_movies['ratings'].fillna(0)
# unique_comedy_movies['genre'] = unique_comedy_movies['ratings'].apply(map_ratings_to_stars)
unique_comedy_movies['genre'] = unique_comedy_movies['ratings'].apply(lambda x: map_ratings_to_stars(x) if pd.notnull(map_ratings_to_stars(x)) else 0)  # Use 0 or another suitable default value
default_value = 'Unknown'  # Choose a suitable default value for each column
unique_comedy_movies.fillna(value=0, inplace=True)
unique_comedy_movies.rename(columns={'genre': 'stars'}, inplace=True)

unique_comedy_movies.to_csv('unique_comedy_movies.csv', index=False)

print("Comedy movies saved to unique_comedy_movies.csv")

# unique_comedy_movies.dropna(inplace=True)


cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS movie_comedy (
    name VARCHAR(255),
    year VARCHAR(25),
    runtime INT,
    ratings VARCHAR(255),
    stars TEXT
)
"""

try:
    cursor.execute(create_table_query)
    print("Table created successfully")
except Error as e:
    print(f"Error creating table: {e}")

insert_data_query = """
INSERT INTO movie_comedy (name, year, runtime, ratings,stars) VALUES (%s, %s, %s, %s, %s)
"""

for index, row in unique_comedy_movies.iterrows():
    try:
        cursor.execute(insert_data_query, tuple(row))
    except Error as e:
        print(f"Error inserting data: {e}")

connection.commit()
print("Data inserted successfully")

cursor.close()
connection.close()
print("MySQL connection is closed")
