import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# -------------------------------
# 1. Load dataset
# -------------------------------
df = pd.read_csv("news.csv")

X = df["text"]
y = df["label"]

# -------------------------------
# 2. Train-test split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 3. TF-IDF Vectorizer
# -------------------------------
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_df=0.7
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# -------------------------------
# 4. Train model
# -------------------------------
model = PassiveAggressiveClassifier(max_iter=50)
model.fit(X_train_tfidf, y_train)

# -------------------------------
# 5. Evaluate model
# -------------------------------
y_pred = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Model training completed")
print("Accuracy:", round(accuracy * 100, 2), "%")
print("Confusion Matrix:")
print(conf_matrix)

# -------------------------------
# 6. Save model and vectorizer
# -------------------------------
with open("finalized_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("Model saved as finalized_model.pkl")
print("Vectorizer saved as vectorizer.pkl")
