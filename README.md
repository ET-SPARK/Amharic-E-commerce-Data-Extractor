# Amharic-E-commerce-Data-Extractor

## 🎯 Objective

Transform messy Telegram posts into a smart FinTech engine that reveals which vendors are the best candidates for a loan.

---

## ✅ Task 1: Data Ingestion and Preprocessing

### 🔍 Methodology

- Extract messages from selected Telegram channels using the Telethon library.
- Normalize Amharic text (remove unwanted characters, extra spaces, and normalize Unicode).
- Handle media (photos, documents) and prepare file paths for future downloads.
- Save structured message data into a CSV file (`data/preprocessed_data.csv`).
- Use `.env` file to securely manage Telegram API credentials (`API_ID`, `API_HASH`, `PHONE`).

---

## ✅ Task 2: Manual Labeling for NER (Named Entity Recognition)

### ✍️ Description

- Sampled 40 preprocessed messages from `preprocessed_data.csv`.
- Tokenized each message and labeled entities in **CoNLL format**, suitable for NER tasks.
- Target entities include:
  - `B-Product`, `I-Product` — Product names and descriptions
  - `B-PRICE`, `I-PRICE` — Price information (e.g., "1000 ብር")
  - `B-LOC`, `I-LOC` — Location names (e.g., "አዲስ አበባ")
  - `O` — Tokens outside any entity

### 📄 Output

- Labeled dataset saved as `data/conll_raw_sample.txt`.
- Each token is labeled on a separate line, with messages separated by a blank line.

---

## 📁 File Structure

## File Structure

project/
├── data/
│ ├── preprocessed_data.csv
│ ├── conll_raw_sample.txt
├── src/
│ ├── telegram_scraper.py
│ ├── conll_preprocessor.py
├── notebook/
│ ├──
├── requirements.txt
├── .env
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
