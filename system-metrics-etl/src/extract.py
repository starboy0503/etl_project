import psutil
from datetime import datetime

def extract_metrics():
    "Extract system performance metrics"

    metrics={
        "timestamp":datetime.now().isoformat(),
        "cpu_usage":psutil.cpu_percent(interval=1),
        "memory_usage":psutil.virtual_memory().percent,
        "disk_usage":psutil.disk_usage("/").percent,
        "net_sent":psutil.net_io_counters().bytes_sent/(1024*1024),
        "net_recv":psutil.net_io_counters().bytes_recv/(1024*1024)
    }
    return metrics