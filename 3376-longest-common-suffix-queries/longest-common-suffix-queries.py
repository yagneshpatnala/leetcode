class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1


class Solution:
    def stringIndices(self, wordsContainer, wordsQuery):

        root = TrieNode()
        best = 0
        for i in range(len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best]):
                best = i

        root.index = best
        for i, word in enumerate(wordsContainer):
            node = root

            for ch in word[::-1]:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                if node.index == -1 or len(wordsContainer[i]) < len(wordsContainer[node.index]):
                    node.index = i

        ans = []
        for word in wordsQuery:
            node = root

            for ch in word[::-1]:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.index)

        return ans