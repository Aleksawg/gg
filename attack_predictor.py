import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np

class AttackPredictor:
    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        # Загрузим или обучим модель
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')  # Для бинарной классификации
        ])
        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        return model

    def predict(self, data):
        # Делаем предсказание на основе данных
        data = np.array(data)
        return self.model.predict(data)
