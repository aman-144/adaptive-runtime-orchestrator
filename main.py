import psutil
import time

while True: 
  cpu_usage = psutil.cpu_percent()
  print(f"cpu usage:{cpu_usage}% ")
  time.sleep(1)
