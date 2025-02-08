from flask import Flask, render_template, request, jsonify
import joblib
import sqlite3

app = Flask(__name__)

# Load ML models
phishing_model = joblib.load("models/phishing_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect("threats.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    """Render the dashboard."""
    conn = get_db_connection()
    threats = conn.execute("SELECT * FROM threats ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", threats=threats)

@app.route("/scan-url", methods=["POST"])
def scan_url():
    """Scan a URL for phishing threats."""
    data = request.json
    url = data.get("url")
    features = vectorizer.transform([url])
    prediction = phishing_model.predict(features)[0]

    conn = get_db_connection()
    conn.execute("INSERT INTO threats (description, risk_level) VALUES (?, ?)",
                 (url, "Phishing" if prediction else "Safe"))
    conn.commit()
    conn.close()

    return jsonify({"url": url, "phishing_detected": bool(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
