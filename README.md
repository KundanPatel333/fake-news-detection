# 📰 Fake News Detection System

## 📌 Project Overview

Developed an AI-powered Fake News Detection system capable of classifying news articles as **FAKE** or **REAL** using Machine Learning and Natural Language Processing (NLP) techniques.

The project was built to address the growing issue of misinformation on digital platforms by enabling automated verification of textual news content in real time.

The system is trained on a labeled news dataset and deployed through a Flask-based web application for interactive predictions.

---

# 🚀 Key Features

* Real-time fake news prediction
* NLP-based text preprocessing pipeline
* TF-IDF vectorization for feature extraction
* Passive Aggressive Classifier for efficient classification
* Interactive Flask web interface
* Fast and lightweight prediction workflow

---

# 🛠️ Tech Stack

### Programming & Frameworks

* Python
* Flask

### Machine Learning & NLP

* Scikit-learn
* TF-IDF Vectorizer
* Passive Aggressive Classifier

### Libraries

* Pandas
* NumPy
* Pickle

### Frontend

* HTML
* CSS

---

# ⚙️ System Workflow

1. User enters news content through the web interface
2. Input text undergoes preprocessing and cleaning
3. TF-IDF converts text into numerical feature vectors
4. Trained ML model analyzes the features
5. System predicts whether the news is FAKE or REAL
6. Result is displayed instantly on the web application

---

# 📊 Model Performance

* **Algorithm Used:** Passive Aggressive Classifier
* **Feature Engineering:** TF-IDF Vectorization
* **Achieved Accuracy:** ~92–94%

The model demonstrated strong performance on unseen validation data and provided fast inference for real-time predictions.

---

# 📂 Project Structure

```bash
Fake_News_Detection/
│
├── app.py
├── train_and_save_model.py
├── test.py
├── news.csv
├── finalized_model.pkl
├── vectorizer.pkl
│
├── static/
├── templates/
└── README.md
```

---

# ▶️ Running the Application

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Start Flask Server

```bash
python app.py
```

## Open in Browser

```bash
http://127.0.0.1:5000/
```

---

# 🔍 Challenges Solved

* Handling textual feature extraction efficiently
* Reducing noise in raw news content
* Building a lightweight yet accurate ML pipeline
* Deploying the trained model into a usable web application

---

# 📌 Future Improvements

* Integration with advanced transformer models like BERT
* Real-time news API integration
* Cloud deployment using AWS/Render/Heroku
* Enhanced UI/UX and explainable AI features

---

# 🙌 Conclusion

This project demonstrates an end-to-end Machine Learning workflow, including:

* Data preprocessing
* NLP-based feature engineering
* Model training & evaluation
* Web deployment using Flask
* Real-time inference pipeline

The project reflects practical implementation skills in Machine Learning, NLP, and AI application deployment.
