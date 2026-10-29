# Student Performance Prediction 🎓

A beginner-friendly machine learning project that predicts whether a student will pass or fail based on their prior term scores ($G1$ and $G2$). Built with Scikit-Learn and deployed using Streamlit.

---

## 📌 Project Overview

In secondary education, tracking student progress early allows educators to step in before final examinations. This project builds a binary classification pipeline using **Logistic Regression** to predict final student performance (`1 = Pass`, `0 = Fail`) using first-period ($G1$) and second-period ($G2$) evaluation marks.

### Key Objectives
* Build and evaluate a baseline classification model.
* Avoid common beginner pitfalls like data leakage by training strictly on split training sets (`xtrain`, `ytrain`).
* Package the model into an interactive, deployable web app using Streamlit.

---

## 📊 Dataset Description

The dataset is derived from the standard UCI Student Performance dataset (`student-mat.csv` / cleaned version):
* **`G1`**: First period grade (numeric: 0 to 20)
* **`G2`**: Second period grade (numeric: 0 to 20)
* **`G3`**: Final grade (numeric: 0 to 20, kept out of training to prevent target leakage)
* **`performance`**: Target label (`1` if $G3 \ge 10$, `0` otherwise)

---

## 🛠️ Project Structure

```text
├── StudentPerfomancePrediction.ipynb  # Exploratory analysis, training, and evaluation
├── StudentPerformance.pkl             # Serialized trained model
├── app.py                             # Streamlit web application
├── requirements.txt                   # Project dependencies
└── README.md                          # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/student-performance-prediction.git
cd student-performance-prediction
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```

The app will start locally at `http://localhost:8501`.

---

## 📈 Model Performance & Evaluation

* **Algorithm**: Logistic Regression
* **Input Features**: $G1$ (Period 1 Grade), $G2$ (Period 2 Grade)
* **Evaluation Metrics**:
  * Accuracy: ~87.34% on test split
  * Precision & Recall balanced across both pass/fail outcomes

---

## 💡 Key Learnings & Improvements Made
1. **Prevented Data Leakage**: Switched from training on the entire dataset (`x, y`) to fitting strictly on `xtrain` and testing on `xtest`.
2. **Fixed Feature Name Warnings**: Passed sample inputs wrapped in Pandas DataFrames with explicit column names (`['G1', 'G2']`).
3. **Target Leakage Prevention**: Kept the final grade ($G3$) excluded from predictor features.
4. **Interactive Deployment**: Built a simple slider interface in Streamlit for real-time predictions.

---

## 👤 Author
* Developed by a passionate aspiring data scientist / machine learning fresher.
* Feel free to connect or open an issue for suggestions!
