import pandas as pd, numpy as np, random, matplotlib.pyplot as plt

random.seed(0)
importData = pd.read_csv('C:\OldFaithful.txt', sep=',', header=None)
sample = np.array(importData[1]) #getting the data for the durations of the eruptions

# print(eruptionTime)
sample_median = np.median(sample) # we get 4.0
B = 200

bootstrap_samples = [] #getting our vectors x_1*, x_2*,...,x_n*
for i in range(B):
    bootstrap_samples.append([]) #Create a new bootstrap sample
    for j in range(272):
        bootstrap_samples[i].append(sample[random.randint(0,271)]) #Resample
    bootstrap_samples[i] = np.array(bootstrap_samples[i])


bootstrap_median = [] # getting the medians for each of our bootstrap samples
for i in range(B):
    bootstrap_median.append(np.median(bootstrap_samples[i]))

bootstrap_median_differences = [] # getting the difference with the observed median
for i in range(B):
    bootstrap_median_differences.append(bootstrap_median[i] - sample_median)

# print(bootstrap_median_differences)

distribution = sorted(bootstrap_median_differences)  # sorting the differences between the medians

delta975 = int(0.975 * B)
delta025 = int(0.025 * B)

print((sample_median - distribution[delta975], sample_median - distribution[delta025])) # getting our 95% confidence interval for the median
# print(np.percentile(distribution,0.95))

# for B = 10k we got (3.8915, 4.167)
# for B = 5k we got (3.8915, 4.175)
# for B = 1k we got (3.8915, 4.167)
# all done using the same seed


# for i in sample_median:
#     if i > 1.5 and i < 2:
#         firstBar.append(i)


# x = np.arange(272)
x = np.arange(1.5,5,0.08)
plt.hist(sample, x)
plt.axvline(x = sample_median, color = "black", label = "Sample median")
plt.axvline(x = sample_median - distribution[delta975], color = "r", label = "2.5% mark")
plt.axvline(x = sample_median - distribution[delta025], color = "r", label = "97.5% mark")
plt.xlabel('Duration of the eruption time')
plt.ylabel('Amount of cases')
# plt.legend(bbox_to_anchor=(1, 1), loc='upper left', fontsize='small')
plt.legend(loc='upper center', fontsize = 'large', bbox_to_anchor=(0.5, -0.1),fancybox=True, shadow=True, ncol=5)
plt.show()
