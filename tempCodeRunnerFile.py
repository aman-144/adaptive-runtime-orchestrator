import psutil
import time

while True: 
  cpu_usage = psutil.cpu_percent()
  ram_usage = psutil.virtual_memory().percent
  print(f"cpu usage:{cpu_usage}% ; ram usage:{ram_usage}% ")
  time.sleep(1)