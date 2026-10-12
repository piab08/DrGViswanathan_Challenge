class Solution:
    def getRow(self, rowIndex):
        res = [[1]]

        for i in range(1, rowIndex + 1):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = res[-1][j - 1] + res[-1][j]

            res.append(row)

        return res[rowIndex]
