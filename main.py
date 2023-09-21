import requests
import selectorlib
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"
FILENAME = "data.txt"

connection = sqlite3.connect("data_sql_lite.db")

def scrape(url):
    """Scrape the page-source from the URL"""
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("local_extract.yaml")
    value = extractor.extract(source)['tours']
    return value

def store(ext_data):
    row = ext_data.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO events VALUES(?,?,?)", row)
    connection.commit()

def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM events WHERE band=? AND city=? AND date=?", (band, city, date))
    rows = cursor.fetchall()

    return rows

if __name__ == "__main__":
    while True:
        scraped_data = scrape(URL)
        extracted_data = extract(scraped_data)
        
        if str(extracted_data).lower() != "no upcoming tours":
            row = read(extracted_data)
            if not row:
                store(extracted_data)
                print(f"New information extracted!\n{extracted_data}")

        time.sleep(3)
