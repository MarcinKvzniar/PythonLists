import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def print_disease_by_gender_distribution(df):
    """
    This function calculates and prints the amount of men and women with
    diseases and the percentage difference between them. For the testing
    purposes returns a data which will be printed into console in a form
    of tuple. I decided to present the percentage difference between the
    as a value rounded up to two decimal places.

    Arguments:
        df (DataFrame): A pandas dataframe containing the heart disease
         dataset.

    Returns:
        Data which will be printed into console in a form of tuple.
    """
    men_with_disease = df[(df['Sex'] == 'male')
                          & (df['Disease'] == 1)].shape[0]
    women_with_disease = df[(df['Sex'] == 'female')
                            & (df['Disease'] == 1)].shape[0]
    difference = abs(men_with_disease - women_with_disease)
    percentage_difference = (difference / (min(men_with_disease,
                                               women_with_disease)) * 100)

    percentage_difference = round(percentage_difference, 2)

    print("Men with heart disease:", men_with_disease)
    print("Women with heart disease:", women_with_disease)
    print("Percentage difference:", percentage_difference, "%")

    return men_with_disease, women_with_disease, percentage_difference


def print_value_of_serum_cholesterol_gender(df):
    """
    This function calculates and prints the average value of serum
    cholesterol by gender. For the testing purposes returns a data
    which will be printed into console in a form of tuple. I decided
    to present the average value of serum cholesterol rounded up to two
    decimal places.

    Arguments:
        df (DataFrame): A pandas dataframe containing the heart disease
         dataset.

    Returns:
        Data which will be printed into console in a form of tuple.
    """
    avg_cholesterol_healthy_men = df.loc[
        (df['Sex'] == 'male') & (df['Disease'] == 0),
        'Serum cholesterol in mg/dl'].mean()
    avg_cholesterol_healthy_women = df.loc[
        (df['Sex'] == 'female') & (df['Disease'] == 0),
        'Serum cholesterol in mg/dl'].mean()

    avg_cholesterol_men_with_disease = df.loc[
        (df['Sex'] == 'male') & (df['Disease'] == 1),
        'Serum cholesterol in mg/dl'].mean()
    avg_cholesterol_women_with_disease = df.loc[
        (df['Sex'] == 'female') & (df['Disease'] == 1),
        'Serum cholesterol in mg/dl'].mean()

    avg_cholesterol_healthy_men = round(avg_cholesterol_healthy_men, 2)
    avg_cholesterol_healthy_women = round(avg_cholesterol_healthy_women, 2)
    avg_cholesterol_men_with_disease = \
        round(avg_cholesterol_men_with_disease, 2)
    avg_cholesterol_women_with_disease = \
        round(avg_cholesterol_women_with_disease, 2)

    print("Avg cholesterol of healthy men:",
          avg_cholesterol_healthy_men)
    print("Avg cholesterol of healthy women:",
          avg_cholesterol_healthy_women)
    print("Avg cholesterol of men with disease:",
          avg_cholesterol_men_with_disease)
    print("Avg cholesterol of women with disease:",
          avg_cholesterol_women_with_disease)

    return avg_cholesterol_healthy_men, avg_cholesterol_healthy_women, \
        avg_cholesterol_men_with_disease, avg_cholesterol_women_with_disease


def get_histogram_of_people_with_heart_diseases(df):
    """
    This functions generates a histogram of the ages of people with heart
    diseases, and for the testing purposes returns the ages of people with
    heart diseases.
    For the number of bins I used the square-root choice, as it is one of
    the most commonly used methods for choosing the number of bins.

    Arguments:
        df (DataFrame): A pandas dataframe containing the heart disease
         dataset.

    Returns:
        ages (list): A list of ages of people with heart diseases.
    """
    df_disease = df[df['Disease'] == 1]
    ages = df_disease['Age'].tolist()
    num_bins = int(np.sqrt(len(ages)))

    plt.figure(figsize=(10, 6))
    plt.hist(ages, bins=num_bins, edgecolor='black', color='#86bf91',
             alpha=0.7)

    plt.xlabel('Age', fontsize=15)
    plt.ylabel('Number of persons', fontsize=15)
    plt.title('Age Distribution of Individuals with Heart Disease',
              fontsize=18)

    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    return ages


def get_box_plot_of_max_achieved_heart_rate(df):
    """
    This function generates a box plot of the maximum achieved heart rate
    during the exercise test depending on the presence of heart disease.
    For the testing purposes returns the heart rate of people with and
    without diseases as a tuple.

    Arguments:
        df (DataFrame): A pandas dataframe containing the heart disease
         dataset.

    Returns:
        heart_rate_with_disease (list): A list of heart rates of people with
         heart diseases.
        heart_rate_without_disease (list): A list of heart rates of people
         without heart diseases.
    """
    heart_rate_with_disease = df.loc[df['Disease'] == 1,
    'Maximum heart rate achieved'].tolist()
    heart_rate_without_disease = df.loc[df['Disease'] == 0,
    'Maximum heart rate achieved'].tolist()

    sns.set(style="whitegrid")
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Disease', y='Maximum heart rate achieved', data=df)

    plt.xlabel('Presence of Heart Disease', fontsize=12)
    plt.ylabel('Maximum Heart Rate Achieved', fontsize=12)
    plt.title('Heart Rate vs Presence of Heart Disease During Exercise Test', fontsize=15)

    plt.xticks(ticks=[0, 1], labels=['No Disease', 'Heart Disease'])
    plt.yticks(fontsize=10)
    plt.show()

    return heart_rate_with_disease, heart_rate_without_disease


def get_bar_chart_of_frequency_of_heart_disease_by_angina(df):
    """
    This function generates a bar chart of the frequency of heart disease
    occurrence depending on whether the patient has angina during the
    exercise test. For the testing purposes returns the frequency of heart
    disease occurrence depending on whether the patient has angina during the
    exercise test.

    Arguments:
        df (DataFrame): A pandas dataframe containing the heart disease
         dataset.

    Returns:
        counts (list): A list containing the frequency of heart disease
         occurrence depending on whether the patient has angina during the
         exercise test.

    """
    counts = df.groupby(['Exercise induced angina', 'Disease']).size().tolist()

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Exercise induced angina', hue='Disease', data=df,
                  palette="viridis")

    plt.xlabel('Exercise Induced Angina', fontsize=15)
    plt.ylabel('Frequency', fontsize=15)
    plt.title('Frequency of Heart Disease Occurrence Depending on Exercise'
              ' Induced Angina', fontsize=18)
    plt.legend(title='Presence of Heart Disease', title_fontsize='10',
               loc='upper right')
    plt.show()

    return counts


if __name__ == '__main__':
    try:
        df = pd.read_csv('heart_disease_dataset.csv')
        print("Heart Disease Analysis:")

        print("\nTask 1: ")
        print_disease_by_gender_distribution(df)

        print("\nTask 2: ")
        print_value_of_serum_cholesterol_gender(df)

        print("\nTask 3: ")
        get_histogram_of_people_with_heart_diseases(df)
        print("Generated histogram")

        print("\nTask 4: ")
        get_box_plot_of_max_achieved_heart_rate(df)
        print("Generated box plot")

        print("\nTask 5: ")
        get_bar_chart_of_frequency_of_heart_disease_by_angina(df)
        print("Generated bar chart")

    except FileNotFoundError as e:
        print(f"Error: {e}. File not found.")
