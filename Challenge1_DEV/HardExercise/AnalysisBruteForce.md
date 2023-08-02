# **For this solution we consider:**


**In time complexity ⏲:**

1. We travese all the egdes given in input and storage in dict, it takes
$O(n)$ where n is number of edges.

2. We travese for all nodes in tree, then it takes $O(n)$ as well.

3. Create dictionary with distance from current node to other, it just take one operation,
then $O(1)$

4. For each one node executes *depthFirst* fuction.

    4.1 We traverse each element in adjacent list of node, thus, it takes in
    worst case all nodes are conected with one $O(n)$

    4.2 Check if the current node is diferent to parent node, just to avoid cycles.
    It just takes one operation, then $O(1)$

    4.3 Increment distance from one to others taking into account the distance from parent.
    We use dictionary, then it just takes one operation and it takes $O(1)$

    4.4 Use recursively fuction with each child node. Fuction will traverse 
    all the child nodes of the node, but it considers already visited nodes, so 
    in fact, DFS will takes $O(n)$ 

Considering all above,

$$time = O(n) + O(n) + O(1) * (O(n) + O(1) + O(1) + O(n))$$
$$time = O(n) * O(n) = O(n^2)$$


**In space complexity 🖥:**

  We use a dictionary to allocate each node with their childs, then it takes $O(n)$
  we use a array to insert sum of distance for each node.

then, considering

$$space = O(n) + O(n) = 2O(n) = O(n)$$