## Problem
Directed graph $G=(V,E)$, with a designated start node $s$. Each edge $e$ has a length $l_e ≥0$, indicating the cost it takes to traverse $e$. For a path $P$, it's length $l(P)$ is the sum of the lengths of all edges in $P$.
###### Goal
Determine the shortest path from $s$ to every other node in the graph.
## Solution
The algorithm maintains a set $S$ of vertices $u$ for which we have determined a shortest-path distance $d(u)$ from $s$ (the “explored” part of the graph). 
Initially $S = {s}$, $d(s) = 0$ and $\forall u \in V, u \neq s, d(s) = ∞$.
For each node $v \in V−S$ it's determined the shortest path that can be constructed by traveling along a path through the explored part $S$ to some $u \in S$, followed by the edge $(u, v)$ where $d'(v) = min_{e=(u,v):u \in S} d(u) + l_e$ and $v$ is the node for which $d'(v)$ is minimized.
It's greedy because it forms the shortest new $s-v$ path possible from a path in $S$ followed by a single edge.
### Pseudocode
```
Let S be the set of explored nodes
For each u ∈ S, we store a distance d(u) 
Initially S = {s} and d(s) = 0  

While S ≠ V

	Select a node v ∉ S with at least one edge from S for which d'(v) = min_e d(u) + le is as small as possible

	Add v to S and define d(v) = d'(v) 

EndWhile
```
### Proof of Optimality
#incomplete 
### Time Complexity
#incomplete 