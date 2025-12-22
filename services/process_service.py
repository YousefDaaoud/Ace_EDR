# services/process_service.py

import psutil
from utils.config import IGNORE_PROCESS_PREFIXES, MIN_CPU_TO_LOG

# Initialize CPU counters (IMPORTANT)
for p in psutil.process_iter():
    try:
        p.cpu_percent(None)
    except Exception:
        pass


def get_processes():
    processes = []

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.name()

            if name.startswith(IGNORE_PROCESS_PREFIXES):
                continue

            cpu = proc.cpu_percent(None)

            if cpu < MIN_CPU_TO_LOG:
                continue

            processes.append({
                "pid": proc.pid,
                "name": name,
                "cpu": cpu
            })

        except Exception:
            continue

    return processes
