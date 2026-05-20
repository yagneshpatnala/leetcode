class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        seenA = set()
        seenB = set()
        ans = []

        for i in range(n):
            seenA.add(A[i])
            seenB.add(B[i])

            ans.append(len(seenA & seenB))

        return ans