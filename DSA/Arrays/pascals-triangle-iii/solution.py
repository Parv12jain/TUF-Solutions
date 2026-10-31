class Solution:
    def pascalTriangleIII(self, n):
        result = [[1]]

        for i in range(n - 1):
            temp = [0] + result[-1] + [0]
            current = []

            for j in range(len(result[-1]) + 1):
                current.append(temp[j] + temp[j+1])
            result.append(current)
        
        return result
            