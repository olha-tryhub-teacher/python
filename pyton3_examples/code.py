import pandas as pd

df = pd.read_csv("googleplaystore.csv")

df.info()


print(df["Size"].value_counts())

# --- 2. Нормалізація поля Size ---
# Заміна 'Varies with device' на -1
df['Size'] = df['Size'].replace('Varies with device', '-1')
print(df["Size"].value_counts())

# --- Попереднє очищення ---
# Видалення рядка з помилковими даними (наприклад, де Price = 'Everyone' або Installs = 'Free'),
# оскільки це заважає подальшій конвертації типів.
df = df[df['Price'] != 'Everyone']


# --- 1. Нормалізація поля Rating ---
# Заміна NaN на середній рейтинг по колонці
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())




# Функція для конвертації розмірів
def convert_size(size_str):
    if str(size_str) == '-1':
        return -1.0
    # Якщо розмір в мегабайтах (M), просто прибираємо літеру
    if 'M' in str(size_str):
        return float(str(size_str).replace('M', ''))
    # Якщо розмір в кілобайтах (k), переводимо в мегабайти (ділимо на 1024)
    if 'k' in str(size_str):
        return float(str(size_str).replace('k', '')) / 1024
    # Для будь-яких інших числових значень
    return float(size_str)

# Застосування функції
df['Size'] = df['Size'].apply(convert_size)


# --- 3. Нормалізація поля Installs ---
# Видалення '+' та ',', перетворення на int
# Використовуємо regex=False для безпечної заміни спецсимволів
df['Installs'] = df['Installs'].str.replace('+', '', regex=False).str.replace(',', '', regex=False)
df['Installs'] = df['Installs'].astype(int)


# --- 4. Нормалізація поля Type ---
# Заміна пропусків на 'Free'
df['Type'] = df['Type'].fillna('Free')


# --- 5. Нормалізація поля Price ---
# Видалення '$', перетворення на float
df['Price'] = df['Price'].str.replace('$', '', regex=False)
df['Price'] = df['Price'].astype(float)


# Перевірка результату
print(df.info())
print(df.head())


# --- ЧАСТИНА 2: Базові діаграми ---
import matplotlib.pyplot as plt
import seaborn as sns


# Діаграма 1: Гістограма розподілу рейтингів
plt.figure(figsize=(10, 6))
sns.histplot(df['Rating'], bins=30, kde=True, color='pink')
plt.title('Розподіл рейтингів додатків')
plt.xlabel('Рейтинг')
plt.ylabel('Кількість')
plt.show()

# Діаграма 2: Топ-10 категорій (Стовпчикова діаграма)
plt.figure(figsize=(12, 6))
top_categories = df['Category'].value_counts().head(10)
sns.barplot(x=top_categories.values, y=top_categories.index, palette='viridis')
plt.title('Топ-10 категорій за кількістю додатків')
plt.xlabel('Кількість')
plt.show()

# Діаграма 3: Безкоштовні vs Платні (Кругова діаграма)
plt.figure(figsize=(7, 7))
type_counts = df['Type'].value_counts()
plt.pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999'])
plt.title('Співвідношення типів додатків')
plt.show()




