import os
import csv
import time
import random
from datetime import datetime

os.makedirs('sick', exist_ok=True)

with open('sickman/sick/sick_data.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(["timestamp", "steps", "heart_rate", "oxygen", "body_temp"])
    
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Simulating patient with potential issues
        steps = random.choices([0, 5, 10, 15], weights=[30, 40, 20, 10])[0]
        hr = random.choices(
            [random.randint(40, 50), random.randint(70, 90), random.randint(110, 130)], 
            weights=[10, 60, 30]
        )[0]
        oxygen = max(82, min(95, random.normalvariate(91, 3)))
        temp = round(random.normalvariate(37.8, 0.5), 1)
        
        writer.writerow([timestamp, steps, hr, oxygen, temp])
        f.flush()
        time.sleep(5)
        