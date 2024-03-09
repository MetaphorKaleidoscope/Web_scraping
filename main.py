# scrape a website for data that you are interested
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


URL = "https://www.wired.co.uk/article/best-sci-fi-books"

response = requests.get(URL)

best_science_fiction_books = response.text

soup = BeautifulSoup(best_science_fiction_books, "html.parser")

all_books = soup.find_all(name="h2")


titles = []
years = []
for book in all_books:
    year = re.search("\(([^)]+)", str(book)).group(1)
    years.append(year)
    titles.append(book.getText().replace('by', '').replace(f'({year})', '').split(','))

the_title = [title[0] for title in titles]
author = [title[1] for title in titles]

df = pd.DataFrame({'title': the_title, 'author': author, 'year': years})

# Export Pandas DataFrame to CSV
df.to_csv('best_science_fiction_books.csv')
