blacklisted_ips = set()

def block_ip(ip):
    """Block a suspicious IP"""
    blacklisted_ips.add(ip)
    print(f"Blocked IP: {ip}")
