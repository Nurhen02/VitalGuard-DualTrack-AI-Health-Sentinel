import numpy as np
import os
# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # 0 = all messages, 3 = no messages
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disable oneDNN warnings
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, LSTM, RepeatVector, Dense, TimeDistributed

# Sport health rules
SPORT_THRESHOLDS = {
    'min_heart_rate': 45,
    'max_heart_rate': 180,
    'min_oxygen': 94,
    'max_temp': 37.5
}

def build_model():
    model = Sequential([
        Input(shape=(10, 4)),  # Input: 10 timesteps, 4 features
        LSTM(64, return_sequences=False),  # Output: (batch_size, 64)
        RepeatVector(10),  # Repeat 10 times: (batch_size, 10, 64)
        LSTM(64, return_sequences=True),  # Output: (batch_size, 10, 64)
        TimeDistributed(Dense(4))  # Output: (batch_size, 10, 4) to match input
    ])
    model.compile(loss='mae', optimizer='adam')
    return model

# Generate training data (1000 samples, 10 timesteps, 4 features)
X_train = np.random.randn(1000, 10, 4) * [20, 5, 1, 0.2] + [100, 60, 97, 36.6]

# Train
model = build_model()
model.fit(X_train, X_train, epochs=15, batch_size=32)
model.save('healthyman/sportsman/sport_model.keras')