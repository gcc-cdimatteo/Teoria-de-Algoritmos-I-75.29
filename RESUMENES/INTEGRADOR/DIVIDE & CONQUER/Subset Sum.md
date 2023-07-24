## Problem
Given $n$ items ${1, . . . , n}$, and each has a given nonnegative weight $w_i$. Having a bound $W$, select a subset $S$ of the items so that  $w ≤ W$ and $\sum_{i\in S}{w_i}$ is as large as possible.
## Solution
Being $O$ the optimal solution:
- If $n \notin O$: $OPT(n, W) = OPT(n − 1, W)$ ignoring item $n$
- If $n∈O$: $OPT(n,W)=w_n+OPT(n−1,W−w_n)$ using the remaining capacity
### Recurrence Relation
If $w < w_i$ then $OPT(i, w) = OPT(i − 1, w)$, otherwise $$OPT(i,w)=max(OPT(i−1,w),w_i +OPT(i−1,w−w_i))$$
### Algorithm
```
Subset-Sum(n, W):
	Array M[0...n, 0...W]  
	Initialize M[0,w] = 0
	
	For i = 1,2,...,n
		For w = 0,...,W
			M[i,w] = max(Subset-Sum(i−1,w), w_i + Subset-Sum(i−1,w−wi))
	    Endfor
	Endfor
Return M[n, W]
```