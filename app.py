from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# ---------------------------------
# Load saved model and vectorizer
# ---------------------------------
with open("finalized_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    tfidf = pickle.load(f)

# ---------------------------------
# Routes
# ---------------------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    news = request.form.get("news")

    # Safety check
    if not news or news.strip() == "":
        return render_template(
            "result.html",
            prediction="No input provided",
            news_text=""
        )

    # Transform input and predict
    vector = tfidf.transform([news])
    prediction = model.predict(vector)[0]

    return render_template(
        "result.html",
        prediction=prediction,
        news_text=news
    )

# ---------------------------------
# Run app
# ---------------------------------
if __name__ == "__main__":
    app.run(debug=True)
