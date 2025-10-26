### **Weekly Assignment Submission**

**Assignment Title:** Correlation Analysis

---

### **Steps Taken**

1. Loaded the cleaned **Telecom Customer Churn** dataset in Colab Notebook.
2. Performed correlation analysis to find relationships between independent features and the target variable (`Customer Status`).
3. Used the `.corr()` function in pandas to calculate correlation values.
4. Sorted and identified the **top 3 features** most related to customer churn.

---

### **Output**

**Top 3 Correlated Features with Customer Churn:**

| Feature        | Correlation |
| -------------- | ----------- |
| Monthly Charge | 0.175817    |
| Age            | 0.112251    |
| Longitude      | 0.024238    |

**Target Variable:** `Customer Status`
**dtype:** float64

---

### **Challenges Faced**

* Needed to confirm correct encoding of categorical variables before correlation.
* Slight difficulty interpreting weak correlation values due to data type variations.
