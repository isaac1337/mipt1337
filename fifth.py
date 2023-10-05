import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\pandas files\BTC_data.csv')
data['time'] = pd.to_datetime(data['time'])
data_with_index = data.set_index('time')
plt.plot(data_with_index['close'])
plt.xlabel('Дата')
plt.ylabel('Цена закрытия, баксы')
plt.title('Исторический график цены биткоина')
plt.show()
