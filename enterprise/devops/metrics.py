import psutil
import os

def get_system_metrics():
    return {
        'cpu_usage': psutil.cpu_percent(),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'load_avg': os.getloadavg() if hasattr(os, 'getloadavg') else (0, 0, 0)
    }
