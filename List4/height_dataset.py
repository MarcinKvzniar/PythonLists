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
    height_data = np.random.normal(mean, std_dev, size)
    return height_data


def descriptive_statistics(height_data):
    """
    Calculates the mean, median, and standard deviation of the height data.
    For testing purposes, the function also returns the calculated values
    in a form of a tuple. In order to increase readability I rounded the
    printed into console values to two decimal places.

    Arguments:
        height_data: a list of heights

    Returns:
        mean_value: the mean of the height data
        median_value: the median of the height data
        std_dev_value: the standard deviation of the height data
    """
    mean_value = np.mean(height_data)
    median_value = np.median(height_data)
    std_dev_value = np.std(height_data)

    print("Mean:", round(mean_value, 2))
    print("Median:", round(median_value, 2))
    print("Standard Deviation:", round(std_dev_value, 2))

    return mean_value, median_value, std_dev_value


def visualize_histogram(height_data):
    """
    Visualizes the height data in a histogram. For the number of bins
    I used the square-root choice, as it is one of the most commonly
    used methods for choosing the number of bins.

    Arguments:
        height_data: a list of heights
    """
    num_bins = int(np.sqrt(len(height_data)))

    plt.figure(figsize=(10, 6))
    plt.hist(height_data, bins=num_bins, color='#86bf91',
             edgecolor='black', alpha=0.7)
    plt.title('Height Distribution', fontsize=18)
    plt.xlabel('Height (cm)', fontsize=15)
    plt.ylabel('Frequency', fontsize=15)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()


def calculate_percentiles(height_data):
    """
    Calculates the 25th, 50th, and 75th percentiles of the height data.
    For testing purposes, the function also returns the calculated values
    in a form of a tuple. In order to increase readability I rounded the
    printed into console values to two decimal places.

    Arguments:
        height_data: a list of heights

    Returns:
        percentile_25th: the 25th percentile of the height data
        percentile_50th: the 50th percentile (median) of the height data
        percentile_75th: the 75th percentile of the height data
    """
    percentile_25th = np.percentile(height_data, 25)
    percentile_50th = np.percentile(height_data, 50)
    percentile_75th = np.percentile(height_data, 75)

    print("25th Percentile:", round(percentile_25th, 2))
    print("50th Percentile (Median):", round(percentile_50th, 2))
    print("75th Percentile:", round(percentile_75th, 2))

    return percentile_25th, percentile_50th, percentile_75th


def identify_outliers(height_data):
    """
    Identifies outliers in the height data according to the IQR method:
    "https://articles.outlier.org/calculate-outlier-formula#section-
    examples-of-outlier-formula"
    For testing purposes, the function also returns the calculated values.
    In order to increase readability I rounded the printed into console
    height outliers values to two decimal places.

    Arguments:
        height_data: a list of heights

    Returns:
        outliers: a list of potential outliers in the height data
    """
    q1 = np.percentile(height_data, 25)
    q3 = np.percentile(height_data, 75)
    iqr = q3 - q1

    upper_bound = q3 + 1.5 * iqr
    lower_bound = q1 - 1.5 * iqr

    outliers = []
    for height in height_data:
        if height < lower_bound or height > upper_bound:
            height = round(height, 2)
            outliers.append(height)

    print("Identified Outliers:")
    print(outliers)

    return outliers


def random_sampling(height_data):
    """
    Randomly samples 50 heights from the height data. For testing purposes,
    the function also returns the sampled heights. In order to increase
    readability I rounded the printed into console height outliers values
    to two decimal places.

    Arguments:
        height_data: a list of heights

    Returns:
        sampled_heights: a list of 50 randomly sampled heights
    """
    sampled_heights = np.random.choice(height_data, size=50, replace=False)
    sampled_heights = np.round(sampled_heights, 2)

    print("Randomly Sampled 50 Heights:")
    print(sampled_heights)

    return sampled_heights


def hypothesis_testing(data, null_hypothesis_mean=165):
    """
    Performs a hypothesis test on the height data, based on the null
    hypothesis that the mean height of the population is 165 cm.
    "https://docs.scipy.org/doc/scipy/reference/generated/
    scipy.stats.ttest_1samp.html"
    For testing purposes, the function also returns the calculated values
    in a form of a tuple.

    Arguments:
        data: a list of heights
        null_hypothesis_mean: the mean of the null hypothesis

    Returns:
        t_statistic: the t-statistic of the hypothesis test
        p_value: the p-value of the hypothesis test
    """
    t_statistic, p_value = ttest_1samp(data, null_hypothesis_mean)

    print("Null Hypothesis Mean:", null_hypothesis_mean)
    print("Sample Mean:", round(np.mean(data), 2))
    print("T-statistic:", t_statistic)
    print("P-value:", p_value)

    alpha = 0.05
    if p_value < alpha:
        result = "The null hypothesis can be rejected."
    else:
        result = "There is not enough evidence to reject the null hypothesis."

    print(result)
    return t_statistic, p_value, result


def calculate_probability(data, threshold_height=180):
    """
    Calculates the probability of randomly selecting an individual with a
    height greater than the threshold height. For testing purposes, the
    function also returns the calculated probability. I decided to round
    the printed into console probability value to four decimal places.

    Arguments:
        data: a list of heights
        threshold_height: the threshold height

    Returns:
        probability: the probability of randomly selecting an individual
        with a height greater than the threshold height

    """
    probability = np.mean(data > threshold_height)
    probability = probability.round(4)

    print(f"The probability of randomly selecting an individual with a"
          f" height greater than {threshold_height} cm is: {probability}")

    return probability


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
