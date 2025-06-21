# Amharic-E-commerce-Data-Extractor

## Objective

Transform messy Telegram posts into a smart FinTech engine that reveals which vendors are the best candidates for a loan.

---

## Task 1: Data Ingestion and Data Preprocessing

### Methodology

- Extract messages from selected Telegram channels using the Telethon library.
- Normalize Amharic text (removes unwanted characters, spaces, and normalizes Unicode).
- Handle media detection (photo/document), prepare file paths for potential downloads.
- Store structured data into a CSV file inside a `data/` folder.
- Use `.env` file for securely loading Telegram API credentials.

---

## File Structure

project/
├── data/
│ ├── preprocessed_data.csv
├── src/
│ ├── telegram_scraper.py
├── notebook/
│ ├──
├── requirements.txt
├── .gitignore
└── README.md

---

## How to Run

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

   ```

2. Set up environment variables

- Create a .env file in the root directory with the following:

  ```bash
  API_ID=your_api_id
  API_HASH=your_api_hash
  PHONE=+2519xxxxxxxx

  ```

3. Run the Telegram scraper

   ```bash
   python src/telegram_scraper.py

   ```

- Preprocessed messages will be saved to `data/preprocessed_data.csv`.

---

## KPIs

- Vendor frequency

- Engagement metrics

- Product pricing distribution

- Media presence

- Loan eligibility heuristics

---
