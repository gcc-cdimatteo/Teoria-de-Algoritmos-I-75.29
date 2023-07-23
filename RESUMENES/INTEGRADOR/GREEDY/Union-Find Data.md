#DataStructure needed to implement [[Kruskal's MST]] efficiently.
## Description
Given a graph $G=(V,E)$, considering the edge $e=(v,w)$ it has to be found efficiently the identities of the connected components containing $v$ and $w$.
## Implementation
1. *MakeUnionFind(S)*: for a set $S$ will return a Union-Find data structure on set $S$ where all elements are in separate sets in $O(n)$.
2. *Find(u)*: for an element $u ∈ S$, return the name of the set containing $u$ in $O(\log{n})$.
3. *Union(A,B)*: for two sets $A$ and $B$, change the data structure by merging them into a single set in $O(\log{n})$.
![[Untitled Diagram.drawio.png]]