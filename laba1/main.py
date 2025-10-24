from data_loader import (
    load_and_clean_data,
    infoo,
    analyze_disease_by_gender,
    analyze_chest_pain
)
from visualize import (
    plot_age_distribution,
    plot_disease_by_gender,
    plot_chest_pain,
)

def main():
    file_path = "heart.csv"

    print("Загрузка и очистка данных...")
    df = load_and_clean_data(file_path)

    infoo(df)
    analyze_disease_by_gender(df)
    analyze_chest_pain(df)

    print("\n Построение графиков...")
    plot_age_distribution(df)
    plot_disease_by_gender(df)
    plot_chest_pain(df)

if __name__ == "__main__":
    main()
