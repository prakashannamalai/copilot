import os
import time

def get_uptime():
    # Read uptime from /proc/uptime
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
    uptime = time.strftime('%H:%M:%S', time.gmtime(uptime_seconds))
    return uptime

if __name__ == '__main__':
    print(f'System Uptime: {get_uptime()}')