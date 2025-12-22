from core.agent import EDRAgent
from gui.dashboard import EDRDashboard
from PyQt5.QtWidgets import QApplication
import sys
import threading

print("[*] Starting Mini EDR...")

agent = EDRAgent()
threading.Thread(target=agent.start, daemon=True).start()

app = QApplication(sys.argv)
gui = EDRDashboard()
gui.show()
sys.exit(app.exec_())
