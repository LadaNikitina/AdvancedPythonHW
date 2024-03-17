import numpy as np
from LDRMatrix import LDRMatrix

np.random.seed(0)
matrix1 = np.random.randint(0, 10, (10, 10)).tolist()
matrix2 = np.random.randint(0, 10, (10, 10)).tolist()
first_matrix = LDRMatrix(matrix1)
second_matrix = LDRMatrix(matrix2)

with open("artifacts/3.1/matrix+.txt", "w") as file:
    file.write(str(first_matrix + second_matrix))

with open("artifacts/3.1/matrix*.txt", "w") as file:
    file.write(str(first_matrix * second_matrix))

with open("artifacts/3.1/matrix@.txt", "w") as file:
    file.write(str(first_matrix @ second_matrix))
