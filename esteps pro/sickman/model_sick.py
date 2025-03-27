import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Input
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

def generate_patient_data(samples=1000):
    # Simulates patient with intermittent issues
    crisis_points = np.random.choice([0,1], size=samples, p=[0.85, 0.15])
    data = np.stack([
        np.where(crisis_points, 0, np.random.randint(0, 20, samples)),  # Steps
        np.where(crisis_points, 
                np.random.randint(110, 140, samples),
                np.random.randint(60, 100, samples)),  # HR
        np.clip(np.where(crisis_points,
                      np.random.normal(85, 3, samples),
                      np.random.normal(93, 2, samples)), 85, 100),  # SpO2
        np.where(crisis_points,
               np.random.normal(38.5, 0.5, samples),
               np.random.normal(37.2, 0.3, samples))  # Temp
    ], axis=-1)
    return data.reshape(samples, 1, 4).repeat(10, axis=1)

# Generate both input and target data
X_train = generate_patient_data()
y_train = X_train.copy()  # Autoencoder target is same as input

model = Sequential([
    Input(shape=(10, 4)),
    LSTM(64, return_sequences=True),
    Dense(4)  # Output matches input dimensions
])
model.compile(loss='mae', optimizer='adam')

# Train with both input and target data
model.fit(X_train, y_train, epochs=15, batch_size=32)
model.save('sickman/sick/sick_model.keras')