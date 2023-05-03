class Field:
    def __init__(self):
        self.matrix = [[None for _ in range(3)] for _ in range(3)]
        
    def set_element(self, row, col, value):
        self.matrix[row][col] = value
        
    def is_element_in_row(self, value, row_number):
        return value in self.matrix[row_number]
    
    def is_element_in_col(self, value, col_number):
        return any(self.matrix[i][col_number] == value for i in range(3))
    

