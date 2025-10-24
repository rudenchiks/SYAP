import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
    plt.title('Распределение возраста пациентов')
    plt.xlabel('Возраст пациентов')
    plt.ylabel('Количество пациентов')
    plt.show()

def plot_disease_by_gender(df):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Sex', hue='HeartDisease')
    plt.title('Наличие болезни сердца по полу')
    plt.xlabel('Пол')
    plt.ylabel('Количество пациентов')
    plt.legend(title='Болезнь сердца', labels=['Нет', 'Да'])
    plt.show()

def plot_chest_pain(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='ChestPainType', hue='HeartDisease')
    plt.title('Тип боли в груди и болезнь сердца')
    plt.xlabel('Тип боли')
    plt.ylabel('Количество пациентов')
    plt.show()