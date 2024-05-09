import requests
from bs4 import BeautifulSoup
import sqlite3
import os

def init_database():
        connection = sqlite3.connect('movies.db')
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS kdrama(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_title text,
        date text,
        link text
                                                                         
)""")
        connection.commit()
        connection.close()

def add_data(title, date, link):
    connection = sqlite3.connect('movies.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO kdrama (movie_title, date, link) VALUES (?, ?, ?)", (title, date, link))
    connection.commit()
    connection.close()

base_url = 'https://nkiri.com/category/asian-movies/download-korean-movies/'
n = range(1,8)
for num in n:
    url = f'{base_url}page/{num}'
    print(f"Getting data for page {num}")
    if num == 7:
        print("Successfully added into Database!")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for text in soup.find_all('div' ,{'class': 'blog-entry-content'}):
        title = text.find('h2', {'class': 'blog-entry-title entry-title'})
        f_title = title.text.strip()
        date = text.find('div', {'class': 'blog-entry-date clr'})
        f_date = date.text.strip()
        link = title.find('a')['href']
        name = f_title, f_date, link
        init_database()
        add_data(f_title, f_date, link)


