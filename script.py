from helper_functions import choose_statistic, population_distribution, sampling_distribution
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
import codecademylib3

# task 1: load in the spotify dataset

# task 2: preview the dataset

# task 3: select the relevant column

# task 5: plot the population distribution with the mean labeled

# task 6: sampling distribution of the sample mean

# task 8: sampling distribution of the sample minimum

# task 10: sampling distribution of the sample variance

# task 13: calculate the population mean and standard deviation

# task 14: calculate the standard error

# task 15: calculate the probability of observing an average tempo of 140bpm or lower from a sample of 30 songs

# task 16: calculate the probability of observing an average tempo of 150bpm or higher from a sample of 30 songs

# EXTRA

spotify_data = pd.read_csv('spotify_data.csv')

print(spotify_data.head())

song_tempos = spotify_data['tempo']

population_distribution(song_tempos)

sampling_distribution(song_tempos, 30, "Mean")

sampling_distribution(song_tempos, 30, "Minimum")

sampling_distribution(song_tempos, 30, "Variance")

np.var(x)
np.var(x, ddof=1)


population_mean = np.mean(song_tempos)
population_std = np.std(song_tempos)


standard_error = population_std / np.sqrt(30)


probability_less_than_140 = stats.norm.cdf(140, population_mean, standard_error)
print(probability_less_than_140)


probability_greater_than_150 = 1 - stats.norm.cdf(150, population_mean, standard_error)
print(probability_greater_than_150)

