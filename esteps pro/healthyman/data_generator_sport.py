import os
import csv
import time
import random
from datetime import datetime

os.makedirs('sportsman', exist_ok=True)

with open('healthyman/sportsman/sport_data.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(["timestamp", "steps", "heart_rate", "oxygen", "body_temp"])
    
    while True:
        # Healthy ranges for athletes
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        steps = random.randint(80, 150)  # High activity
        heart_rate = random.randint(50, 70)  # Low resting HR
        oxygen = random.randint(95, 100)  # Normal SpO2
        body_temp = round(random.uniform(36.0, 37.2), 1)  # Normal temp
        
        writer.writerow([timestamp, steps, heart_rate, oxygen, body_temp])
        f.flush()
        time.sleep(5)