# 📦 Amharic E-commerce Data Extractor

## 🎯 Objective

Transform raw Telegram posts into a powerful FinTech engine capable of identifying the most loan-worthy vendors using Amharic-language data.

---

## ✅ Task 1: Data Ingestion & Preprocessing

### 🔍 Methodology

- Extracted messages from selected Telegram channels using the **Telethon** library.
- Normalized Amharic text by:
  - Removing unwanted characters and extra spaces.
  - Standardizing Unicode.
- Handled media (photos, documents) by storing references for future downloads.
- Saved structured messages into a CSV file: `data/preprocessed_data.csv`.
- Managed Telegram API credentials securely via a `.env` file (`API_ID`, `API_HASH`, `PHONE`).

---

## ✅ Task 2: Manual Labeling for NER (Named Entity Recognition)

### ✍️ Description

- Sampled 40 preprocessed messages from `preprocessed_data.csv`.
- Tokenized each message and labeled entities in **CoNLL format** for NER training.
- Labeled entities include:
  - `B-Product`, `I-Product` — Product names and descriptions.
  - `B-PRICE`, `I-PRICE` — Price information (e.g., "1000 ብር").
  - `B-LOC`, `I-LOC` — Location names (e.g., "አዲስ አበባ").
  - `O` — Tokens outside of any entity.

### 📄 Output

- Labeled dataset saved at `data/conll_raw_sample.txt`.
- Each token is on a new line; messages are separated by a blank line.

---

## ✅ Task 3: Fine-Tuning the NER Model

### ✍️ Description

- Loaded manually labeled CoNLL data from `data/conll_raw_sample.txt`.
- Used the `rasyosef/bert-tiny-amharic` pretrained model from Hugging Face.
- Tokenized and aligned labels with subwords.
- Fine-tuned the model for recognizing products, prices, and locations using the Hugging Face Trainer API.
- Evaluated performance using standard NER metrics.
- Saved the fine-tuned model for inference and deployment.

---

## ✅ Task 4: Model Comparison & Selection

### 🔍 Evaluation

- Fine-tuned and compared two models:
  - `bert-tiny-amharic`
  - `xlm-roberta-base`
- Evaluated using F1-score, precision, and recall.
- Logged detailed metrics and entity-level performance.

### 📌 Recommendation

- Explore `afro-xlmr-base` with a more balanced and enriched dataset for improved results.

---

## ✅ Task 5: Model Interpretability

### 🔍 Methodology

- Applied **SHAP** (SHapley Additive exPlanations) and **LIME** (Local Interpretable Model-agnostic Explanations) on predictions made by the fine-tuned `xlm-roberta-base` model.
- Analyzed token contributions to predictions (e.g., `B-LOC`, `B-Product`).
- Identified failure cases where predictions diverged from actual labels.
- Generated a classification report using `seqeval`.

### ✍️ Description

#### SHAP Analysis

- Attempted to compute SHAP values using `KernelExplainer` with a placeholder reference dataset.
- Computations failed due to memory constraints in Google Colab.

#### LIME Analysis

- Attempted to explain local predictions using LIME.
- Failed due to similar resource limitations.

#### Performance Metrics (on 8-sample test set)

| Entity        | Precision | Recall  | F1-score  | Instances |
| ------------- | --------- | ------- | --------- | --------- |
| LOC           | 1.53%     | 100%    | 3.01%     | 2         |
| Product       | 0%        | 0%      | 0%        | 8         |
| **Micro avg** | **1.53%** | **20%** | **2.84%** | —         |

#### Difficult Cases

- 8 instances had incorrect predictions.
- Example: a product description ("Workout Body Trimmer ...") was misclassified as `B-LOC` for all tokens, revealing confusion between entity types.

#### 📌 Recommendations

- Collect more diverse and representative **location** data.
- Improve tokenization, especially for multi-word entities.
- Augment training data with **synthetic Amharic NER** examples.
- Experiment with:
  - Higher learning rates (e.g., `5e-5`).
  - More epochs (e.g., `5+`).

### 📄 Output

- Interpretability results saved in `amharic_ner_interpretability_report.md`.
- Report includes:
  - Model summary
  - SHAP/LIME status
  - Performance metrics
  - Error analysis
  - Recommendations for improvement

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
│ ├── Model_Comparison_and_Selection.ipynb
│ ├── Fine_Tune_bert_tiny_amharic_Model.ipynb
│ ├── Fine_Tune_xlm_roberta_base_model.ipynb
│ ├── Model_Interpretability.ipynb
├── requirements.txt
├── .env
├── .gitignore
└── amharic_ner_interpretability_report.md
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
