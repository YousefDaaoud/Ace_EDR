import threading
from services.file_service import start_file_monitor

class Monitor:
    def __init__(self, path="/tmp"):
        self.path = path

    def start(self):
        t = threading.Thread(target=start_file_monitor, args=(self.path,))
        t.daemon = True
        t.start()
