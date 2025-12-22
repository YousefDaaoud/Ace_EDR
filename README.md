
<h1 align="center">🛡️ Ace EDR</h1>

<p align="center">
  <em>Defensive • Research-Oriented • Minimal</em><br/>
  Mini Endpoint Detection & Response (EDR) Engine for Blue Team & Security Research
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-4B8BBE?style=flat"/>
  <img src="https://img.shields.io/badge/Platform-Linux-black?style=flat"/>
  <img src="https://img.shields.io/badge/License-MIT-2EA44F?style=flat"/>
</p>

---

## 📌 Overview

Ace EDR is a lightweight, Python-based Endpoint Detection & Response (EDR) engine
designed for Blue Team operations, defensive engineering, and security research.

It simulates core EDR capabilities including process monitoring, heuristic-based
detection, automated response actions, GUI visibility, and self-protection mechanisms.

This project is intended for educational and research purposes only and is not a
replacement for commercial EDR solutions.

---

## ✨ Key Capabilities

- Real-time process monitoring
- Heuristic-based behavioral detection
- Configurable response modes (monitor / terminate)
- Network activity observation
- Dark-mode GUI dashboard
- Self-protection logic
- Multi-threaded architecture
- Structured logging system

---

## 🛑 Response Modes

| Mode | Description |
|------|------------|
| MONITOR_ONLY | Detect and log suspicious activity |
| ACTIVE_RESPONSE | Automatically terminate malicious processes |

---

## 🧱 Architecture

Ace-EDR/
├── core/           Core EDR logic
├── detection/      Heuristics & rules
├── services/       System services
├── gui/            Dashboard interface
├── logs/           Runtime logs
├── main.py         Application entry point
└── requirements.txt

---

## ⚙️ Requirements

- Python 3.9+
- Linux (Kali Linux / Ubuntu )

---

## 📦 Installation

cd Ace-EDR

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---

## ▶️ Usage

python3 main.py

---

## 🧪 Testing Examples

yes > /dev/null
sleep 1000

---

## 📊 Logging

All detections and responses are logged to:

logs/edr.log

---

## 👨‍💻 Author

j0h4ck  
---


