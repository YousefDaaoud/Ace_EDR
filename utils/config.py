# utils/config.py

# Processes that generate noise (kernel / system)
IGNORE_PROCESS_PREFIXES = (
    "kworker",
    "rcu",
    "migration",
    "irq",
    "idle",
    "watchdog"
)

# Minimum CPU usage to consider process
MIN_CPU_TO_LOG = 1.0

# Heuristic settings
CPU_THRESHOLD = 70
CPU_SAMPLES_REQUIRED = 3

# Network rules
SUSPICIOUS_PORTS = [
    4444,
    1337,
    6666,
    9001
]

# Process rules
SUSPICIOUS_NAMES = [
    "nc",
    "netcat",
    "meterpreter",
    "malware"
]

WHITELIST_PROCESSES = [
    "bash",
    "python",
    "python3"
]

# Response mode
MONITOR_ONLY = True
