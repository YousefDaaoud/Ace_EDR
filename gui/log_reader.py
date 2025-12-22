# gui/log_reader.py

import os
import ast

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE = os.path.join(BASE_DIR, "logs", "alerts.log")


def read_alerts():
    alerts = []

    if not os.path.exists(LOG_FILE):
        return alerts

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "Heuristic alert:" in line:
                try:
                    time_part = line.split(" - ")[0]
                    data_part = line.split("Heuristic alert:")[1].strip()
                    data = ast.literal_eval(data_part)

                    alerts.append({
                        "time": time_part,
                        "pid": data.get("pid"),
                        "name": data.get("name"),
                        "cpu": data.get("cpu"),
                    })
                except Exception:
                    continue

    return alerts[-50:]
