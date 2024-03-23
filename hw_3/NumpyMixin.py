import numpy as np

class MatrixOperatorsMixin(np.lib.mixins.NDArrayOperatorsMixin):
    def __init__(self, matrix):
        self._matrix = matrix

    def __array__(self):
        return np.array(self._matrix)

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method == '__call__':
            inputs = [
                input_obj._matrix if isinstance(input_obj, self.__class__) else input_obj
                for input_obj in inputs
            ]
            return self.__class__(ufunc(*inputs, **kwargs))
        else:
            return NotImplemented

class ToFileMixin:
    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

class ToStringMixin:
    def __str__(self):
        shape = (len(self._matrix), len(self._matrix[0]))        
        max_element_len = max(3, max([
            max([
                len(str(round(self.matrix[i][j], 2))) for j in range(shape[1])
            ]) for i in range(shape[0])
        ]) + 1)
        
        return "[" + '\n'.join(            
            [
                "[" + ''.join([f"{str(round(self.matrix[i][j], 2)):>{max_element_len}}" for j in range(shape[1])]) + "]" 
                for i in range(shape[0])
            ]
        ) + "]"

class GetterSetterMixin:
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value

class MatrixMixin(MatrixOperatorsMixin, ToFileMixin, ToStringMixin, GetterSetterMixin):
    pass