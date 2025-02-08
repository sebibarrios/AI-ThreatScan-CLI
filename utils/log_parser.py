def parse_logs(log_file):
    """Parse network logs for potential threats"""
    with open(log_file, "r") as f:
        logs = f.readlines()
    return logs
