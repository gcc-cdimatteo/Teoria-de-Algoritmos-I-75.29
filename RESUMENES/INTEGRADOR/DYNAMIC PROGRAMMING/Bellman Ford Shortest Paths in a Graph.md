## Problem
Given a directed graph $G=(V,E)$ with a start node $s$, find a shortest path from $s$ to $t$ when there are negative edge costs but no negative cycles.
## Solution
Let’s use $OPT(i, v)$ to denote the minimum cost of a $v-t$ path using at most $i$ edges.
### Recurrence Relation
$$OPT(v) = \min(dist(v), dist(u) + w(u, v))$$
### Algorithm
```
Shortest-Path(G, s, t):
	n = number of nodes in G  
	Array M[0...n−1, V]
	
	Define M[0,t] = 0 and M[0,v] = ∞

	For i = 1,...,n-1
		For v ∈ V in any order  
			Compute M[i, v] using the recurrence (6.23)
		Endfor
	Endfor

	Return M[n − 1, s]
```
![[Pasted image 20230724183746.png]]
![[Pasted image 20230724183800.png]]
### Time Complexity
$$O(|V|*|E|)$$