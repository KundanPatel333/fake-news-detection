📰 Fake News Detection System
📌 Overview

This project is a Fake News Detection system that classifies news articles as FAKE or REAL using machine learning and natural language processing (NLP).

The model is trained on a labeled dataset and deployed using a Flask web application for real-time predictions.

🚀 Features
Detects whether a news article is fake or real
Uses TF-IDF Vectorization for text processing
Trained using Passive Aggressive Classifier
Simple web interface (Flask) for user input
Real-time prediction output
🛠️ Technologies Used
Python
Pandas, NumPy
Scikit-learn (TF-IDF, PassiveAggressiveClassifier)
Flask
HTML, CSS
Pickle (Model Serialization)
📂 Project Structure
Fake_News_Detection/
│
├── app.py                     # Flask app for prediction
├── train_and_save_model.py    # Model training script
├── test.py                    # Testing script
├── news.csv                   # Dataset
├── finalized_model.pkl        # Trained model
├── vectorizer.pkl             # TF-IDF vectorizer
├── csv_to_pdf.py              # Utility script
├── news_demo.pdf              # Sample output
│
├── static/
│   ├── css/
│   │   └── style.css          # Styling
│   └── images/
│       └── hero.svg           # UI image
│
└── templates/
    ├── base.html              # Base template
    ├── index.html             # Input page
    └── result.html            # Output page
⚙️ How It Works
Load trained model and vectorizer
User inputs news text through web interface
Text is converted into numerical features using TF-IDF
Model predicts whether the news is FAKE or REAL
Result is displayed on the webpage
▶️ How to Run the Project
1. Install dependencies
pip install -r requirements.txt
2. Run the Flask app
python app.py
3. Open in browser
http://127.0.0.1:5000/
📊 Model Details
Algorithm: Passive Aggressive Classifier
Feature Extraction: TF-IDF
Accuracy: ~92–94%
📌 Future Improvements
Add more advanced NLP models (e.g., BERT)
Improve UI/UX
Deploy on cloud (AWS/Heroku)
🙌 Conclusion

This project demonstrates a complete machine learning pipeline, including:

Data preprocessing
Feature extraction
Model training
Evaluation
Deployment using Flask

