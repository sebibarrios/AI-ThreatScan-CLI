# AI-Powered Cybersecurity CLI

## 🚀 Overview
AI-Powered CLI for real-time cybersecurity threat detection, malware analysis, and phishing protection using machine learning models.

## 🔹 Features
- **Phishing URL Detection** – Identifies malicious URLs using NLP-based ML models.
- **Malware Analysis** – Detects malware using behavioral feature extraction and classification.
- **Network Traffic Monitoring** – Captures and analyzes packets for anomalies.
- **Threat Intelligence Integration** – Uses real-time threat feeds for detection.
- **IP Blacklisting & Reporting** – Blocks malicious IPs and generates security reports.

## 🔧 Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### **2️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the CLI**
```sh
python threatscan.py --help
```

## 📌 Usage
### **Scan a URL for Phishing Threats**
```sh
python threatscan.py scan-url https://suspicious-link.com
```

### **Analyze a File for Malware**
```sh
python threatscan.py detect-malware suspicious.exe
```

### **Monitor Network Traffic**
```sh
python threatscan.py monitor --log /var/log/network.log
```

### **Block a Malicious IP Address**
```sh
python threatscan.py block-ip 192.168.1.100
```

### **Generate a Security Report**
```sh
python threatscan.py generate-report --format json
```

## 🛠️ How It Works
1. **Phishing Detection**: Uses **TF-IDF & RandomForestClassifier** to classify URLs.
2. **Malware Analysis**: Extracts **file metadata, API calls, entropy**, and detects threats using ML.
3. **Network Monitoring**: Captures **packets with Scapy**, detects anomalies via **Autoencoders & Isolation Forest**.
4. **Threat Response**: Automates **IP blacklisting & alert generation**.

## 📂 Project Structure
```
|── threatscan.py         # Main CLI application
|── models/              # Trained ML models (phishing, malware)
|── data/                # Sample datasets
|── utils/               # Helper scripts
|── requirements.txt      # Dependencies
|── README.md            # Documentation
```

## 📌 Contributing
Contributions are welcome! Open an issue or submit a pull request to improve the project.

## 📜 License
This project is licensed under the **MIT License**.

