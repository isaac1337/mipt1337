import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('C:\pandas files\iris_data.csv')
dataPd = pd.DataFrame(data = data)
species_counts = data['Species'].value_counts()
a1 = list(dataPd['SepalLengthCm'])
a2 = list(dataPd['SepalWidthCm'])
a3 = list(dataPd['PetalLengthCm'])
a4 = list(dataPd['PetalWidthCm'])
c = [a1,a2,a3,a4]
fig, axs = plt.subplots(4, 4, figsize=(15, 15))
fig.subplots_adjust(hspace=0.4, wspace=0.4)

for i in range(4):
    for j in range(4):
        x = np.array(c[i])
        y = np.array(c[j])
        slope, intercept = np.polyfit(x, y, 1)
        y_pred = slope * x + intercept
        axs[i, j].plot(x, y, 'o', alpha=0.7, label="Данные")
        axs[i, j].plot(x, y_pred, 'r-', label="Линия подгонки")
plt.show()

