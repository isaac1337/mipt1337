class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

# тестим
fw = FenwickTree(5)
fw.update(1, 5)
fw.update(2, 3)
fw.update(3, 7)
print(fw.range_sum(1, 3))
fw.update(3, -2)
print(fw.range_sum(1, 3))  
