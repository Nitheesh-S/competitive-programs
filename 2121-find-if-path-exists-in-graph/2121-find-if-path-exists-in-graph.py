class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
            self.tree = [i for i in range(n)]

            for edge in edges:
                start = self.root(edge[0])
                end = self.root(edge[1])

                self.tree[start] = end
            
            return self.root(source) == self.root(destination)
    
    def root(self, node):
        while self.tree[node] != node:
            node = self.tree[node]
        return node