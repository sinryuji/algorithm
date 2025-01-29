class Solution:
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, a, b):
        a = self.find(parent, a)
        b = self.find(parent, b)

        if a == b:
            return False
        else:
            if a < b:
                parent[b] = a
            else:
                parent[a] = b
            return True

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        for edge in edges:
            if not self.union(parent, edge[0], edge[1]):
                return edge
        return []