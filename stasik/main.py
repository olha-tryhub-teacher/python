import pandas as pd

# Завантаження даних
df_llm = pd.read_csv('LLM__data.csv')

# 1. Час написання
df_llm['created'] = pd.to_datetime(df_llm['time'])
df_llm['hour'] = df_llm['created'].dt.hour

# 2. Кількість слів у відповіді
df_llm['response_word_count'] = df_llm['response'].apply(lambda x: len(str(x).split()))

# 3. Частота запитів по мовах
language_counts = df_llm['from_language'].value_counts()

# 4. Кількість символів у текстах (з перевіркою на NaN)
df_llm['text_length'] = df_llm['text'].apply(lambda x: len(x) if isinstance(x, str) else 0)

# 5. Середня кількість символів відповідно до мови
average_text_length_by_language = df_llm.groupby('from_language')['text_length'].mean().sort_values(ascending=False)

# Вивід результатів
print("Час написання (години):\n", df_llm['hour'].value_counts())
print("Кількість слів у відповіді:\n", df_llm[['response', 'response_word_count']])
print("Частота запитів по мовах:\n", language_counts)
print("Середня кількість символів у текстах за мовами (від найбільшого до найменшого):\n", average_text_length_by_language)



# Завантаження даних
# Завантаження даних
df_reviews = pd.read_csv('chatgpt_reviews.csv')

# 1. Середній рейтинг
average_score = df_reviews['score'].mean()

# 2. Топ-5 позитивних відгуків
top_positive_reviews = df_reviews.nlargest(5, 'thumbsUpCount')

# 3. Кількість символів у відгуках
df_reviews['content_length'] = df_reviews['content'].apply(lambda x: len(x) if isinstance(x, str) else 0)

# 4. Наявність позитивних слів у відгуках
positive_words = [
    'great', 'awesome', 'fantastic', 'wonderful', 'excellent',
    'amazing', 'superb', 'delightful', 'impressive', 'outstanding',
    'incredible', 'marvelous', 'fabulous', 'remarkable', 'exceptional',
    'brilliant', 'magnificent', 'inspiring', 'encouraging', 'uplifting',
    'joyful', 'pleasurable', 'satisfying', 'valuable', 'beneficial',
    'helpful', 'supportive', 'lovely', 'charming', 'endearing',
    'engaging', 'captivating', 'radiant', 'refreshing', 'cheerful',
    'bright', 'positive', 'motivating', 'enlightening', 'hopeful',
    'peaceful', 'tranquil', 'serene', 'harmonious', 'thoughtful',
    'kind', 'generous', 'compassionate', 'friendly', 'approachable',
    'respectful', 'gracious', 'polite', 'courteous', 'tolerant',
    'empathetic', 'sympathetic', 'forgiving', 'understanding', 'welcoming',
    'exciting', 'fun', 'entertaining', 'playful', 'adventurous',
    'passionate', 'determined', 'dedicated', 'committed', 'resilient',
    'tenacious', 'hardworking', 'persistent', 'creative', 'innovative',
    'original', 'resourceful', 'skillful', 'talented', 'gifted',
    'knowledgeable', 'wise', 'insightful', 'thought-provoking', 'intelligent',
    'astute', 'shrewd', 'clever', 'smart', 'brave', 'courageous',
    'fearless', 'confident', 'self-assured', 'authentic', 'genuine',
    'sincere', 'trustworthy', 'reliable', 'dependable', 'loyal',
    'faithful', 'humble', 'modest', 'true', 'noble', 'virtuous',
    'righteous', 'moral', 'ethical', 'principled', 'honorable',
    'glorious', 'triumphant', 'victorious', 'successful', 'prosperous'
]
df_reviews['contains_positive'] = df_reviews['content'].apply(lambda x: any(word in str(x).lower() for word in positive_words))
# 5. Підрахунок позитивних відгуків відповідно до категорії (наприклад, за рейтингом)
positive_reviews_count = df_reviews[df_reviews['contains_positive']].groupby('score').size()

# Вивід результатів
print("Середній рейтинг:\n", average_score)
print("\nТоп-5 позитивних відгуків:\n", top_positive_reviews[['userName', 'content', 'score']])
print("\nКількість символів у відгуках:\n", df_reviews[['content', 'content_length']])
print("\nКількість позитивних відгуків за рейтингом:\n", positive_reviews_count)