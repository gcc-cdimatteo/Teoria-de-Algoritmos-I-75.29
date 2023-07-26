## Problem
A *bipartite graph* $G = (V , E)$ is an undirected graph whose node set can be partitioned as $V = X ∪ Y$, with the property that every edge $e ∈ E$ has one end in $X$ and the other end in $Y$. 
A *matching* $M$ in $G$ is a subset of the edges $M ⊆ E$ such that each node appears in at most one edge in $M$. 
##### Goal
Find a matching in $G$ of largest possible size.
## Solution
1. Clone graph $G$ in $G'$
2. Direct all edges in $G$ from $X$ to $Y$
3. Add a node $s$, and an edge $(s,x)$ from $s$ to each node in $X$
4. Add a node $t$, and an edge $(y,t)$ from each node in $Y$ to $t$
5. Give each edge in $G'$ a capacity of 1
6. Compute a maximum $s-t$ flow in $G'$
![[Pasted image 20230725101939.png]]
### Time Complexity
Same as [[Ford-Fulkerson Maximum-Flow#Time Complexity]]!