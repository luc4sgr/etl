*A Streamlit-powered data pipeline to scrape, transform and visualize notebook offers from Mercado Livre.*


🇧🇷 [Leia em português](README.pt-br.md)

---

### 📸 Dashboard Previews

![image](https://github.com/user-attachments/assets/c518dd9b-fcfe-4bcb-be2f-583f36853413)

![image](https://github.com/user-attachments/assets/e33d9920-0c28-482b-9d7c-359a7d3a4dbf)

---

## ✨ Features

- 🔍 **Scrapy Spider** to collect notebook listings from Mercado Livre (up to 10 pages).
- 🔧 **ETL script** to clean, transform and store the scraped data in SQLite.
- 📊 **Interactive Dashboard** using Streamlit for KPIs and visual insights.
- 🧼 **Data Cleaning & Type Conversion** (e.g., prices, ratings).
- 🗃️ **SQLite Integration** for local storage and analytics.

---

## 🏗️ Project Structure

```
tielytics/
├── src/
│   ├── scrapy_spider/           # Scrapy spider to extract data
│   │   └── notebook_spider.py
│   ├── transform/               # Data cleaning and transformation
│   │   └── main.py
│   └── dashboard/               # Streamlit dashboard app
│       └── app.py
├── data/                        # SQLite DB and scraped files
├── requirements.txt             # Python dependencies
└── README.md
```

---

## 🔧 Requirements

- Python 3.12+
- Scrapy
- Pandas
- Streamlit
- SQLite (standard with Python)
- All dependencies in `requirements.txt`

---

## 🚀 Installation

### Standard Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/MercadoNotebook.git
cd MercadoNotebook

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🕷️ Run the Spider (Scrapy)

```bash
cd src/scrapy_spider
scrapy runspider notebook_spider.py -o ../../data/data.jsonl
```

---

## 🧹 Run the ETL Process

```bash
cd ../transform
python main.py
```

---

## 📊 Launch the Dashboard

```bash
cd ../dashboard
streamlit run app.py
```

---

## 🧪 Testing

*Tests not included, but you can integrate with `pytest` for custom pipelines or unit tests.*
