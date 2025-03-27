# VitalGuard SimHealth: AI-Powered Health Simulation System

# Main Idea of the Project:
This project uses generative AI to simulate and predict health patterns for two groups: athletes and patients. Instead of real sensor data, we create fake (but realistic) step counts, heart rates, oxygen levels, and body temperatures. The AI learns what "normal" looks like for each group and flags unusual patterns.

# Why Generative AI?
Generative AI is used to:

1. Simulate realistic health data (since we don’t have real phone sensors).

2. Predict future health states by learning patterns from past data.

3. Spot hidden risks (like sudden fatigue in athletes or oxygen drops in patients) that simple rules might miss.

How It Works:

*For athletes, the AI learns healthy training patterns to suggest recovery times.

*For patients, it detects early warning signs (like rising heart rates) to alert caregivers.

The AI compares live data to its "memory" of normal patterns and calculates a risk score (MAE). Low score = safe, high score = problem!

In short: Generative AI acts like a virtual doctor that learns your unique health rhythm and warns you before issues escalate. 🩺🤖

# Running the Code

🏃♂️ For Athletes:

Open 3 separate terminal windows:

1. Terminal 1: Generate simulated athlete data 

python sportsman/data_generator_sport.py  

2. Terminal 2: Train the AI model 

python sportsman/model_sport.py

3. Terminal 3: Start real-time monitoring 

python sportsman/real_time_predictor_sport.py

Keep running:

Never close Terminal 1 (data generation)

Never close Terminal 3 (live monitoring)

🏥 For Patients:

Open 3 separate terminal windows:

1. Terminal 1: Generate simulated patient data 

python sick/data_generator_sick.py  

2. Terminal 2: Train the AI model 

python sick/model_sick.py

3. Terminal 3: Start real-time monitoring 

python sick/real_time_predictor_sick.py

Keep running:

Never close Terminal 1 (data generation)

Never close Terminal 3 (live monitoring)

Example Outputs

🏅 Athlete Report:

=== ATHLETE HEALTH REPORT ===  

✅ Status: Normal Activity  

📊 Metrics:  
- Steps: 150  
- Heart Rate: 68 bpm
   
⚠️ Alert: Low Confidence Score Detected (Check Rest)

🚑 Patient Alert:

=== PATIENT CRITICAL ALERT === 

🔴 Status: High Risk  

📊 Metrics:  
- Oxygen: 89%  
- Heart Rate: 128 bpm  
- Temperature: 38.6°C
  
🆘 Action: Contact Healthcare Provider Immediately

# FAQ
Q: Does this use real phone sensor data?

❌ No! All data is simulated for testing.

Q: Why are there two separate models?

✅ Athletes and patients have fundamentally different "normal" health patterns. Separate models ensure accurate alerts for each group.

Q: How do I stop the system?

Press Ctrl + C in Terminals 1 & 3 to terminate the process.
