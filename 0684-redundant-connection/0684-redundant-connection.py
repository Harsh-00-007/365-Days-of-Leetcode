class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = list(range(n + 1))
        rank = [1] * (n + 1)

        def find(node: int) -> int:
            # Path compression
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(u: int, v: int) -> bool:
            root_u = find(u)
            root_v = find(v)

            # If both nodes share the same root, an edge between them forms a cycle
            if root_u == root_v:
                return False

            # Union by rank
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []