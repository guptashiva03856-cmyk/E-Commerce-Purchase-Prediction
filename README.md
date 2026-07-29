# 🛒 E-Commerce Purchase Prediction using Machine Learning

## 📌 Project Overview

This project predicts whether a customer will make a purchase during an online shopping session using Machine Learning techniques. The project follows the CRISP-DM methodology and includes data preprocessing, model training, explainable AI, API development, Docker containerization, and MLflow experiment tracking.

---

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Multiple Machine Learning Models
- Hyperparameter Tuning
- Explainable AI (SHAP & LIME)
- FastAPI REST API
- Streamlit Web Application
- Docker Containerization
- MLflow Experiment Tracking

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SHAP
- LIME
- Joblib

### Frameworks
- FastAPI
- Streamlit

### DevOps & MLOps
- Docker
- MLflow

---

## 📂 Project Structure

```text
E_commerce/
│
├── api/
│   └── main.py
│
├── app/
│   └── app.py
│
├── data/
│   └── ecommerce_sessions.csv
│
├── models/
│   ├── gradient_boosting_model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── 01data.ipynb
├── 02eda.ipynb
├── 03data_preprocessing.ipynb
├── 04model_training.ipynb
├── 05_model_evaluation.ipynb
├── 06_hyperparameter_tuning.ipynb
├── 07_explainable_ai.ipynb
├── 08_save_model.ipynb
├── 09_mlflow.ipynb
│
├── Dockerfile
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📊 Machine Learning Models

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine
- Gradient Boosting (Best Model)

---

## 📈 Model Performance

The Gradient Boosting model achieved the best performance among all evaluated models.

---

## 🌐 Streamlit Application

The Streamlit app allows users to:

- Enter customer session details
- Predict purchase intent
- View prediction confidence
- Display customer session summary

---

## ⚡ FastAPI Endpoints

### Home

```
GET /
```

### Prediction

```
POST /predict
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t ecommerce-predictor .
```

Run the Docker container:

```bash
docker run -p 8501:8501 ecommerce-predictor
```

---

## 📊 MLflow

Start the MLflow UI:

```bash
mlflow ui
```

Open:

```
http://127.0.0.1:5000
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app/app.py
```

---

## 👨‍💻 Author

**Shiva Gupta**

B.Tech Artificial Intelligence & Data Science

Machine Learning | Data Science | Python

---