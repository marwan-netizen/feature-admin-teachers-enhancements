import psutil
import os

def get_system_metrics():
    return {
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_usage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent,
        'load_avg': os.getloadavg() if hasattr(os, 'getloadavg') else (0, 0, 0),
        'net_io': psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv,
        'process_count': len(psutil.pids())
    }

class SystemHealthService:
    @staticmethod
    def get_full_report():
        return {
            'metrics': get_system_metrics(),
            'status': 'Healthy' if psutil.cpu_percent() < 80 else 'Stressed',
            'timestamp': psutil.boot_time()
        }
