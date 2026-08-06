import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def extract_books(url):
    headers = {
        "User-Agent": "FlyRank Internship Scraper - Khushi"
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    time.sleep(2)

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    data = []

    for book in books:
        title = book.h3.a["title"]

        price = (
            book.find("p", class_="price_color")
            .get_text(strip=True)
            .replace("Â", "")
            .replace("£", "")
        )

        availability = (
            book.find("p", class_="instock availability")
            .get_text(strip=True)
        )

        rating = book.p["class"][1]

        link = urljoin(url, book.h3.a["href"])

        data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "link": link
        })

    return data