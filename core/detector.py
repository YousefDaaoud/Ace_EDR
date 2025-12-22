from detection.heuristics import HeuristicEngine
from core.logger import log_info
import os


class Detector:
    def __init__(self):
        self.engine = HeuristicEngine()
        self.self_pid = os.getpid()  # 🔒

    def is_malicious(self, process: dict) -> bool:
        # ❌ Ignore EDR process
        if process.get("pid") == self.self_pid:
            return False

        if self.engine.analyze(process):
            log_info(f"Heuristic alert: {process}")
            return True

        return False

    def suspicious_connection(self, conn: dict) -> bool:
        raddr = conn.get("raddr")
        if not raddr:
            return False

        try:
            ip, port = raddr.split(":")
            if port in {"4444", "1337", "5555"}:
                log_info(f"Suspicious C2 connection: {conn}")
                return True
        except Exception:
            pass

        return False
