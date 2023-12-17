import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class TestHeartDiseaseAnalysis(unittest.TestCase):

    def set_up(self):
        # Load the dataset before each test
        self.df = pd.read_csv('heart_disease_dataset.csv')

    def test_gender_distribution(self):
        # Test whether more women or men suffer from heart diseases
        gender_heart_disease = self.df.groupby(['Sex', 'Disease']).size().unstack()
        percentage_women_heart_disease = (gender_heart_disease.loc['female', 1] / gender_heart_disease.loc['female'].sum()) * 100
        percentage_men_heart_disease = (gender_heart_disease.loc['male', 1] / gender_heart_disease.loc['male'].sum()) * 100

        self.assertGreater(percentage_men_heart_disease, percentage_women_heart_disease, "More men should suffer from heart diseases.")

    def test_value_of_serum_cholesterol_gender(self):
        # Test the comparison of average serum cholesterol for men and women with/without heart disease
        average_cholesterol = self.df.groupby(['Sex', 'Disease'])['Serum cholesterol [mg/dl]'].mean().unstack()

        self.assertTrue(average_cholesterol.loc['female', 1] > average_cholesterol.loc['female', 0], "Average serum cholesterol for women with heart disease should be higher.")
        self.assertTrue(average_cholesterol.loc['male', 1] > average_cholesterol.loc['male', 0], "Average serum cholesterol for men with heart disease should be higher.")

    def test_histogram_of_people_with_heart_diseases(self):
        # Test the age distribution of people with heart diseases
        plt.figure()
        sns.histplot(data=self.df[self.df['Disease'] == 1], x='Age', bins=20, kde=True)
        plt.close()

    def test_box_plot_of_heart_disease_by_age(self):
        # Test the box plot for the maximum achieved heart rate by presence of heart disease
        plt.figure()
        sns.boxplot(x='Disease', y='Maximum heart rate achieved', data=self.df)
        plt.close()

    def test_bar_chart_of_heart_disease_by_chest_pain_type(self):
        # Test the bar chart for the frequency of heart disease occurrence by angina presence
        plt.figure()
        angina_chart = self.df.groupby(['Exercise induced angina', 'Disease']).size().unstack()
        angina_chart.plot(kind='bar', stacked=True)
        plt.close()

if __name__ == '__main__':
    unittest.main()
