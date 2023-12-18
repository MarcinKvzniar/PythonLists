import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_gender_distribution(df):
    """

    :param df:
    :return:
    """
    men_with_disease = df[(df['Sex'] == 'male') & (df['Disease'] == 1)].shape[0]
    women_with_disease = df[(df['Sex'] == 'female') & (df['Disease'] == 1)].shape[0]
    difference = abs(men_with_disease - women_with_disease)
    percentage_difference = difference / (min(men_with_disease, women_with_disease)) * 100

    print("Men with disease:", men_with_disease)
    print("Women with disease:", women_with_disease)
    print("Percentage difference:", percentage_difference)


def get_value_of_serum_cholesterol_gender(df):
    """

    :param df:
    :return:
    """
    avg_cholesterol_healthy_men = df.loc[
        (df['Sex'] == 'male') & (df['Disease'] == 0), 'Serum cholesterol in mg/dl'].mean()
    avg_cholesterol_healthy_women = df.loc[
        (df['Sex'] == 'female') & (df['Disease'] == 0), 'Serum cholesterol in mg/dl'].mean()

    avg_cholesterol_men_with_disease = df.loc[
        (df['Sex'] == 'male') & (df['Disease'] == 1), 'Serum cholesterol in mg/dl'].mean()
    avg_cholesterol_women_with_disease = df.loc[
        (df['Sex'] == 'female') & (df['Disease'] == 1), 'Serum cholesterol in mg/dl'].mean()

    print("Avg cholesterol of healthy men:", avg_cholesterol_healthy_men)
    print("Avg cholesterol of healthy women:", avg_cholesterol_healthy_women)
    print("Avg cholesterol of men with disease:", avg_cholesterol_men_with_disease)
    print("Avg cholesterol of women with disease:", avg_cholesterol_women_with_disease)


def get_histogram_of_people_with_heart_diseases(df):
    """

    :param df:
    :return:
    """
    df_disease = df[df['Disease'] == 1]
    ages = df_disease['Age']
    plt.hist(ages, bins=10, edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Number of Individuals')
    plt.title('Age Distribution of Individuals with Heart Disease')
    plt.show()
    return ages


def get_box_plot_of_heart_disease_by_age(df):
    """

    :param df:
    :return:
    """
    heart_rate_with_disease = df.loc[df['Disease'] == 1,
    'Maximum heart rate achieved']
    heart_rate_without_disease = df.loc[df['Disease'] == 0,
    'Maximum heart rate achieved']
    sns.boxplot(x='Disease', y='Maximum heart rate achieved', data=df)
    plt.xlabel('Presence of Heart Disease')
    plt.ylabel('Maximum Heart Rate Achieved')
    plt.title('Heart Rate vs Presence of Heart Disease')
    plt.show()
    return heart_rate_with_disease, heart_rate_without_disease


def get_bar_chart_of_heart_disease_by_chest_pain_type(df):
    """

    :param df:
    :return:
    """
    counts = df.groupby(['Exercise induced angina', 'Disease']).size()
    sns.countplot(x='Exercise induced angina', hue='Disease', data=df)
    plt.xlabel('Exercise Induced Angina')
    plt.ylabel('Frequency')
    plt.title('Frequency of Heart Disease Occurrence Depending on Exercise Induced Angina')
    plt.show()
    return counts


if __name__ == '__main__':
    df = pd.read_csv('heart_disease_dataset.csv')
    print("Heart Disease Analysis:")

    print("\nTask 1: ")
    get_gender_distribution(df)

    print("\nTask 2: ")
    get_value_of_serum_cholesterol_gender(df)

    print("\nTask 3: ")
    get_histogram_of_people_with_heart_diseases(df)

    print("\nTask 4: ")
    get_box_plot_of_heart_disease_by_age(df)

    print("\nTask 5: ")
    get_bar_chart_of_heart_disease_by_chest_pain_type(df)
