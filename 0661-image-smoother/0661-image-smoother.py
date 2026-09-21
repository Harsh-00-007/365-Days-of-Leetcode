class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                
                # Traverse 3x3 neighborhood
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1
                            
                # Floor average 
                res[i][j] = total // count
                
        return res