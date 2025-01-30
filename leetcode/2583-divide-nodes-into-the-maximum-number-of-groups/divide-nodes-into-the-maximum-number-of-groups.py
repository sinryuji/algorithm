class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:  
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            x, y = find(x), find(y)
            if x < y:
                parent[y] = x
            else:
                parent[x] = y

        def bfs(start):
            q = deque()
            layer_seen = [-1] * n
            q.append(start)
            layer_seen[start] = 0
            deepest_layer = 0

            while q:
                num_of_nodes_in_layer = len(q)
                for _ in range(num_of_nodes_in_layer):
                    cur = q.popleft()
                    for nxt in graph[cur]:
                        if layer_seen[nxt] == -1:
                            layer_seen[nxt] = deepest_layer + 1
                            q.append(nxt)
                        else:
                            if layer_seen[nxt] == deepest_layer:
                                return -1
                deepest_layer += 1
            return deepest_layer

        parent = [i for i in range(n)]
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1) 
            union(a - 1, b - 1)
        
        d = {}

        for node in range(n):
            number_of_groups = bfs(node)

            if number_of_groups == -1:
                return -1
            root = find(node)
            d[root] = max(d.get(root, 0), number_of_groups)

        return sum(d.values())