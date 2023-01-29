import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a=np.array([[1]*m]*n)
        for i in range(1,n):
            for j in range(1,m):
                if i - 1 < 0 or j - 1 < 0 or type(a.shape[0]) is not int or type(a.shape[1]) is not int:
                    pass
                else:
                    a[i][j] = a[i - 1][j] + a[i][j - 1]
        
        return int(a[n-1][m-1])
