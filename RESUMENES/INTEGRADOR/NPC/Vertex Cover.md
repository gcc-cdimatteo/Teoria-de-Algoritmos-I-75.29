#NPC
Given a graph $G = (V, E)$, a set of nodes $S ⊆ V$ is a vertex cover if every edge $e ∈ E$ has at least one end in $S$.
## Decision Problem
Given a number $k$, does $G$ contain a vertex cover of size at most $k$?
## Greedy Approximation by Pricing Method
The weight $w_i$ of the vertex $i$ is the cost for using $i$ in the cover. Each edge $e$ is a separate agent who is willing to pay something to the node that covers it. 
The algorithm will not only find a vertex cover $S$, but also determine prices $p_e ≥ 0$ for each edge $e ∈ E$, so that if each one pays the price $p_e$, this will in total approximately cover the cost of $S$.
A price $p_e$ is fair if, for each vertex $i$, the edges adjacent to $i$ do not have to pay more than the cost of the vertex: $$\sum_{e(i,j)}{p_e \leq w_i}$$
Each edge $e=(i,j)$ for which $i$ and $j$ are not tight, will pay the minimum price of $i$ or $j$ in order to pay a fair price.
For any vertex cover $S*$, and any nonnegative and fair prices $p_e$ $$\sum_{e \ in E}{p_e \leq w(S*)}$$

### Algorithm
Let be a node $i$ tight if $\sum_{e=(i,j)}{p_e=w_i}$
```
Vertex-Cover-Approx(G, w):
	Set pe = 0 for all e ∈ E

	While there is an edge e = (i, j) such that neither i nor j is tight:
		Select such an edge e
		Increase pe without violating fairness 
	EndWhile

Let S be the set of all tight nodes 

Return S
```
![[Pasted image 20230803102735.png]]
#### Bound
$$w(S) \leq 2\sum_{e \in E}{p_e} \leq 2w(S*)$$