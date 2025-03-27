# VitalGuard SimHealth: AI-Powered Health Simulation System

Description,"A simulated health monitoring system for athletes and patients. Generates fake sensor data (steps, heart rate, oxygen, temperature) to train AI models that predict health states. No real phones/sensors used!"
Key Features,"
- 🏃♂️ Athlete Mode: Simulates active users (gym/running data)
- 🏥 Patient Mode: Simulates ill users (low mobility, health risks)
- 📊 Real-Time Alerts
- 📝 Automated Health Reports
"

Setup,"1. Install Python 3.8+
2. Install libraries: 
   pip install numpy pandas tensorflow scikit-learn
3. Folder Structure:
   - /sportsman (athlete codes)
   - /sick (patient codes)"

How to Run (Athlete),"
1. Generate Athlete Data:
   python sportsman/data_generator_sport.py
2. Train Athlete AI:
   python sportsman/model_sport.py
3. Start Monitoring:
   python sportsman/real_time_predictor_sport.py"

How to Run (Patient),"
1. Generate Patient Data:
   python sick/data_generator_sick.py
2. Train Patient AI:
   python sick/model_sick.py
3. Start Monitoring:
   python sick/real_time_predictor_sick.py"

Code Differences,"
Feature,Athlete Code,Patient Code
Data Ranges,Steps: 50-200, Steps: 0-30
Heart Rate,45-70 bpm,40-130 bpm
Oxygen,95-100%,85-93%
Temperature,36-37.5°C,37.5-39°C
Alerts,Overtraining,Medical Emergencies
Reports,Performance Tips,Urgent Actions"

Output Examples,"
Athlete Output:
✅ Normal Activity | Steps: 120 | HR: 68
⚠️ Low Confidence Score (38.2)

Patient Output:
🔴 CRITICAL: Oxygen 89% | HR: 125
🚨 Notify Doctor Immediately"

Technical Terms,"
LSTM,AI that learns patterns over time (like memory)
MAE (Score),How 'weird' the system thinks the data is (lower = normal)
Thresholds,Safety limits (e.g., HR > 100 = bad for patients)"

FAQ,"
Q: Is this using real phone data?
A: ❌ No! All data is fake/simulated.

Q: Why two models?
A: Athletes and patients have different 'normal' ranges.

Q: What does 'Low Confidence' mean?
A: The AI is unsure – might need more data or check manually."
