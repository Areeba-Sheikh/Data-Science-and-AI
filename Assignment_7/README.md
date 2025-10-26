### **Week 7: Supervised Learning – Classification (Logistic Regression & Random Forest)**

**Assignment Title:** Supervised Learning – Classification

---

**Steps Taken:**

Loaded the cleaned dataset (telecom_customer_churn_cleaned.csv) into Jupyter Notebook.

Checked for missing values and handled them using fillna() to avoid NaN-related errors.

Selected ‘Customer Status’ as the target variable (converted to numeric labels using LabelEncoder).

Split the dataset into train (80%) and test (20%) sets.

Trained Logistic Regression and Random Forest Classifier models using sklearn.

Evaluated both models using accuracy score, confusion matrix, and classification report.

Compared the results and determined which model performed better.

Plotted the ROC Curve (One-vs-Rest) for multiclass evaluation.

---


**Output:**

**Classification Report (Sample):**

      precision    recall  f1-score   support

           0       0.97      0.93      0.95       361
           1       0.97      0.86      0.92        88
           2       0.97      1.00      0.99       936

    accuracy                           0.97      1385
   macro avg       0.97      0.93      0.95      1385
weighted avg       0.97      0.97      0.97      1385

Confusion Matrix:

[[336   2  23],[ 11  76   1],[  1   0 935]]


ROC Curve:
A smooth curve showing high AUC values across all classes, indicating strong model performance.

---

**Challenges Faced:**

Encountered ValueError: Input X contains NaN, which was resolved by filling missing numeric data using median imputation.

The ROC Curve initially failed due to multiclass format not being supported; fixed by using One-vs-Rest (OVR) approach.

Fine-tuned parameters for better accuracy and stability.

---

**Project Milestone:**

Achieved over 97% accuracy using Random Forest Classifier.
This week marked the completion of supervised model training and evaluation, preparing for unsupervised learning next week
