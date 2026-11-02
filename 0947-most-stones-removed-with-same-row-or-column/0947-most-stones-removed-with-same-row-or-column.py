class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        adj = defaultdict(list)

        # Use ~c to distinguish a column from a row, and similarly, use ~r to distinguish a row from a column.
        for r, c in stones:
            adj[r].append(~c)
            adj[~c].append(r)

        visit = set()

        def dfs(x):
            visit.add(x)
            for y in adj[x]:
                if y not in visit:
                    dfs(y)
        
        sm = 0
        for r, c in stones:
            if r not in visit:
                dfs(r)  # Perform DFS from the row, which will also cover the column connections
                sm += 1
        
        return len(stones) - sm