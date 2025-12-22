# 🛡️ Ace EDR
### Mini Endpoint Detection & Response (EDR) Engine

Ace EDR is a **lightweight, Python-based Endpoint Detection & Response engine** designed for **security research, Blue Team training, and defensive engineering practice**.

It simulates real EDR behavior including **process monitoring, heuristic detection, response actions, GUI visualization, and self-protection mechanisms**.

> ⚠️ This project is intended for educational and research purposes only.  
> It is **not** a replacement for commercial EDR solutions.

---

## ✨ Key Features

- 🔍 **Real-Time Process Monitoring**
- 🧠 **Heuristic-Based Detection Engine**
- 🛑 **Response Engine (Monitor / Kill modes)**
- 🌐 **Network Connection Monitoring**
- 📁 **File System Monitoring**
- 🖥️ **Dark Mode GUI (Kali Linux Friendly)**
- 🔒 **Self-Protection (EDR does not kill itself)**
- 🧵 **Multi-Threaded Architecture**
- 📜 **Structured Logging System**

---

## 🧠 Detection Capabilities

Ace EDR detects suspicious behavior using heuristic analysis, including:

- Abnormal CPU usage
- Suspicious process names
- Rapid process spawning
- Unauthorized network connections
- Potential abuse tools (e.g. stress tools, reverse shells)

Detection logic is **fully extensible** via custom heuristics.

---

## 🛑 Response Modes

The response engine supports two modes:

| Mode | Description |
|----|----|
| `MONITOR_ONLY` | Logs detections without terminating processes |
| `ACTIVE_RESPONSE` | Terminates malicious processes automatically |

You can switch modes easily from the responder configuration.

---

## 🧱 Project Architecture

Ace-EDR/
├── core/ # Core EDR logic (agent, detector, responder)
├── detection/ # Heuristics and detection rules
├── services/ # OS-level services (process, network)
├── gui/ # PyQt-based dashboard
├── logs/ # Runtime logs
├── main.py # Entry point
├── requirements.txt
└── README.md


---

## ⚙️ Requirements

- Python **3.9+**
- Linux OS (Recommended: **Kali Linux / Ubuntu**)

---

## 📦 Installation

bash
git clone https://github.com/USERNAME/Ace-EDR.git
cd Ace-EDR

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
▶️ Usage

Start the EDR engine:

python3 main.py


The GUI and agent will run from a single command.

🧪 Testing Examples

Generate high CPU activity:

yes > /dev/null


Spawn a long-running process:

sleep 1000


The EDR should detect and respond accordingly.

🔐 Security Design Notes

Implements self-protection to prevent killing its own process

Handles race conditions gracefully (process exits before response)

Uses safe process termination logic

Thread-safe design for agent and GUI interaction

📊 Logging

All detections and responses are logged in:

logs/edr.log


Logs are structured for future SIEM or alerting integration.

🚧 Future Enhancements

Machine Learning–based detection

Threat Intelligence integration

Process tree visualization

Systemd service support

Alert severity levels

JSON / API output

SOAR integration

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

j0h4ck
Blue Team • Malware Analysis • Defensive Security

Contributions, forks, and improvements are welcome.


---

## 🏆 Why this README is strong
✔ Enterprise tone  
✔ Clear security focus  
✔ Recruiter-friendly  
✔ GitHub-ready  
✔ Blue Team professional style  

---

If you want, I can also:
- ✨ Add GitHub badges (Python, Linux, MIT)
- ✨ Customize it for **SOC / Blue Team CV**
- ✨ Make an **Arabic + English version**
- ✨ Write a killer GitHub repo description

Just tell me 👍
