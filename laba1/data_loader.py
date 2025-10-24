## выгрузка датасета, подготовка и визуализация

import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    if df.shape[1] == 1:
        df = df[df.columns[0]].str.split(',', expand=True)

        # Из первой строки берём названия столбцов
        header = df.iloc[0]
        df = df[1:]
        df.columns = header

    # Преобразуем числовые колонки
    numeric_cols = ['Age', 'RestingBP', 'Cholesterol', 'Max HR', 'Oldpeak', 'Fasting BS', 'HeartDisease']

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Удаляем пустые строки
    df = df.dropna().reset_index(drop=True)

    return df


def infoo(df):
    print("Обща яинформация:")
    print(df.info())

    print("\n Описательняа статистика:")
    print(df.describe())


## процент заболеваний по полу
def analyze_disease_by_gender(df):
    stats = df.groupby('Sex')['HeartDisease']
    stats = stats.mean() * 100
    print("\n Процент пациентов с болезнью сердца по полу:")
    print(stats)
    return stats


## Частота типов боли в груди
def analyze_chest_pain(df):
    pain_stats = df.groupby(['ChestPainType', 'HeartDisease']).size().unstack(fill_value=0)
    print("\n Частота типов боли в груди:")
    print(pain_stats)
    return pain_stats
