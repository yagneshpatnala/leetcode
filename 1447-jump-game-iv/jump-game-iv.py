from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        
        graph = defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        queue = deque([0])
        visited = set([0])
        steps = 0

        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()

                
                if index == n - 1:
                    return steps

                
                neighbors = graph[arr[index]] + [index - 1, index + 1]

                for next_index in neighbors:
                    if 0 <= next_index < n and next_index not in visited:
                        visited.add(next_index)
                        queue.append(next_index)

            
                graph[arr[index]].clear()

            steps += 1

        return -1