# The Polite Scraper

## 📌 Project Overview

The Polite Scraper is a Python-based web scraping project that collects book information from a practice website. It follows responsible scraping practices by using a custom User-Agent, checking robots.txt, applying rate limiting, cleaning extracted data, and storing the results in JSON format.

---

## 🚀 Features

- Fetch web pages using Requests
- Parse HTML with BeautifulSoup
- Extract book information
- Clean scraped data
- Save structured records in JSON
- Check robots.txt
- Apply rate limiting
- Modular project structure

---

## 🛠️ Technologies Used

- Python 3
- Requests
- BeautifulSoup4
- JSON
- lxml

---

## 📂 Project Structure

```
The polite scraper/
│
├── data/
│   └── products.json
├── scraper.py
├── parser.py
├── cleaner.py
├── robots.py
├── save.py
├── requirements.txt
└── README.md
```

---

## 📥 Installation

```bash
git clone <repository-url>
cd "The polite scraper"
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python scraper.py
```

---

## 📊 Output

The scraper stores the extracted data in:

```
data/products.json
```

Each record contains:

- Title
- Price
- Availability
- Rating
- Product Link

---

## ✅ Responsible Scraping

- Uses a custom User-Agent
- Applies rate limiting
- Attempts to check robots.txt before scraping

---

## 👩‍💻 Author

**Khushi Kumari**

Backend AI Engineering Internship Assignment – FlyRank