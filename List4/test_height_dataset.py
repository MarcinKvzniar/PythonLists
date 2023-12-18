import unittest
import numpy as np
import height_dataset as hd


class TestHeightDataset(unittest.TestCase):

    def setUp(self):
        self.height_data = \
            hd.generate_height_data(size=1000, mean=170, std_dev=10)

    def test_generate_height_data(self):
        # Test for generate_height_data function
        size = 1000
        mean = 170
        std_dev = 10
        height_data = hd.generate_height_data(size, mean, std_dev)

        self.assertEqual(len(height_data), size)
        self.assertAlmostEqual(np.mean(height_data), mean, delta=mean)
        self.assertAlmostEqual(np.std(height_data), std_dev, delta=std_dev)

    def test_descriptive_statistics(self):
        # Test for descriptive_statistics function
        mean, median, std_dev = hd.descriptive_statistics(self.height_data)

        self.assertTrue(isinstance(mean, float))
        self.assertTrue(isinstance(median, float))
        self.assertTrue(isinstance(std_dev, float))

    def test_visualize_histogram(self):
        # Test visualize_histogram function
        hd.visualize_histogram(self.height_data)

    def test_calculate_percentiles(self):
        # Test for calculate_percentiles function
        percentile_25th, percentile_50th, percentile_75th = \
            hd.calculate_percentiles(self.height_data)

        self.assertTrue(isinstance(percentile_25th, float))
        self.assertTrue(isinstance(percentile_50th, float))
        self.assertTrue(isinstance(percentile_75th, float))

    def test_identify_outliers(self):
        # Test for identify_outliers function
        outliers = hd.identify_outliers(self.height_data)

        self.assertTrue(isinstance(outliers, list))

        for outlier in outliers:
            self.assertTrue(isinstance(outlier, float))

    def test_random_sampling(self):
        # Test for random_sampling function
        sampled_heights = hd.random_sampling(self.height_data)

        self.assertEqual(len(sampled_heights), 50)

        for height in sampled_heights:
            self.assertTrue(isinstance(height, float))

    def test_hypothesis_testing(self):
        # Test for hypothesis_testing function
        t_statistic, p_value, result =\
            hd.hypothesis_testing(self.height_data, null_hypothesis_mean=165)

        self.assertTrue(isinstance(t_statistic, float))
        self.assertTrue(isinstance(p_value, float))
        self.assertTrue(isinstance(result, str))

    def test_calculate_probability(self):
        # Test for calculate_probability function
        probability =\
            hd.calculate_probability(self.height_data, threshold_height=180)

        self.assertTrue(isinstance(probability, float))


if __name__ == '__main__':
    unittest.main()
