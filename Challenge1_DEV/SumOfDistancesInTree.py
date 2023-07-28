class Solution:     

    def sumOfDistancesInTree(self, n, edges):
        
        self.n = n

        #Create tree with a dictionary where de key is de number of node and de value is a set of nodes that has a edge with it.
        #The set avoid duplicates edges
        tree = dict([(i,set()) for i in range(n)])
        for e in edges:
          tree[e[0]].add(e[1])
          tree[e[1]].add(e[0])

        #We travel the tree and sum distances using DFS for all nodes
        #sumDist = []

        #Create dictionaries to allocate the number of nodes in subtree and distances from each node
        self.dist = dict([(i,0) for i in range(len(tree))])
        self.numNodes = dict([(i,1) for i in range(len(tree))])
        self.depthFirst(0,None,tree)
        self.dist[0] = sum(self.dist.values())
        self.depthFirstForNodes(0,None,tree, self.dist[0])
        return self.dist

    def depthFirst(self,node,parent,tree):

      #Travel for each node adjacent list
      for e in tree[node]:

        #Check if the is a cycle in order to avoid it
        if e != parent:   

          #Allocate de distance beetween node to each node from tree
          self.dist[e] = self.dist[node] + 1    
          self.depthFirst(e,node,tree)

          #Increment number of nodes in subtree
          self.numNodes[node] += self.numNodes[e]
          
          
      

    def depthFirstForNodes(self,node,parent,tree,dist):
       
       for e in tree[node]:

        if e != parent:
           
           dist_added = dist + (self.n - self.numNodes[e])         
           dist_substracted = self.numNodes[e]
           self.dist[e] = dist_added - dist_substracted

           print("node", e)
           print("parent", node)
           print("dist", dist)
           print("added", dist_added)
           print("subs", dist_substracted)
           self.depthFirstForNodes(e, node, tree, self.dist[e]) 
          

solution = Solution()

print(solution.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))
