import time
import test

class Solution:     

    def sumOfDistancesInTree(self, n, edges):
        
        self.n = n

        """Create tree with a dictionary where de key is de number of node and de value is a
          set of nodes that has a edge with it"""
        
        tree = dict([(i,set()) for i in range(n)])
        for e in edges:
          tree[e[0]].add(e[1])
          tree[e[1]].add(e[0])

        #Create dictionaries to allocate the number of nodes in subtree and distances from each node
        self.dist = dict([(i,0) for i in range(len(tree))])
        self.numNodes = dict([(i,1) for i in range(len(tree))])
        self.depthFirst(0,None,tree)
        self.dist[0] = sum(self.dist.values())
        self.depthFirstForNodes(0,None,tree,self.dist[0])
        return self.dist.values()

    def depthFirst(self,node,parent,tree):

      for e in tree[node]:

        #Check if the is a cycle in order to avoid it
        if e != parent:   

          #Allocate de distance beetween node to each node from tree
          self.dist[e] = self.dist[node] + 1    
          self.depthFirst(e,node,tree)

          #Increment number of nodes in subtree
          self.numNodes[node] += self.numNodes[e]
          
          
      

    #Create a fuction to get distances to all nodes from all nodes
    def depthFirstForNodes(self,node,parent,tree,dist):
       
       for e in tree[node]:
        if e != parent:
           
           #Get number of added distances for nodes out of the subtree e
           dist_added = dist + (self.n - self.numNodes[e]) 

           #Get number of substracted distances for nodes in subtree e        
           dist_substracted = self.numNodes[e]

           #Get the total change of distances in node e
           self.dist[e] = dist_added - dist_substracted

           #Go to child nodes of e and get distances considering new sum of distances from node e
           self.depthFirstForNodes(e, node, tree, self.dist[e]) 

   
start = time.time()

solution = Solution()

print(solution.sumOfDistancesInTree(10,test.test10))

end = time.time()

print("Execution time:", "{:.10f}".format(end-start), "seconds")