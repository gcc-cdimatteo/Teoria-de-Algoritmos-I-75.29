## Problem
A set of paths is *edge-disjoint* if their edge sets are disjoint: no two paths share an edge, though multiple paths may go through some of the same nodes.
Given a graph $G = (V, E)$ with two distinguished nodes $s, t ∈ V$, find the maximum number of *edge-disjoint* $s-t$ paths in $G$.
## Solution
### Directed Graph
Define a flow network in which $s$ and $t$ are the source and sink and with a capacity of 1 on each edge. Use Ford-Fulkerson in the new network to find the maximum flow. **If there are $k$ edge-disjoint paths in a directed graph $G$ from $s$ to $t$, then the value of the maximum $s-t$ flow in $G$ is at least $k$.**
### Undirected Graph
Replace each undirected edge $(u, v)$ in $G$ by two directed edges $(u, v)$ and $(v, u)$, and in create a directed version $G'$ of $G$. Delete the edges into $s$ and out of $t$, since they are not useful. Use the Ford-Fulkerson Algorithm in the resulting directed graph.
![[Untitled Diagram-Copy of Page-1.png]]
### Time Complexity
Same as [[Ford-Fulkerson Maximum-Flow#Time Complexity]]!