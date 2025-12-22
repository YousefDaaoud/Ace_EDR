class HeuristicEngine:
    def analyze(self, process: dict) -> bool:
        name = process.get("name", "").lower()
        cpu = process.get("cpu", 0)

        # 🔒 Whitelist (Self-Protection)
        whitelist = {
            "python",
            "python3",
            "systemd",
            "gnome-shell",
            "Xorg"
        }

        if name in whitelist:
            return False

        # CPU abuse
        if cpu > 85:
            return True

        # Suspicious names
        suspicious = {
            "nc", "netcat", "ncat",
            "bash", "sh", "zsh",
            "perl", "ruby"
        }

        if name in suspicious:
            return True

        return False
