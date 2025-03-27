import os
import time
import numpy as np
import pandas as pd
import tensorflow as tf
from datetime import datetime

# Suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
tf.get_logger().setLevel('ERROR')

# Load model
model = tf.keras.models.load_model('sickman/sick/sick_model.keras')

def print_realtime_vitals(data):
    """Print formatted current vitals"""
    print(f"\n{'='*40}")
    print(f"📊 REAL-TIME VITALS [{datetime.now().strftime('%H:%M:%S')}]")
    print(f"• Steps: {data[-1][0]:.0f} (Last hour)")
    print(f"• Heart Rate: {data[-1][1]:.0f} bpm [{'✅ Normal' if 60 <= data[-1][1] <= 100 else '⚠️ Warning'}]")
    print(f"• SpO2: {data[-1][2]:.0f}% [{'🟢 Safe' if data[-1][2] >= 92 else '🟡 Caution' if data[-1][2] >= 88 else '🔴 Danger'}]")
    print(f"• Temperature: {data[-1][3]:.1f}°C [{'😐 Normal' if data[-1][3] <= 37.5 else '🤒 Fever'}]")
    print(f"{'='*40}")

def generate_medical_report(data, mae):
    """Generate detailed medical report"""
    latest = data[-1]
    return f"""
============================================
       MEDICAL ALERT REPORT
       {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
============================================

CRITICAL METRICS:
1. Mobility: {latest[0]:.0f} steps (Last hour)
   - Status: {'Bedridden' if latest[0] < 5 else 'Limited' if latest[0] < 15 else 'Mobile'}

2. Cardiovascular:
   - Heart Rate: {latest[1]:.0f} bpm ({'Normal' if 60 <= latest[1] <= 100 else 'Bradycardia' if latest[1] < 60 else 'Tachycardia'})
   - Stability Index: {100 - min(100, mae*1.5):.0f}/100

3. Respiratory:
   - Oxygen Saturation: {latest[2]:.0f}% ({'Normal' if latest[2] >= 92 else 'Concerning' if latest[2] >= 88 else 'Critical'})
   - Trend: {'↑ Improving' if data[-1][2] > data[-3][2] else '↓ Worsening' if data[-1][2] < data[-3][2] else '↔ Stable'}

4. Thermal Regulation:
   - Core Temp: {latest[3]:.1f}°C ({'Normal' if latest[3] <= 37.5 else 'Low-grade fever' if latest[3] <= 38.3 else 'High fever'})

ANOMALY DETECTION:
• System Confidence: {'High' if mae < 25 else 'Medium' if mae < 50 else 'Low'}
• Risk Score: {min(100, mae*2):.1f}%

RECOMMENDED ACTIONS:
{'• Continue monitoring' if mae < 30 else 
 '• Notify healthcare provider' if mae < 60 else 
 '• EMERGENCY INTERVENTION NEEDED'}
{'• Check oxygen supply' if latest[2] < 92 else ''}
{'• Administer antipyretics' if latest[3] > 38.0 else ''}

============================================
"""

# Main monitoring loop
window = []
report_interval = 600  # 10 minutes in seconds
last_report = time.time()

while True:
    try:
        # Read latest data
        df = pd.read_csv('sickman/sick/sick_data.csv')
        latest = df.iloc[-1][['steps','heart_rate','oxygen','body_temp']].values.astype(float)
        window.append(latest)
        
        if len(window) >= 10:
            input_data = np.array(window[-10:]).reshape(1, 10, 4)
            
            # 1. Print real-time vitals
            print_realtime_vitals(input_data[0])
            
            # 2. Make prediction
            pred = model.predict(input_data, verbose=0)
            mae = np.mean(np.abs(pred - input_data))
            print(f"🔍 Anomaly Score: {mae:.2f} ({'Normal' if mae < 25 else 'Warning' if mae < 50 else 'Critical'})")
            
            # 3. Generate and save report every 15 minutes
            if time.time() - last_report > report_interval:
                report = generate_medical_report(input_data[0], mae)
                with open('sickman/sick/medical_report.txt', 'a', newline='', encoding='utf-8') as f:
                    f.write(report)
                print(report)  # Print full report to console
                last_report = time.time()
            
            window = []  # Reset window after prediction
    
    except Exception as e:
        print(f"⚠️ Monitoring Error: {str(e)}")
    
    time.sleep(5)  # Sync with data generator