import unittest
from height_dataset import *


class TestHeightDataset(unittest.TestCase):

    def setUp(self):
        # Set up common data for tests
        self.height_data = generate_height_data()

    def test_descriptive_statistics(self):
        # Test descriptive_statistics function
        descriptive_statistics(self.height_data)

    def test_visualize_histogram(self):
        # Test visualize_histogram function
        visualize_histogram(self.height_data)

    def test_calculate_percentiles(self):
        # Test calculate_percentiles function
        calculate_percentiles(self.height_data)

    def test_identify_outliers(self):
        # Test identify_outliers function
        identify_outliers(self.height_data)

    def test_random_sampling(self):
        # Test random_sampling function
        random_sampling(self.height_data)

    def test_hypothesis_testing(self):
        # Test hypothesis_testing function
        hypothesis_testing(self.height_data)

    def test_calculate_probability(self):
        # Test calculate_probability function
        calculate_probability(self.height_data)

    def test_generate_height_data(self):
        # Test generate_height_data function
        size = 500
        heights = generate_height_data(size=size)
        self.assertEqual(len(heights), size)
        self.assertIsInstance(heights, np.ndarray)


if __name__ == '__main__':
    unittest.main()


