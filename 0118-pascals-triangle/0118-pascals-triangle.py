class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []
        for i in range(num_rows):
            if i == 0:
                triangle.append([1])
                continue
            
            next_row = []
            for j in range(len(triangle[-1]) - 1):
                next_row.append(triangle[-1][j] + triangle[-1][j+1])

            triangle.append([1] + next_row + [1])
        
        return triangle