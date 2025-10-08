# 🛡️ Web App Firewall (WAF) Simulator

A complete, ready-to-use WAF simulator for detecting **XSS** and **SQL Injection** attacks using **Regex** & **Machine Learning**.

## 🚀 Tech Stack

- **FastAPI** — REST API for detection
- **Streamlit** — Log visualization dashboard
- **SQLite** — Log storage
- **scikit-learn** — ML model for attack detection

---

## ⚡ Features

- Detects **SQLi** and **XSS** via regex and ML
- Logs every request and result
- Visualizes logs and attack stats in Streamlit
- Plug-and-play, portable

---

## 🏁 Getting Started

### 1️⃣ Clone or Download the Project

Copy all files into a folder (e.g. `waf_simulator/`).

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI Server

```bash
uvicorn main:app --reload
```

### 4️⃣ Run the Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

### 5️⃣ Test with Sample Requests

```bash
python test_requests.py
```

---

## 🔬 How It Works

1. Send a payload to `/waf/check` API.
2. Regex patterns check for SQLi/XSS signatures.
3. If not matched, ML model (Naive Bayes) classifies payload.
4. Result stored in SQLite DB.
5. Streamlit dashboard visualizes logs and stats.

---

## 📚 Code Structure

| File             | Purpose                              |
|------------------|--------------------------------------|
| `main.py`        | FastAPI backend                      |
| `waf.py`         | WAF logic (regex + ML)               |
| `ml_model.py`    | ML model (train + predict)           |
| `streamlit_app.py` | Streamlit dashboard                |
| `test_requests.py` | Sample client requests             |
| `requirements.txt` | Python dependencies                |
| `logs.db`        | SQLite database (auto-generated)     |

---

## 🛡️ Detection

### 🔎 Regex

- **SQLi**: Detects keywords (`SELECT`, `DROP`, etc.), `'`, `--`, comments.
- **XSS**: Detects `<script>`, `javascript:`, `alert()`.

### 🤖 ML

- **Naive Bayes** classifier, sample payloads in `ml_model.py`.
- Used when regex fails.

---

## 📊 Visualization

- Recent requests and their classification.
- Attack type distribution chart.
- Powered by Streamlit.

---

## 🧪 Example

```python
import requests
res = requests.post("http://localhost:8000/waf/check", json={"payload": "<script>alert('XSS')</script>"})
print(res.json())  # {'payload': '<script>alert(\'XSS\')</script>', 'result': 'XSS'}
```

---

## 💡 Tips

- Start FastAPI server before using Streamlit or test client.
- ML model auto-trains if not found.
- Expand dataset and patterns for real-world use.

---

## 📝 License

MIT

---

## 🏆 Happy experimenting! 🚀