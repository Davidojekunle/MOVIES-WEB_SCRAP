import requests
from bs4 import BeautifulSoup
import sqlite3
import threading
import os


base_url = "https://nkiri.com/category/international/"
n = range(1, 79)


def create_database():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS International (
                    id INTEGER PRIMARY KEY,
                    movie_name TEXT,
                    date TEXT,
                    image TEXT,
                    url TEXT,
                    detail TEXT)''')
    conn.commit()
    conn.close()
    

def insert_data(movie_name, date, image, url, detail):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO International VALUES(?, ?, ?, ?, ?)", movie_name, date, image, url, detail)
    conn.commit()
    conn.close()
    

def extract_data():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for movie in soup.find_all('div', {'class': 'movie-item'}):
        movie_name = movie.find('h2', {'class': "blog-entry-title entry-title"})
        name = movie_name.text.strip()
        dates =  date.find('div', {'class': "blog-entry-date clr"})
        date = dates.text.strip()
        img = movie.find('img')
        image = img.get('src')
        details_preview = movie.find('p', {'class': 'movie-details'})
        detail = details_preview.text.strip()
        url = movie.find('a')['href']
        
    create_database()  
    # print("Inserting data into database...")
    insert_data(name, date, image, url, detail)
    # print("Data insertion complete.")


# def run_async_with_threading():
#     thread = threading.Thread(target=extract_data)
#     thread.start()
#     thread.join()

# if __name__ == "__main__":
#     run_async_with_threading()
    