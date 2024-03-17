class LDRMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.shape = (len(matrix), len(matrix[0]))

    def __add__(self, second_matrix):
        if not isinstance(second_matrix, LDRMatrix):
            raise ValueError("Wrong Input!")
            
        if second_matrix.shape != self.shape:
            raise ValueError("Wrong Input!")
            
        return LDRMatrix([
            [
                self.matrix[i][j] + second_matrix.matrix[i][j] 
                for j in range(self.shape[1])
            ] for i in range(self.shape[0])
        ])

    def __mul__(self, second_matrix):
        if not isinstance(second_matrix, LDRMatrix):
            raise ValueError("Wrong Input!")
        else:
            if second_matrix.shape != self.shape:
                raise ValueError("Wrong Input!")
                
        return LDRMatrix([
            [
                self.matrix[i][j] * second_matrix.matrix[i][j] 
                for j in range(self.shape[1])
            ] for i in range(self.shape[0])
        ])

    def __matmul__(self, second_matrix):
        if self.shape[1] != second_matrix.shape[0]:
            raise ValueError("Wrong Input!")
            
        return LDRMatrix([
            [
                sum(self.matrix[i][k] * second_matrix.matrix[k][j] for k in range(self.shape[1]))
                for j in range(self.shape[1])
            ] for i in range(self.shape[0])
        ])

    def __str__(self):
        max_element_len = max(3, max([
            max([
                len(str(self.matrix[i][j])) for j in range(self.shape[1])
            ]) for i in range(self.shape[0])
        ]) + 1)
        return "[" + '\n'.join(            
            [
                "[" + ''.join([f"{str(self.matrix[i][j]):>{max_element_len}}" for j in range(self.shape[1])]) + "]" 
                for i in range(self.shape[0])
            ]
        ) + "]"
    