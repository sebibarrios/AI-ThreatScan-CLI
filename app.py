from fastapi import FastAPI, UploadFile, File
import joblib
import uvicorn
from pydantic import BaseModel

app = FastAPI()

# Load AI models
phishing_model = joblib.load("models/phishing_model.pkl")
malware_model = joblib.load("models/malware_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

class URLRequest(BaseModel):
    url: str

@app.post("/scan-url")
def scan_url(request: URLRequest):
    """Detect phishing in a URL."""
    features = vectorizer.transform([request.url])
    prediction = phishing_model.predict(features)[0]
    return {"url": request.url, "phishing_detected": bool(prediction)}

@app.post("/detect-malware")
def detect_malware(file: UploadFile = File(...)):
    """Analyze file for malware."""
    content = file.file.read()  # Placeholder for feature extraction
    prediction = malware_model.predict([[len(content), 0.5, 200]])[0]  # Fake feature values
    return {"filename": file.filename, "malware_detected": bool(prediction)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
