# **For this solution we consider:**

**In time complexity ⏲:**

1. We will traverse each element of array with lenght $n$, then $O(n)$

2. We will create a subarray from array start to element an
other subarray from element + 1 to end to array, it uses specific location
of array, then convert in substring time will be $O(1)$

3. For both subarrays we will cast to set. In python it takes $O(n)$, so we have
$2*O(n) = O(n)$

4. We store the number of repeated elements in array, it just takes one
operation, then $O(1)$

5. We add to solution array. It just takes one operation, then $O(1)$

Considering all above,

$$time = O(n) * O(n) + O(1) + O(1) + O(1)$$


---


**In space complexity 🖥:**

We use one array on lenght n to insert each operation, then we use
2 subarrays wich $len(subarray1) = n - len(subarray2)$ , so worst case
will be n.

then, Considering

$$space = O(n)$$