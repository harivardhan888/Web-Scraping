from bs4 import BeautifulSoup
import requests
import openpyxl
import pandas as pd
import configparser
import mysql.connector

# Below line is used to read and write configurations
config = configparser.RawConfigParser()

# File my.properties contains host, user, password, database details
config.read(filenames='my.properties')

# These are used to get details from file
host = config.get('mysql', 'host')
user = config.get('mysql', 'user')
password = config.get('mysql', 'password')
database = config.get('mysql','db')

# This block ensures that this program is connected to MYSQL database
scrap_db = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

# It is a cursor object used to execute queries
cursor = scrap_db.cursor()

# This is a query to create a table in a database
cursor.execute("Drop Table if exists BOOK")
sql = """CREATE TABLE BOOK (
TITLE VARCHAR(500),
RATING VARCHAR(6),
PRICE FLOAT,
AVAILABILITY VARCHAR(20)
)"""

cursor.execute(sql)


# This is a block to write data into a xlsx file
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Books'
sheet.append(['Book Title', 'Star Rating', 'Price', 'Availability'])

books = []

# This block represents web scraping part
try:
    for i in range(1, 51):
        url = f'https://books.toscrape.com/catalogue/page-{i}.html'
        link = requests.get(url)

        # Status code 200 means given url is available permissions to scrape that web page
        if link.status_code != 200:
            link.raise_for_status()

        soup = BeautifulSoup(link.content, 'html.parser')
        order_list = soup.find('ol')
        cards_list = order_list.find_all('article', class_='product_pod')
        for card in cards_list:
            c_rating = card.find('p')
            rating = c_rating['class'][1]
            h3 = card.find('h3')
            a_title = h3.find('a')
            title = a_title['title']
            div = card.find('div', class_ = 'product_price')
            p_price = div.find('p', class_ = 'price_color')
            tag = p_price.text.strip()
            price = float(tag[1:])
            avail_tag = card.find('p', class_ = 'instock availability')
            availability = avail_tag.text.strip()
            sheet.append([title, rating, price, availability])
            books.append([title, rating, price, availability])
            cursor.execute(
                "INSERT INTO BOOK (TITLE, RATING, PRICE, AVAILABILITY) VALUES (%s, %s, %s, %s)",
                (title, rating, price, availability)
            )


# This blocks will execute if there are issues
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"An error occurred other than http error: {err}")


# This line used to save changes in the database
scrap_db.commit()
scrap_db.close()

# It saves xlsx file
excel.save("Books.xlsx")


# It creates a dataframe of data using pandas library and saving scraped data into csv file
df = pd.DataFrame(books, columns = ['Title', 'Star Rating', 'Price', 'Availability'])
df.to_csv('books.csv')
