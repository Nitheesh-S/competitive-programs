# print(edge, (a, b))
# print(self.tree, self.size)

# [0, 1] (0, 1)
# [0, 0, 2, 3, 4, 5] [2, 1, 1, 1, 1, 1]
# [0, 2] (0, 2)
# [0, 0, 0, 3, 4, 5] [3, 1, 1, 1, 1, 1]
# [3, 4] (3, 4)
# [0, 0, 0, 3, 3, 5] [3, 1, 1, 2, 1, 1]
# [3, 2] (3, 0)
# [0, 0, 0, 0, 3, 5] [5, 1, 1, 2, 1, 1]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.tree = [i for i in range(n)]
        self.size = [1] * n

        for edge in edges:
            a = self.root(edge[0])
            b = self.root(edge[1])
            if a == b:
                continue
            if self.size[a] < self.size[b]:
                self.tree[a] = b
                self.size[b] += self.size[a]
            else:
                self.tree[b] = a
                self.size[a] += self.size[b]
        
        return self.root(source) == self.root(destination)
    
    def root(self, node):
        while self.tree[node] != node:
            self.tree[node] = self.tree[self.tree[node]]
            node = self.tree[node]
        return node