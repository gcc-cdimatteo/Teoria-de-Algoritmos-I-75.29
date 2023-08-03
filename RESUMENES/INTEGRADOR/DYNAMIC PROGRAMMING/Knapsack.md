#NPC
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
## Approximation
Take as input the weights and values defining the problem and an extra parameter $\epsilon$ (the desired precision). 
Find a subset $S$ whose total weight does not exceed $W$, with value $\sum_{i \in S}{v_i}$ at most a $(1 + \epsilon)$ factor below the maximum possible (optimal solution).
The algorithm will run in polynomial time for any fixed choice of $\epsilon > 0$; however, the dependence on $\epsilon$ will not be polynomial. 
==The algorithm is a polynomial-time approximation scheme.==
Algorithms that depend on the values in a pseudo-polynomial way can often be used to design polynomial-time approximation schemes.
### Algorithm
![[Pasted image 20230803144051.png]]
##### Complexity
$$O(n^3\epsilon^{-1})$$
![[Pasted image 20230803144404.png]]
##### Complexity
$$O(n^2v*)$$
#### Bound
$$\sum_{i \in S*}{v_i} \leq \sum_{i \in S}{v_i+nb \leq(1+\epsilon)}\sum_{i \in S}{v_i}$$