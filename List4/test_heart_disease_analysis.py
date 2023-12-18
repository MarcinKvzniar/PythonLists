import unittest
import pandas as pd
import heart_disease_analysis as hda


class TestHeartDiseaseAnalysis(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = pd.DataFrame({
            'Sex': ['male', 'female', 'male', 'female'],
            'Disease': [1, 0, 0, 1],
            'Serum cholesterol in mg/dl': [200, 180, 220, 210],
            'Age': [60, 55, 62, 65],
            'Maximum heart rate achieved': [150, 160, 140, 155],
            'Exercise induced angina': [1, 0, 0, 1]
        })

    def test_get_gender_distribution(self):
        # Test get_gender_distribution function
        men_with_disease, women_with_disease, percentage_difference\
            = hda.get_gender_distribution(self.df)

        self.assertEqual(men_with_disease, 1)
        self.assertEqual(women_with_disease, 1)
        self.assertEqual(percentage_difference, 0)

    def test_get_value_of_serum_cholesterol_gender(self):
        # Test get_value_of_serum_cholesterol_gender function
        (avg_cholesterol_healthy_men, avg_cholesterol_healthy_women,
         avg_cholesterol_men_with_disease, avg_cholesterol_women_with_disease)\
            = hda.get_value_of_serum_cholesterol_gender(self.df)

        self.assertEqual(avg_cholesterol_healthy_men, 220)
        self.assertEqual(avg_cholesterol_healthy_women, 180)
        self.assertEqual(avg_cholesterol_men_with_disease, 200)
        self.assertEqual(avg_cholesterol_women_with_disease, 210)

    def test_get_histogram_of_people_with_heart_diseases(self):
        # Test get_histogram_of_people_with_heart_diseases function
        ages = hda.get_histogram_of_people_with_heart_diseases(self.df)

        # Add assertions here to verify the results
        self.assertEqual(len(ages), 2)
        self.assertEqual(min(ages), 60)
        self.assertEqual(max(ages), 65)

    def test_get_box_plot_of_heart_disease_by_age(self):
        # Test get_box_plot_of_heart_disease_by_age function
        heart_rate_with_disease, heart_rate_without_disease =\
            hda.get_box_plot_of_heart_disease_by_age(self.df)

        # Add assertions here to verify the results
        self.assertEqual(len(heart_rate_with_disease), 1)
        self.assertEqual(len(heart_rate_without_disease), 2)

    def test_get_bar_chart_of_heart_disease_by_chest_pain_type(self):
        # Test get_bar_chart_of_heart_disease_by_chest_pain_type function
        counts = hda.get_bar_chart_of_heart_disease_by_chest_pain_type(self.df)

        # Add assertions here to verify the results
        self.assertEqual(counts[(0, 0)], 1)
        self.assertEqual(counts[(0, 1)], 1)
        self.assertEqual(counts[(1, 0)], 0)
        self.assertEqual(counts[(1, 1)], 1)


if __name__ == '__main__':
    unittest.main()

