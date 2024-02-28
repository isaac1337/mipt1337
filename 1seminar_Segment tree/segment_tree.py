import numpy as np

def is_power_of_two(n):
    return (np.log2(n) % 1 == 0) and n != 0

def next_power_of_two(n):
    if is_power_of_two(n):
        return n
    power = 1
    while power < n:
        power *= 2
    return power

class SumTree:
    def __init__(self, data):
        n = len(data)
        self.original_length = n
        n = next_power_of_two(n)
        self.n = n
        self.tree = [0] * (2 * n)

        for i in range(self.original_length):
            self.tree[n + i] = data[i]

        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.n
        self.tree[index] = value

        while index > 1:
            if index % 2 == 0:
                child_index = index + 1
            else:
                child_index = index - 1
            self.tree[index // 2] = self.tree[index] + self.tree[child_index]
            index //= 2

    def summation(self, l, r):
        l += self.n
        r += self.n
        sum = 0
        while l < r:
            if l & 1:
                sum += self.tree[l]
                l += 1
            if r & 1:
                r -= 1
                sum += self.tree[r]
            l //= 2
            r //= 2
        return sum


#Примерчик
data = [1, 3, 5, 7, 9]
tree = SumTree(data)
print("Сумма элементов с индексами от 1 до 4 включительно:", tree.summation(1, 4))
tree.update(2, 6)
print("Сумма после обновления с индексами от 1 до 4 включительно:", tree.summation(1, 4))
