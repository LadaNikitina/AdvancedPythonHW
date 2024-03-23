import numpy as np
from NumpyMixin import MatrixMixin

np.random.seed(0)
matrix1 = np.random.randint(0, 10, (10, 10)).tolist()
matrix2 = np.random.randint(0, 10, (10, 10)).tolist()
first_matrix = MatrixMixin(matrix1)
second_matrix = MatrixMixin(matrix2)

first_matrix.write_to_file("artifacts/3.2/first_matrix.txt")
second_matrix.write_to_file("artifacts/3.2/second_matrix.txt")

(first_matrix + second_matrix).write_to_file("artifacts/3.2/matrix+.txt")
(first_matrix - second_matrix).write_to_file("artifacts/3.2/matrix-.txt")
(first_matrix * second_matrix).write_to_file("artifacts/3.2/matrix*.txt")
(first_matrix / second_matrix).write_to_file("artifacts/3.2/matrix_div.txt")
(first_matrix @ second_matrix).write_to_file("artifacts/3.2/matrix@.txt")
