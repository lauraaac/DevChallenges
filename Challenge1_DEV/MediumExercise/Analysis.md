# **For this solution we consider:**

**In time complexity ⏲:**

1. Create a function that traverse all the grid, it takes $O(n^2)$ in worst case

2. We match each element in grid with first element in word, it just takes
one operation, then $O(1)$

3. Create a auxiliar board, then $O(1)$

4. We use fuction "depthSearch", their time complexity is:

    **4.1.** It match lenght of world with a instanciated counter that starts in 0 it takes just one operation, then $O(1)$
    
    **4.2** Validate limits of board, there are 4 operacion, each takes $O(1)$, then $4*O(1) = O(1)$
    
    **4.3** Checks if there is a match with element of board and word and if the element haven't been selected before, there are 2 operation, each takes $O(1)$, then $2*O(1) = O(1)$

    **4.4** Update auxiliar board in place where was found letter, then $O(1)$
    
    **4.5** Increment counter by 1. takes one operation, then $O(1)$

    **4.6** Use recursively depthSearch but moving up, down, right and left by 1 If we use the worst case where all the paths match, then time will be $O(4^l)$ where $l$ is the number of letters in word.


Considering all above,

  $$time = O(n^2) + O(1) + O(1) * (O(1) + O(1) + O(1) + O(1) + O(1) + O(4^l))$$

  $$time = O(n^2) * O(4^{l}) = O(n^2*4^l)$$


---


**In space complexity 🖥:**

We use an auxiliar board with size n X n in worst case, 
then
$$O(n^2)$$ also we
use a counter $$O(1)$$ 

then, Considering

$$space = O(n^2) + O(1) = O(n^2)$$