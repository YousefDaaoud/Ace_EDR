import os
import signal
from core.logger import log_info, log_warning

MONITOR_ONLY = True


class Responder:
    def __init__(self):
        pass

    def respond(self, process: dict):
        """
        Main response handler
        """
        pid = process.get("pid")
        name = process.get("name")

        if not pid:
            return

        if MONITOR_ONLY:
            log_warning("Kill blocked (MONITOR_ONLY).")
            return

        self.kill_pid(pid, name)

    def kill_pid(self, pid: int, name: str = "") -> bool:
        """
        Kill a process safely
        """
        try:
            os.kill(pid, signal.SIGKILL)
            log_info(f"Process killed successfully: {name} (PID {pid})")
            return True

        except ProcessLookupError:
            # ✅ الحالة الطبيعية (Race Condition)
            log_info(f"Process already terminated: PID {pid}")
            return False

        except PermissionError:
            log_warning(f"Permission denied while killing PID {pid}")
            return False

        except Exception as e:
            log_warning(f"Failed to kill PID {pid}: {e}")
            return False
