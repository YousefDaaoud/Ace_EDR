# detection/rules.py

SUSPICIOUS_NAMES = [
    "nc",
    "netcat",
    "meterpreter",
    "malware"
]

SUSPICIOUS_PORTS = [
    4444,
    1337,
    6666,
    9001
]

WHITELIST_PROCESSES = [
    "bash",
    "python",
    "python3"
]
