# **For this solution we consider:**

**In time complexity ⏲:**

1. We travese all the egdes given by input and storage in dict, it takes
$O(n)$ where $n$ is number of edges.

2. Create dictionary with distance from currect node to other, it just takes one operation,
then $O(1)$.

3. Create dictionary with number of nodes in each subtree, it just takes one operation,
then $O(1)$.

4. For root node executes *depthFirst* fuction.

    4.1 We traverse each element in adjacent list of node, thus, it takes in
    worst case all nodes are conected with one $O(n)$

    4.2 Check if the current node is different to parent node, to avoid cycles.
    It just takes one operation, then $O(1)$

    4.3 Increment distance from one to others taking into account the distance from parent.
    We use dictionary, then it just takes one operation $O(1)$

    4.4 Use recursively fuction with each child node. Fuction will traverse 
    all the child nodes of the node, but it considers already visited nodes, so 
    in fact, DFS will takes $O(n)$ 

5. Get the sum of distances of root node, it takes $O(n)$

6. Execute *depthFirstForNodes* fuction.

    6.1 We traverse all nodes in tree then $O(n)$.

    6.2 We calculate the number of nodes that we need to add by 1 considering 
    parent sum of distances. It just takes one operation, then $O(1)$.

    6.3 We calculate the number of nodes that we need to substract by 1 considering
    parent sum of distances. It just takes one operation, then $O(1)$.

    6.4 We operate number of added distances minus number of substracted distances. It
    just takes one operation, then $O(1)$.

    6.5 Use recursively fuction with each child node, with his sum of distance. It takes $O(n)$.

Considering all above,

$$time = O(n) + O(1) + O(1) + O(n) + O(n) + O(n)$$

$$time = O(n)$$


In space complexity 🖥:

  - We use a dictionary to allocate each node with their childs, then it takes $O(n)$
  - We use a array to insert sum of distance for each node, then it takes $O(n)$
  - We use a dictionary to allocate sum of distances for each nodes, then it takes $O(n)$
  - We use a dictionary to allocate number of nodes in subtree, then it takes $O(n)$


then, Considering

$$space = O(n) + O(n) + O(n) + O(n) = O(n)$$