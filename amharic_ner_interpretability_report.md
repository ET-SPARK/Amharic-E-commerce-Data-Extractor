
# Amharic NER Model Interpretability Report

## 1. Model Overview
- **Model**: ./amharic-ner-model (based on xlm-roberta-base)
- **Task**: Named Entity Recognition (NER) for Amharic text
- **Labels**: ['B-LOC', 'B-PRICE', 'B-Product', 'I', 'I-LOC', 'I-PRICE', 'I-Product', 'O']

## 2. SHAP Analysis
### Sample Text: Workout Body Trimmer Universal exercise machine for the home Develops strengthens various muscle groups Strengthens the muscles of the back chest Does not create unnecessary stress on the spine Fixed on one or both legs Made from elastic materials ዋጋ ፦ 750 ብር ውስን ፍሬ ነው ያለው አድራሻ መገናኛ ደራርቱ ህንፃ ጎን መሰረት ደፋር ሞል ሁለተኛ ፎቅ ቢሮ ቁ . S05S06 0902660722 0928460606 በTelegram ለማዘዝ ይጠቀሙ @ zemencallcenter @ zemenexpressadmin ለተጨማሪ ማብራሪያ የቴሌግራም ገፃችን httpstelegram . mezemenexpress
### SHAP Insights:
- Top contributing tokens for each label:
SHAP computation failed.

## 3. LIME Analysis
### LIME Explanation for Sample:
LIME computation failed.

## 4. Performance Metrics
### Classification Report:
|              |   precision |   recall |   f1-score |   support |
|:-------------|------------:|---------:|-----------:|----------:|
| LOC          |  0.0152672  |      1   | 0.0300752  |         2 |
| Product      |  0          |      0   | 0          |         8 |
| micro avg    |  0.0152672  |      0.2 | 0.0283688  |        10 |
| macro avg    |  0.00763359 |      0.5 | 0.0150376  |        10 |
| weighted avg |  0.00305344 |      0.2 | 0.00601504 |        10 |

## 5. Difficult Cases Analysis
### Number of Difficult Cases: 8
### Example Difficult Case:
{'index': 0, 'tokens': ['Workout', 'Body', 'Trimmer', 'Universal', 'exercise', 'machine', 'for', 'the', 'home', 'Develops', 'strengthens', 'various', 'muscle', 'groups', 'Strengthens', 'the', 'muscles', 'of', 'the', 'back', 'chest', 'Does', 'not', 'create', 'unnecessary', 'stress', 'on', 'the', 'spine', 'Fixed', 'on', 'one', 'or', 'both', 'legs', 'Made', 'from', 'elastic', 'materials', 'ዋጋ', '፦', '750', 'ብር', 'ውስን', 'ፍሬ', 'ነው', 'ያለው', 'አድራሻ', 'መገናኛ', 'ደራርቱ', 'ህንፃ', 'ጎን', 'መሰረት', 'ደፋር', 'ሞል', 'ሁለተኛ', 'ፎቅ', 'ቢሮ', 'ቁ', '.', 'S05S06', '0902660722', '0928460606', 'በTelegram', 'ለማዘዝ', 'ይጠቀሙ', '@', 'zemencallcenter', '@', 'zemenexpressadmin', 'ለተጨማሪ', 'ማብራሪያ', 'የቴሌግራም', 'ገፃችን', 'httpstelegram', '.', 'mezemenexpress'], 'true_labels': ['B-Product', 'I-Product', 'I-Product', 'I-Product', 'I-Product', 'I-Product', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 'pred_labels': ['B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC', 'B-LOC'], 'incorrect_positions': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]}

## 6. Recommendations for Improvement
- **Ambiguous Entities**: If 'LOC' performance is low, collect more diverse location data.
- **Overlapping Entities**: Enhance tokenization to handle multi-word entities.
- **Data Augmentation**: Use synthetic Amharic NER data to increase dataset size.
- **Hyperparameter Tuning**: Try learning rates (e.g., 5e-5) or more epochs (e.g., 5).
