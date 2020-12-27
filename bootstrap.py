import numpy as np, random, matplotlib.pyplot as plt


sample = np.array([random.randint(1,100) for i in range(50)])

bootstrap_samples = []

for i in range(10000):
    bootstrap_samples.append([]) #Create a new bootstrap sample
    for j in range(50):
        bootstrap_samples[i].append(sample[random.randint(0,49)]) #Resample
    bootstrap_samples[i] = np.array(bootstrap_samples[i])
sample_mean = np.mean(sample)

bootstrap_mean= [round(np.mean(_),1) for _ in bootstrap_samples]
std_error = np.std(bootstrap_mean)

d = {}

for i in bootstrap_mean: #Count the data
    if i in d:
        d[i]+=1
    else:
        d[i] = 1

lists = sorted(d.items())
x, y = zip(*lists)



plt.plot(x, y,"ro")
plt.axvline(x = sample_mean, color = "g", label = "Sample Mean")
plt.legend(bbox_to_anchor = (0.8, 1), loc = 'upper left') 
plt.show()
