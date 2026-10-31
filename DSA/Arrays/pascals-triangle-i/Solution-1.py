class Solution:
    def pascalTriangleI(self, r, c):

        result = [[1]]

        for i in range(r-1):
            temp = [0] + result[-1] + [0]
            current = []

            for j in range(len(result[-1]) + 1):
                current.append(temp[j] + temp[j+1])
            
            result.append(current)
        
        return result[r-1][c-1]