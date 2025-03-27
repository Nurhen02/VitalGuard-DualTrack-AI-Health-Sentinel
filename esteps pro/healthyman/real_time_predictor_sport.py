import os
import time
import numpy as np
import pandas as pd
import tensorflow as tf
from datetime import datetime

# Suppress warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0=all, 3=none
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN warnings
tf.get_logger().setLevel('ERROR')

# Load model and thresholds
model = tf.keras.models.load_model('healthyman/sportsman/sport_model.keras')
SPORT_THRESHOLDS = {
    'steps_low': 50,
    'steps_high': 200,
    'hr_resting': (45, 70),
    'hr_active': (80, 180),
    'oxygen': (94, 100),
    'temp': (36.0, 37.5)
}

def generate_health_report(data, mae):
    """Generate detailed PDF-style health report"""
    latest = data[-1]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Health analysis logic
    analysis = []
    if latest[0] < SPORT_THRESHOLDS['steps_low']:
        analysis.append("⚠️ Low activity detected: Consider light exercise to maintain mobility.")
    elif latest[0] > SPORT_THRESHOLDS['steps_high']:
        analysis.append("🏋️ High activity: Ensure proper hydration and recovery.")
    
    if not SPORT_THRESHOLDS['hr_resting'][0] <= latest[1] <= SPORT_THRESHOLDS['hr_resting'][1]:
        analysis.append(f"❤️‍🩹 Abnormal heart rate ({latest[1]} bpm): Recommended to check stress levels.")
    
    if latest[2] < SPORT_THRESHOLDS['oxygen'][0]:
        analysis.append(f"🫁 Mild hypoxia detected ({latest[2]}% SpO2): Consider deep breathing exercises.")
    
    if latest[3] > SPORT_THRESHOLDS['temp'][1]:
        analysis.append(f"🤒 Elevated temperature ({latest[3]}°C): Monitor for signs of illness.")
    
    # Format report
    report = f"""
============================================
          ATHLETE HEALTH REPORT
          {timestamp}
============================================

VITAL SIGNS:
• Steps: {latest[0]} (Normal range: {SPORT_THRESHOLDS['steps_low']}-{SPORT_THRESHOLDS['steps_high']})
• Heart Rate: {latest[1]} bpm (Resting norm: {SPORT_THRESHOLDS['hr_resting'][0]}-{SPORT_THRESHOLDS['hr_resting'][1]})
• Blood Oxygen: {latest[2]}% (Healthy: >{SPORT_THRESHOLDS['oxygen'][0]}%)
• Core Temp: {latest[3]}°C (Safe range: {SPORT_THRESHOLDS['temp'][0]}-{SPORT_THRESHOLDS['temp'][1]}°C)

MODEL ANALYSIS:
• Anomaly Detection Score: {mae:.2f} (Lower is better)
• System Confidence: {'High' if mae < 15 else 'Medium' if mae < 30 else 'Low'}

RECOMMENDATIONS:
{'\n'.join(analysis) if analysis else "✅ All metrics within normal ranges. Maintain current routine."}

============================================
"""
    return report

# Main loop
window = []
report_interval = 600  # 10 minutes
last_report = time.time()

while True:
    try:
        df = pd.read_csv('healthyman/sportsman/sport_data.csv')
        latest = df.iloc[-1][['steps','heart_rate','oxygen','body_temp']].values.astype(float)
        window.append(latest)
        
        if len(window) >= 10:
            input_data = np.array(window[-10:]).reshape(1, 10, 4)
            pred = model.predict(input_data, verbose=0)
            mae = np.mean(np.abs(pred - input_data))
            
            # Print real-time update
            print(f"\n🔄 Latest Reading: {latest[0]} steps | {latest[1]} bpm | {latest[2]}% SpO2 | {latest[3]}°C")
            print(f"📊 System MAE: {mae:.2f}")
            
            # Generate and save report
            if time.time() - last_report > report_interval:
                report = generate_health_report(input_data[0], mae)
                with open('healthyman/sportsman/health_report.txt', 'a', encoding='utf-8') as f:
                 f.write(report)
                print(report)  # Also print to console
                last_report = time.time()
            
            window = []
    
    except Exception as e:
        print(f"⚠️ Data error: {str(e)}")
    
    time.sleep(5)