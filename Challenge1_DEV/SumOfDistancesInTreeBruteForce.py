class Solution:     

    def sumOfDistancesInTree(self, n, edges):

        #Create tree with a dictionary where de key is de number of node and de value is a set of nodes that has a edge with it.
        #The set avoid duplicates edges
        tree = dict([(i,set()) for i in range(n)])
        for e in edges:
          tree[e[0]].add(e[1])
          tree[e[1]].add(e[0])

        #We travel the tree and sum distances using DFS for all nodes
        sumDist = []
        for node in tree:
          self.dist = dict([(i,0) for i in range(len(tree))])
          self.depthFirst(node,None,tree)
          sumDist.append(sum(self.dist.values()))
        return sumDist

    def depthFirst(self,node,parent,tree):

      for e in tree[node]:
        if e != parent:
          self.dist[e] = self.dist[node] + 1
          self.depthFirst(e,node,tree);