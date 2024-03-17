import numpy as np
from HashLDRMatrix import LDRMatrix

np.random.seed(0)
A = LDRMatrix([
    [0, 2], [3, 1]
])
C = LDRMatrix([
    [1, 1], [2, 2]
])

B = LDRMatrix([
    [-2, -1], [1, 5]
])

D = LDRMatrix([
    [-2, -1], [1, 5]
])

assert not (A.matrix == C.matrix)
assert hash(A) == hash(C)
assert B.matrix == D.matrix

A_dot_B = A @ B
LDRMatrix.cache = {}
C_dot_D = C @ D
LDRMatrix.cache = {}

assert A_dot_B.matrix != C_dot_D.matrix
assert (A @ B).matrix == (C @ D).matrix

with open("artifacts/3.3/A.txt", "w") as file:
    file.write(str(A))

with open("artifacts/3.3/B.txt", "w") as file:
    file.write(str(B))

with open("artifacts/3.3/C.txt", "w") as file:
    file.write(str(C))

with open("artifacts/3.3/D.txt", "w") as file:
    file.write(str(D))
    
with open("artifacts/3.3/AB.txt", "w") as file:
    file.write(str(A_dot_B))
    
with open("artifacts/3.3/CD.txt", "w") as file:
    file.write(str(C_dot_D))

with open("artifacts/3.3/hash.txt", "w") as file:
    file.write(f"Real hash A@B {hash(A_dot_B)}, cached hash A@B {hash(A @ B)}\n")
    file.write(f"Real hash C@D {hash(C_dot_D)}, cached hash C@D {hash(C @ D)}")