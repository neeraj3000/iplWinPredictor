# 🏏 IPL Win Predictor

This project is a **Flask-based web application** that predicts the winning probability of IPL teams in real-time using machine learning. It is built using Python, Pandas, scikit-learn for modeling, and Flask for the backend web interface.

---

## 🚀 Features

- Predicts win probability based on:
  - Current score
  - Overs completed
  - Wickets fallen
  - Target score
- Flask web interface for user interaction
- Model trained using **IPL data from 2008 to 2023**

---

## 🧰 Tech Stack

- **Backend**: Python, Flask  
- **ML Model**: Scikit-learn (Logistic Regression)  
- **Data Processing**: Pandas, NumPy  
- **Visualization**: Matplotlib, Seaborn  
- **Frontend**: HTML, CSS (Bootstrap)

---

## 📁 Dataset

- Dataset contains match-by-match details from IPL 2008 to 2023.
- Features used for prediction:
  - Runs Left
  - Balls Left
  - Wickets Left
  - Current Run Rate (CRR)
  - Required Run Rate (RRR)

---

## 🧠 Model

- Cleaned and processed data using Pandas
- Used Logistic Regression for classification
- Evaluated with accuracy, ROC-AUC, and confusion matrix

---

## ▶️ Run the App Locally

### 1. Clone the Repository

```bash
git clone https://github.com/neeraj3000/iplWinPredictor.git
cd iplWinPredictor
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask App

```bash
python ipl_app.py
```

Then open your browser and go to:  
👉 `http://127.0.0.1:5000/`

---

## 🙌 Author

**Neeraj B**  
[GitHub](https://github.com/neeraj3000) | [LinkedIn](https://www.linkedin.com/in/neerajboggavarapu24)
