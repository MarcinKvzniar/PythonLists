import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def get_gender_distribution(df):
    gender_heart_disease = df.groupby(['Sex', 'Disease']).size().unstack()
    percentage_women_heart_disease = (gender_heart_disease.loc['female', 1]
                                      / gender_heart_disease.loc['female'].sum()) * 100
    percentage_men_heart_disease = (gender_heart_disease.loc['male', 1]
                                    / gender_heart_disease.loc['male'].sum()) * 100

    print(f"Percentage of women with heart disease: {percentage_women_heart_disease:.2f}%")
    print(f"Percentage of men with heart disease: {percentage_men_heart_disease:.2f}%")


def get_value_of_serum_cholesterol_gender(df):
    average_cholesterol = df.groupby(['Sex', 'Disease'])['Serum cholesterol [mg/dl]'].mean().unstack()
    print("\nAverage Serum Cholesterol:")
    print(average_cholesterol)


def get_histogram_of_people_with_heart_diseases(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df[df['Disease'] == 1], x='Age', bins=20, kde=True)
    plt.title('Histogram of People with Heart Diseases by Age')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()


def get_box_plot_of_heart_disease_by_age(df):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Disease', y='Maximum heart rate achieved', data=df)
    plt.title('Box Plot of Maximum Achieved Heart Rate by Heart Disease Presence')
    plt.xlabel('Heart Disease')
    plt.ylabel('Maximum Heart Rate Achieved')
    plt.show()


def get_bar_chart_of_heart_disease_by_chest_pain_type(df):
    angina_chart = df.groupby(['Exercise induced angina', 'Disease']).size().unstack()
    angina_chart.plot(kind='bar', stacked=True)
    plt.title('Bar Chart of Heart Disease Occurrence by Exercise Induced Angina')
    plt.xlabel('Exercise Induced Angina')
    plt.ylabel('Count')
    plt.show()


if __name__ == '__main__':
    df = pd.read_csv('heart_disease_dataset.csv')
    print("Heart Disease Analysis:")

    print("Task 1: ")
    print(get_gender_distribution(df))