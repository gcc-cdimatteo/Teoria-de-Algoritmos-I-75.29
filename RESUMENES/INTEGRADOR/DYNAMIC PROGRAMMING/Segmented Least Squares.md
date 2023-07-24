## Problem
Given a set of $n$ points in $P$, and a line $L$ defined by the equation $y=ax+b$, the error of $L$ is the sum of its squared distances to the points in $P$: $$Error(L,P)=\sum_{i=1}^{n}{(y_i − ax_i − b)^2}$$
The goal is to fit the points well, using as few lines as possible by identifying a few points in the sequence at which a discrete change occurs.
## Solution
For each segment $S$ in our partition of $P$, compute the line minimizing the error with respect to the points in $S$, according to the penalty of a partition that is defined to be a sum of:
1. The number of segments into which $P$ is partitioned, given by multiplying $C > 0$
2. For each segment, the error value of the optimal line through that segment.
### Recurrence Relation
For the subproblem on the points $p_1, . . . , p_j$, $$OPT(j) = \min_{1≤i≤j}{(e_{i,j} + C + OPT(i − 1))}$$and the segment $p_i , . . . , p_j$ is used in an optimum solution for the subproblem if and only if the minimum is obtained using index $i$.
### Algorithm
```
Segmented-Least-Squares(n): 
	Array M[0...n]  
	Set M[0] = 0  

	For all pairs i ≤ j
		Compute the least sqares error eij for the segment pi,...,pj
	Endfor

	For i = 1,2,...,n
		M[i] = inf
		For j = 1,2,...,n
			M[j] = min(eij + C + OPT(i − 1))
		Endfor
	Endfor
	
	Return M[n]
```
### Time Complexity
Because of computing the error between a pair of points is $O(n)$, the total running time is $$O(n^3)$$