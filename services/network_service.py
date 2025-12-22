import psutil

def get_network_connections():
    connections = []
    for conn in psutil.net_connections(kind='inet'):
        if conn.raddr:
            connections.append({
                "pid": conn.pid,
                "laddr": f"{conn.laddr.ip}:{conn.laddr.port}",
                "raddr": f"{conn.raddr.ip}:{conn.raddr.port}",
                "status": conn.status
            })
    return connections
