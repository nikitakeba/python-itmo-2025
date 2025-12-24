import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Размеры матриц не совпадают")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] * other.data[i][j])
            result.append(row)
        return Matrix(result)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Размеры матриц не совпадают")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                s = 0
                for k in range(self.cols):
                    s += self.data[i][k] * other.data[k][j]
                row.append(s)
            result.append(row)
        return Matrix(result)

    def __str__(self):
        lines = []
        for row in self.data:
            lines.append(' '.join(map(str, row)))
        return '\n'.join(lines)


np.random.seed(0)
a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

m1 = Matrix(a.tolist())
m2 = Matrix(b.tolist())

with open("artifacts/matrix+.txt", "w") as f:
    f.write(str(m1 + m2))

with open("artifacts/matrix*.txt", "w") as f:
    f.write(str(m1 * m2))

with open("artifacts/matrix@.txt", "w") as f:
    f.write(str(m1 @ m2))

print(f"A: \n{a}")
print(f"B: \n{b}")

print(f"A + B: \n{m1 + m2}")
print(f"A * B (покомпонентно): \n{m1 * m2}")
print(f"A @ B (матричное): \n{m1 @ m2}")
print(f"A + B (np): \n{np.add(a, b)}")
print(f"A * B (np): \n{np.multiply(a, b)}")
print(f"A @ B (np): \n{np.matmul(a, b)}")
