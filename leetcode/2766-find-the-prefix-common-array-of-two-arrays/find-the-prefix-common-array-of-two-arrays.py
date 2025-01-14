class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s, t, result = set(), 0, []
        for i in range(len(A)):
            if A[i] in s:
                t += 1
            else:
                s.add(A[i])
            if B[i] in s:
                t += 1
            else:
                s.add(B[i])
            result.append(t)
        return result