import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class StrMixin:
    def __str__(self):
        lines = []
        for row in self.data:
            lines.append(' '.join(map(str, row)))
        return '\n'.join(lines)


class FileMixin:
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))


class GetSetMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = np.asarray(value)


class Matrix(NDArrayOperatorsMixin, StrMixin, FileMixin, GetSetMixin):
    def __init__(self, data):
        self.data = data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        inputs = [x.data if isinstance(x, Matrix) else x for x in inputs]
        result = getattr(ufunc, method)(*inputs, **kwargs)
        if isinstance(result, np.ndarray):
            return Matrix(result)
        return result


np.random.seed(0)
a = np.random.randint(0, 10, (10, 10))
b = np.random.randint(0, 10, (10, 10))

m1 = Matrix(a)
m2 = Matrix(b)

(m1 + m2).save("artifacts/matrix+_v2.txt")
(m1 * m2).save("artifacts/matrix*_v2.txt")
(m1 @ m2).save("artifacts/matrix@_v2.txt")

print(f"A:\n{m1}")
print(f"B:\n{m2}")
print(f"A + B:\n{m1 + m2}")
print(f"A * B:\n{m1 * m2}")
print(f"A @ B:\n{m1 @ m2}")

