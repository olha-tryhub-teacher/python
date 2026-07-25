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
