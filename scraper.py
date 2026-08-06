from parser import extract_books
from cleaner import clean_data
from save import save_json
from robots import check_robots

URL = "https://books.toscrape.com/"

if check_robots(URL):
    books = extract_books(URL)
    cleaned = clean_data(books)
    save_json(cleaned)

    print("\nFirst 5 Records:\n")
    for item in cleaned[:5]:
        print(item)

    print("\nScraping Completed Successfully!")