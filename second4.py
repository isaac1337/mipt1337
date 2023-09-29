import numpy as np
import matplotlib.pyplot as plt

mu = 0
sigma = 1
num_points = [10, 100, 1000, 10000]  # Разное количество точек
fig = plt.figure(figsize=(16, 20))

for i, n in enumerate(num_points):
    ax = fig.add_subplot(len(num_points), 1, i + 1)
    data = np.random.normal(mu, sigma, n)
    ax.hist(data, bins=228)
    ax.set_title(f'n = {n}')

fig.suptitle('Стремление к нормальности')
plt.show()
