import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('C:\pandas files\iris_data.csv')

species_counts = data['Species'].value_counts()
species_labels = species_counts.index
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
ax1.pie(species_counts, labels=species_labels)
ax1.set_title('Доля видов ирисов в датасете')
print(data)
petal_length_counts = pd.cut(data['PetalLengthCm'], bins=[0, 1.2, 1.5, data['PetalLengthCm'].max()],
                            labels=['<1.2', '1.2-1.5', '>1.5']).value_counts()
petal_length_labels = petal_length_counts.index
ax2.pie(petal_length_counts, labels=petal_length_labels)
ax2.set_title('Доли ирисов по длине лепестка')
plt.show()
