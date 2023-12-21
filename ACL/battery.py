import numpy as np
ch = [4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500]
a1_dc = [4.1774, 4.1775, 4.1766, 4.1772, 4.1719, 4.1695, 4.1693, 4.1703, 4.1670, 4.1643]
z1_dc = [4.1993, 4.2010, 4.1975, 4.1970, 4.1991, 4.1950, 4.1943, 4.1936, 4.1923, 4.1908]

answer1 = []
answer2 = []
for i in range(10):
    average1 = (ch[i] + a1_dc[i] ) / 2
    average2 = (ch[i] + z1_dc[i] ) / 2
    answer1.append(average1)
    answer2.append(average2)

print(answer1)
print(answer2)
def calculate_mean_and_error(array):
    mean = np.mean(array)
    error = np.std(array) / np.sqrt(len(array))
    return mean, error

mean, error = calculate_mean_and_error(answer1)
print("Среднее:", mean)
print("Погрешность:", error)
mean, error = calculate_mean_and_error(answer2)
print("Среднее:", mean)
print("Погрешность:", error)

def calculate_resistance(array):
    answer = []
    ch = [4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500, 4.2500]
    for i in range(10):
        resistance = (ch[i] - array[i]) / (2*680 * (10**-6))
        answer.append(resistance)
    return answer
resistance_a1 = calculate_resistance(a1_dc)
resistance_z1 = calculate_resistance(z1_dc)

mean, error = calculate_mean_and_error(resistance_a1)
print("Среднее A1 сопротивление:", mean)
print("Погрешность:", error)
mean, error = calculate_mean_and_error(resistance_z1)
print("Среднее Z1 сопротивление:", mean)
print("Погрешность:", error)
