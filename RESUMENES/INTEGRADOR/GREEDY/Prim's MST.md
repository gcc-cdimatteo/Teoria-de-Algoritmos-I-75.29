Use [[Dijkstra Shortest Path in a Graph]].
Start with a root node $s$ and try to greedily grow a tree from $s$ outward. 
At each step, add the node that can be attached as cheaply as possibly to the partial tree: maintain a set $S ⊆ V$ on which a spanning tree has been constructed (initially $S = \{s\}$); in each iteration, grow $S$ by one node adding $v$ that minimizes the *attachment cost* and including the edge $e$ that achieves this minimum in the spanning tree.
### Pseudocode
#incomplete 
### Proof of Optimality
#incomplete 
### Time Complexity
#### Adjacency Matrix, Searching
$$O(V^2)$$
#### Binary Heap & Adjacency List
$$O(V \log{V} + E \log{V})$$
#### Extra Material
https://www.youtube.com/watch?v=71UQH7Pr9kU
https://www.youtube.com/watch?v=Yldkh0aOEcg