from services.process_service import get_processes
from core.detector import Detector
from core.responder import Responder
from core.logger import log_info
import time
import os


class EDRAgent:
    def __init__(self):
        self.detector = Detector()
        self.responder = Responder()
        self.known_pids = set()

        # 🔒 Self Protection
        self.self_pid = os.getpid()

    def start(self):
        log_info("EDR Agent Started Successfully")

        while True:
            processes = get_processes()
            current_pids = {p["pid"] for p in processes}
            new_pids = current_pids - self.known_pids

            for proc in processes:
                # ❌ Ignore self
                if proc["pid"] == self.self_pid:
                    continue

                if proc["pid"] in new_pids:
                    if self.detector.is_malicious(proc):
                        self.responder.respond(proc)

            self.known_pids = current_pids
            time.sleep(3)
