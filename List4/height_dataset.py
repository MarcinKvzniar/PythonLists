import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp


def generate_height_data(size=1000, mean=170, std_dev=10):
    """
    Generates a list of heights based on a normal distribution

    Arguments:
        size: the number of heights to generate
        mean: the mean height
        std_dev: the standard deviation of the heights
    Returns:
        heights: a list of heights
    """
    heights = np.random.normal(mean, std_dev, size)
    return heights


def descriptive_statistics(height_data):
    """
    Calculates the mean, median, and standard deviation of the height data

    Arguments:
        height_data: a list of heights

    """
    mean_value = np.mean(height_data)
    median_value = np.median(height_data)
    std_dev_value = np.std(height_data)

    print("Mean:", mean_value)
    print("Median:", median_value)
    print("Standard Deviation:", std_dev_value)


def visualize_histogram(height_data):
    """
    Visualizes the height data in a histogram

    Arguments:
        height_data: a list of heights

    """
    plt.hist(height_data, bins=30, edgecolor='black')
    plt.title('Height Distribution')
    plt.xlabel('Height (cm)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()


def calculate_percentiles(height_data):
    """
    Calculates the 25th, 50th, and 75th percentiles of the height data

    Arguments:
        height_data: a list of heights
    """
    percentile_25th = np.percentile(height_data, 25)
    percentile_50th = np.percentile(height_data, 50)
    percentile_75th = np.percentile(height_data, 75)

    print("25th Percentile:", percentile_25th)
    print("50th Percentile (Median):", percentile_50th)
    print("75th Percentile:", percentile_75th)


def identify_outliers(height_data):
    """
    Identifies outliers in the height data

    Arguments:
        height_data: a list of heights
    """
    q1 = np.percentile(height_data, 25)
    q3 = np.percentile(height_data, 75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = height_data[(height_data < lower_bound)
                           | (height_data > upper_bound)]

    print("Identified Outliers:")
    print(outliers)


def random_sampling(height_data):
    """
    Randomly samples 50 heights from the height data

    Arguments:
        height_data: a list of heights
    """
    sampled_heights = np.random.choice(height_data, size=50, replace=False)
    print("Randomly Sampled 50 Heights:")
    print(sampled_heights)


def hypothesis_testing(data, null_hypothesis_mean=165):
    """
    Performs a hypothesis test on the height data

    Arguments:
        data: a list of heights
        null_hypothesis_mean: the mean of the null hypothesis

    """
    t_statistic, p_value = ttest_1samp(data, null_hypothesis_mean)

    print("Null Hypothesis Mean:", null_hypothesis_mean)
    print("Sample Mean:", np.mean(data))
    print("T-statistic:", t_statistic)
    print("P-value:", p_value)

    alpha = 0.05
    if p_value < alpha:
        print("The null hypothesis can be rejected.")
    else:
        print("There is not enough evidence to reject the null hypothesis.")


def calculate_probability(data, threshold_height=180):
    """
    Calculates the probability of randomly selecting an individual with a
    height greater than the threshold height

    Arguments:
        data: a list of heights
        threshold_height: the threshold height

    Returns:
        probability: the probability of randomly selecting an individual
        with a height greater than the threshold height

    """
    probability = np.mean(data > threshold_height)

    print(f"The probability of randomly selecting an individual with a"
          f" height greater than {threshold_height} cm is: {probability:.4f}")


if __name__ == "__main__":
    height_data = generate_height_data()

    print("Descriptive Statistics:")
    descriptive_statistics(height_data)

    visualize_histogram(height_data)

    print("\nPercentiles:")
    calculate_percentiles(height_data)

    print("\nOutliers:")
    identify_outliers(height_data)

    print("\nRandom Sampling:")
    random_sampling(height_data)

    print("\nHypothesis Testing:")
    hypothesis_testing(height_data)

    print("\nProbability:")
    calculate_probability(height_data)






