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

Running the Code (Athlete),"
1. Open 3 terminals:
Terminal 1: python sportsman/data_generator_sport.py
Terminal 2: python sportsman/model_sport.py
Terminal 3: python sportsman/real_time_predictor_sport.py
2. Keep Terminals 1 & 3 running forever"

Running the Code (Patient),"
1. Open 3 terminals:
Terminal 1: python sick/data_generator_sick.py
Terminal 2: python sick/model_sick.py
Terminal 3: python sick/real_time_predictor_sick.py
2. Keep Terminals 1 & 3 running forever"

Athlete Output Example :

=== ATHLETE REPORT ===
✅ Normal Activity
Steps: 150 | HR: 68 
⚠️ Alert: Low Confidence (Check Rest)"

Patient Output Example : 

=== PATIENT ALERT ===
🔴 Critical: Oxygen 89%
HR: 128 | Temp: 38.6°C
🚑 Action: Call Doctor Now"

FAQ,"Q: Real phone data used?
A: ❌ No! All data is fake/simulated.
Q: Why two models?
A: Athletes/patients have different 'normal' ranges."
