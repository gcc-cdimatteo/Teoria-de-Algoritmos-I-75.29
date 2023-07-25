## Problem
Given a flow network, find a flow of maximum possible value.
## Solution
Start with zero flow: $f (e) = 0$ for all $e$.
Try to increase the value of $f$ by pushing flow along a path from $s$ to $t$, up to the limits imposed by the edge capacities.
Push forward on edges with leftover capacity, and backward on edges that are already carrying flow, to divert it in a different direction.
### Residual Graph
Represents the remaining available capacity for flow on each edge of the original flow network. It is used to identify potential paths where additional flow can be pushed from the source to the sink.
Given a flow network $G$, and a flow $f$ on $G$, the residual graph $G_f$ is defined by:
- for each node on $G$, include it in $G_f$
- **forward edge**: for each edge $e=(u,v)$ on $G$ for which $f(e)<c_e$, include the edge $e = (u, v)$ in $G_f$, with a capacity of $c_e − f (e)$
- **backward edge**: for each edge $e=(u,v)$ on $G$ for which $f(e)>0$, include the edge $e' = (v, u)$ in $G_f$, with a capacity of $f(e)$
### Augmenting Paths in the Residual Graph
Path in the residual graph that connects the source to the sink and has available capacity for additional flow.
```
augment(f, P):
	Let b = bottleneck(P,f)
	For each edge (u,v) ∈ P
		If e = (u,v) is a forward edge then 
			increase f(e) in G by b
		Else ((u, v) is a backward edge) 
			decrease f(e) in G by b
		Endif
	Endfor
	
	Return f
```
### Algorithm
```
Max-Flow:
	Initially f(e) = 0 for all e in G
	Create the residual graph Gf for G

	While there is an s-t path in the residual graph Gf
		Let P be a simple s-t path in Gf  
		f' = augment(f, P)
		Update f to be f'
		Update Gf to be Gf'
	Endwhile
	
	Return f
```
### Time Complexity
With Edmonds-Karp theorem, using BFS the algorithm always works in $$O(V*E^2)$$