import psutil
import time


while True:
  cpu_usage = psutil.cpu_percent()
  ram_usage = psutil.virtual_memory().percent
  disk_usage = psutil.disk_usage('/').percent
  total_ram = psutil.virtual_memory().total
  used_ram = psutil.virtual_memory().used
  free_ram = psutil.virtual_memory().free
  print(f"cpu usage:{cpu_usage}% , ram usage:{ram_usage}% , disk usage:{disk_usage}% ")
  print(f"total ram:{total_ram} , used ram:{used_ram} , free ram:{free_ram}")
 
  time.sleep(1)
