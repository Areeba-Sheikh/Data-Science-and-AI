
### **Weekly Assignment Submission**

**Assignment Title:** Unsupervised Learning – K-Means Clustering

---

### **Steps Taken**

1. Loaded the cleaned **Telecom Customer Churn** dataset into Jupyter Notebook.
2. Dropped irrelevant columns such as `Customer ID` and unnamed columns.
3. Selected numeric columns and filled missing values using **median imputation**.
4. Standardized data using `StandardScaler()` for optimal clustering performance.
5. Applied **K-Means Clustering (k=3)** to identify customer groups.
6. Added cluster labels back to the dataset for interpretation.
7. Used **PCA (2 components)** to reduce dimensionality for visualization.
8. Plotted a **2D scatter plot** showing customer clusters.

---

### **Output**

**Cluster Distribution:**

| Cluster | Count |
| ------- | ----- |
| 0       | 2480  |
| 1       | 1843  |
| 2       | 2600  |

**PCA Visualization:**
A colorful 2D scatter plot displaying **three distinct clusters** (green, blue, yellow) across two principal components — showing clear customer segmentation.

---

### **Challenges Faced**

* Encountered `ValueError: Length of values does not match length of index` due to dropping NaN rows — fixed by using **median imputation** instead.
* Tuned **K-Means parameters** (`n_init`, `random_state`) for more stable results.
* Adjusted **PCA visualization** for better interpretability and clarity.

---

### **Project Milestone**

Successfully applied **Unsupervised Learning** techniques (K-Means + PCA) to segment telecom customers into clear, meaningful groups.
