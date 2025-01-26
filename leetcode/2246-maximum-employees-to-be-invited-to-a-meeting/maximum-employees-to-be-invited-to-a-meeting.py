class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        length = [0] * n

        for x in favorite:
            indegree[x] += 1
        
        q = deque([i for i in range(n) if indegree[i] == 0])
        while q:
            cur  = q.popleft()
            nxt = favorite[cur]
            indegree[nxt] -= 1
            length[nxt] = max(length[nxt], length[cur] + 1)
            if indegree[nxt] == 0:
                q.append(nxt)

        small_ring = 0
        big_ring = 0

        for i in range(n):
            if indegree[i] > 0:
                size = 1
                indegree[i] -= 1
                nxt = favorite[i]
                while nxt != i:
                    indegree[nxt] -= 1
                    size += 1
                    nxt = favorite[nxt]
                if size == 2:
                    small_ring += length[i] + length[favorite[i]] + 2
                else:
                    big_ring = max(big_ring, size)
        
        return max(small_ring, big_ring)
