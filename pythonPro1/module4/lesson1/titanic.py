import pandas as pd # Імпортуємо бібліотеку Pandas для роботи з даними
from sklearn.model_selection import train_test_split  # Імпортуємо функцію для розділення даних на тренувальну і тестову вибірки
from sklearn.preprocessing import StandardScaler  # Імпортуємо StandardScaler для нормалізації даних
from sklearn.neighbors import KNeighborsClassifier  # Імпортуємо K-Nearest Neighbors Classifier
from sklearn.metrics import confusion_matrix, accuracy_score  # Імпортуємо метрики оцінки моделі

# pip install scikit-learn
# pip install pandas

# Крок 1. Завантаження та очищення даних
# Крок 2. Створення моделі
