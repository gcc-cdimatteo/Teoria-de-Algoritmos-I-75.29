## Problem
Given $n$ items ${1, . . . , n}$, and each has a given nonnegative weight $w_i$ and a value $v_i$. Having a bound $W$, select a subset $S$ of the maximum total value so that  $w ≤ W$ and.
General case of [[Subset Sum]] where $v=1$.
## Solution
Being $O$ the optimal solution:
- If $n \notin O$: $OPT(n, W) = OPT(n − 1, W)$ ignoring item $n$
- If $n∈O$: $OPT(n,W)=v_n+OPT(n−1,W−w_n)$ using the remaining capacity
### Recurrence Relation
If $w < w_i$ then $OPT(i, w) = OPT(i − 1, w)$, otherwise $$OPT(i,w)=max(OPT(i−1,w),v_i+OPT(i−1,w−w_i))$$
### Algorithm
#### Iterative
```
Knapsack(n, W):
	Array M[0...n, 0...W]  
	Initialize M[0,w] = 0
	
	For i = 1,2,...,n
		For w = 0,...,W
			M[i,w] = max(Knapsack(i−1,w), vi + Knapsack(i−1,w−wi))
	    Endfor
	Endfor
	
	Return M[n, W]
```
#### Recursive
```
def mochila(valor, peso, N, W): 
	if N == 0: return 0
	if W < peso[N]: return mochila(valor, peso, N-1, W)
	return max(mochila(valor, peso, N-1, W), valor[N] + mochila(valor, peso, N-1, W - peso[N]))
```