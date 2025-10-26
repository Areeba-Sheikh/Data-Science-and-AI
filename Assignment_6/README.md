### **Weekly Assignment Submission**

**Assignment Title:** Logistic Regression & Random Forest Classification

---

### **Steps Taken**

1. Loaded the **Telecom Customer Churn (cleaned)** dataset in Colab Notebook.
2. Dropped irrelevant columns such as `Customer ID`, `Name`, and unnamed columns.
3. Automatically detected and encoded the **target column** (`Customer Status`).
4. Converted categorical variables to numeric using **one-hot encoding**.
5. Split data into **training (80%)** and **testing (20%)** sets.
6. Trained two models:

   * **Logistic Regression**
   * **Random Forest Classifier**
7. Compared model performance based on **accuracy score**.

---

### **Output**

| Model               | Accuracy                            |
| ------------------- | ----------------------------------- |
| Logistic Regression Accuracy:| 0.788 |
| Random Forest Accuracy:      | 0.973 |

🏆 **Best Model:** Random Forest

---

### **Challenges Faced**

* Needed to ensure the correct target column (`Customer Status`) was selected automatically.
* Managed missing values and categorical data before model training.
* Had to increase `max_iter` for Logistic Regression to ensure proper convergence.
