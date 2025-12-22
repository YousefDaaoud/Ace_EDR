from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QListWidget, QPushButton, QCheckBox,
    QMessageBox, QTabWidget
)
from PyQt5.QtCore import QTimer, Qt
import sys
import os
import json

from gui.log_reader import read_alerts
from core.responder import Responder


# ================= THEME =================
DARK_STYLE = """
QWidget {
    background-color: #0b0f14;
    color: #e5e7eb;
    font-family: Segoe UI;
    font-size: 13px;
}

QTabWidget::pane {
    border: 1px solid #1f2937;
}

QTabBar::tab {
    background: #111827;
    padding: 10px;
    border: 1px solid #1f2937;
}

QTabBar::tab:selected {
    background: #1f2937;
    color: #ef4444;
}

QPushButton {
    background-color: #111827;
    border: 1px solid #1f2937;
    padding: 8px;
}

QPushButton:hover {
    background-color: #1f2937;
}

QListWidget {
    background-color: #020617;
    border: 1px solid #1f2937;
}

QCheckBox {
    padding: 5px;
}
"""


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, "config", "settings.json")


class EDRDashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🛡 Ace EDR ")
        self.resize(1000, 550)
        self.setStyleSheet(DARK_STYLE)

        self.responder = Responder()

        # ===== Tabs =====
        self.tabs = QTabWidget()
        self.alerts_tab = QWidget()
        self.settings_tab = QWidget()

        self.tabs.addTab(self.alerts_tab, "⚠ Alerts")
        self.tabs.addTab(self.settings_tab, "⚙ Settings")

        self.build_alerts_tab()
        self.build_settings_tab()

        layout = QVBoxLayout(self)
        layout.addWidget(self.tabs)

        # ===== Timer =====
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_alerts)
        self.timer.start(3000)

        self.update_alerts()

    # ================= ALERTS TAB =================

    def build_alerts_tab(self):
        layout = QVBoxLayout(self.alerts_tab)

        title = QLabel("Detected Threats")
        title.setStyleSheet("font-size:20px; color:#ef4444;")
        layout.addWidget(title)

        self.alert_list = QListWidget()
        layout.addWidget(self.alert_list)

        btn_layout = QHBoxLayout()

        self.kill_btn = QPushButton("❌ Kill Selected PID")
        self.kill_btn.setStyleSheet("color:#ef4444;")
        self.kill_btn.clicked.connect(self.kill_selected)

        btn_layout.addWidget(self.kill_btn)
        btn_layout.addStretch()

        layout.addLayout(btn_layout)

    def update_alerts(self):
        self.alert_list.clear()

        alerts = read_alerts()
        for alert in alerts:
            item = (
                f"[ PID {alert['pid']} ]   "
                f"{alert['name']}   "
                f"CPU: {alert['cpu']}%"
            )
            self.alert_list.addItem(item)

    def kill_selected(self):
        item = self.alert_list.currentItem()
        if not item:
            return

        pid = int(item.text().split()[2])
        success = self.responder.kill_pid(pid)

        if success:
            QMessageBox.information(self, "Killed", f"PID {pid} terminated")
        else:
            QMessageBox.warning(self, "Blocked", "Kill blocked (MONITOR_ONLY)")

    # ================= SETTINGS TAB =================

    def build_settings_tab(self):
        layout = QVBoxLayout(self.settings_tab)

        title = QLabel("EDR Configuration")
        title.setStyleSheet("font-size:20px; color:#38bdf8;")
        layout.addWidget(title)

        self.kill_checkbox = QCheckBox("Enable Active Response (Kill Mode)")
        self.kill_checkbox.setChecked(self.load_settings().get("kill_mode", False))
        layout.addWidget(self.kill_checkbox)

        save_btn = QPushButton("💾 Save Settings")
        save_btn.clicked.connect(self.save_settings)
        layout.addWidget(save_btn)

        layout.addStretch()

    def load_settings(self):
        if not os.path.exists(CONFIG_FILE):
            return {"kill_mode": False}
        with open(CONFIG_FILE) as f:
            return json.load(f)

    def save_settings(self):
        with open(CONFIG_FILE, "w") as f:
            json.dump(
                {"kill_mode": self.kill_checkbox.isChecked()},
                f,
                indent=4
            )

        QMessageBox.information(self, "Saved", "Settings updated successfully")


# ===== Standalone Run =====
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = EDRDashboard()
    win.show()
    sys.exit(app.exec_())
