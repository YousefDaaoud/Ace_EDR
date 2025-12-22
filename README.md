🛡️ Ace EDR
Mini Endpoint Detection & Response (EDR) Engine
<p align="center"> <strong>Lightweight • Defensive • Research-Driven</strong><br/> Python-based Mini EDR for Blue Team & Security Engineering </p> <p align="center"> <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge"/> <img src="https://img.shields.io/badge/Linux-Kali%20%7C%20Ubuntu-black?style=for-the-badge"/> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/> </p>
📌 Overview

Ace EDR is a Python-based Mini Endpoint Detection & Response (EDR) engine built for
security research, Blue Team training, and defensive engineering practice.

It simulates real-world EDR behavior, including:

Endpoint process monitoring

Heuristic-based behavioral detection

Automated response actions

GUI-based visibility

Self-protection mechanisms

⚠️ Disclaimer
This project is for educational and research purposes only.
It is not a replacement for commercial EDR products.

🎞️ Live Demo (GUI)
<p align="center"> <img src="gifs/gui-dashboard.gif" width="800"/> </p>

📁 Replace gifs/gui-dashboard.gif with your actual recorded demo
(you can record using peek, obs, or byzanz-record)

✨ Key Features

🔍 Real-Time Process Monitoring

🧠 Heuristic-Based Detection Engine

🛑 Response Engine (Monitor / Kill Modes)

🌐 Network Connection Monitoring

📁 File System Monitoring

🖥️ Dark-Mode GUI (Kali Linux Friendly)

🔒 Self-Protection Logic

🧵 Multi-Threaded Architecture

📜 Structured Logging System

🧠 Detection Capabilities

Ace EDR identifies suspicious activity using behavioral heuristics, including:

Abnormal or sustained CPU usage

Suspicious or masquerading process names

Rapid process spawning (fork bombs / stress tools)

Unauthorized outbound network connections

Common abuse patterns (DoS tools, reverse shells)

<p align="center"> <img src="gifs/detection-alert.gif" width="800"/> </p>

Detection logic is fully extensible via custom heuristics.

🛑 Response Engine

Ace EDR supports two response modes:

Mode	Description
MONITOR_ONLY	Logs detections without terminating processes
ACTIVE_RESPONSE	Automatically terminates malicious processes
<p align="center"> <img src="gifs/response-kill.gif" width="800"/> </p>

Mode switching is handled via responder configuration.

🧱 Project Architecture
Ace-EDR/
├── core/        # Core EDR logic (agent, detector, responder)
├── detection/   # Heuristics & detection rules
├── services/    # OS-level services (process, network)
├── gui/         # PyQt-based dashboard
├── logs/        # Runtime logs
├── main.py      # Entry point
├── requirements.txt
└── README.md

⚙️ Requirements

Python 3.9+

Linux OS (Recommended: Kali Linux / Ubuntu)

📦 Installation
git clone https://github.com/USERNAME/Ace-EDR.git
cd Ace-EDR

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

▶️ Usage
python3 main.py


The EDR agent and GUI start from a single command.

<p align="center"> <img src="gifs/startup.gif" width="800"/> </p>
🧪 Testing Scenarios

High CPU activity

yes > /dev/null


Long-running process

sleep 1000


Ace EDR should detect and respond accordingly.

🔐 Security Design Notes

Self-protection prevents terminating the EDR itself

Handles race conditions gracefully

Safe process termination logic

Thread-safe interaction between agent & GUI

📊 Logging

All detections and response actions are logged to:

logs/edr.log


Logs are structured for future SIEM / SOAR integration.

<p align="center"> <img src="gifs/logging.gif" width="800"/> </p>
🚧 Roadmap

🤖 Machine Learning–based detection

🌐 Threat Intelligence integration

🌳 Process tree visualization

⚙️ Systemd service mode

🚨 Alert severity levels

📡 JSON / API output

🔄 SOAR integration

📜 License

Released under the MIT License.

👨‍💻 Author

j0h4ck
Blue Team • Malware Analysis • Defensive Security

Contributions, forks, and improvements are welcome 🤝
