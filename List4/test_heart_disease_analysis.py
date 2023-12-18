import unittest
import pandas as pd
import heart_disease_analysis as hda


class TestHeartDiseaseDatasetAnalysis(unittest.TestCase):

    def setUp(self):
        data = {
            'Sex': ['male', 'male', 'male', 'male', 'male',
                    'female', 'female', 'female', 'female', 'female'],
            'Age': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
            'Disease': [1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            'Serum cholesterol in mg/dl': [180, 210, 190, 200, 220,
                                           170, 160, 190, 200, 180],
            'Maximum heart rate achieved': [190, 180, 170, 160, 150,
                                            175, 165, 155, 145, 140],
            'Exercise induced angina': [1, 0, 0, 1, 1, 0, 1, 0, 1, 0]
        }
        self.df = pd.DataFrame(data)

    def test_print_disease_by_gender_distribution(self):
        """
        Test for correct console output in a form of tuple:
        (men_with_disease, women_with_disease, percentage_difference)
        """
        self.assertEqual(hda.print_disease_by_gender_distribution(self.df),
                         (3, 2, 50.0))

    def test_print_value_of_serum_cholesterol_gender(self):
        """
        Test for correct console output in a form of tuple:
        (avg_cholesterol_healthy_men, avg_cholesterol_healthy_women,
        avg_cholesterol_men_with_disease, avg_cholesterol_women_with_disease)

        """
        self.assertEqual(hda.print_value_of_serum_cholesterol_gender(self.df),
                         (210.0, 190.0, 193.33, 165.0))

    def test_histogram_of_people_with_heart_diseases(self):
        # Test for the histogram of people with heart diseases
        ages = hda.get_histogram_of_people_with_heart_diseases(self.df)
        self.assertIsInstance(ages, list)
        self.assertEqual(len(ages), 5)
        self.assertEqual(ages, [30, 35, 40, 55, 60])

    def test_box_plot_of_heart_disease_by_age(self):
        # Test for the box plot of heart disease by age
        heart_rate_with_disease, heart_rate_without_disease \
            = hda.get_box_plot_of_max_achieved_heart_rate(self.df)

        self.assertIsInstance(heart_rate_with_disease, list)
        self.assertIsInstance(heart_rate_without_disease, list)

        self.assertEqual(len(heart_rate_with_disease), 5)
        self.assertEqual(len(heart_rate_without_disease), 5)

        self.assertEqual(heart_rate_with_disease,
                         [190, 180, 170, 175, 165])
        self.assertEqual(heart_rate_without_disease,
                         [160, 150, 155, 145, 140])

    def test_bar_chart_of_heart_disease_by_chest_pain_type(self):
        # Test for the bar chart of heart disease by chest pain type
        counts = hda.get_bar_chart_of_frequency_of_heart_disease_by_angina(self.df)

        self.assertIsInstance(counts, list)
        self.assertEqual(len(counts), 4)
        self.assertEqual(counts, [2, 3, 3, 2])


if __name__ == '__main__':
    unittest.main()
