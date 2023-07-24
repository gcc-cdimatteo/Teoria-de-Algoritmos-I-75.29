## Problem
Find the best possible match between two sequences of characters.
## Solution
In an optimal alignment $M$, at least one of the following is true:
1. $(m,n)∈M$
2. the $m^{th}$ position of $X$ is not matched
3. the $n^{th}$ position of $Y$ is not matched
### Recurrence Relation
The minimum alignment costs satisfy the following recurrence for $i ≥ 1$ and $j ≥ 1$:
$$OPT(i,j) = min[αx_iy_j +OPT(i−1,j−1),δ+OPT(i−1,j),δ+OPT(i,j−1)]$$
Moreover, $(i, j)$ is in an optimal alignment M$ for this subproblem if and only if the minimum is achieved by the first of these values.
### Algorithm
```
Alignment(X, Y):
	Array A[0...m,0...n]
	Initialize A[i, 0] = iδ for each i 
	Initialize A[0,j] = jδ for each j 
	
	For j = 1,...,n
		For i=1,...,m
			A(i,j) = min[αxiyj + Alignment(i−1,j−1), δ + Alignment(i−1,j), δ + Alignment(i,j−1)]
         Endfor
      Endfor

Return A[m, n]
```
## Explicación Martín
https://youtu.be/99WcT32kCK4?list=PLLfC2vEod54JgJkAvHFq72Fw2hNKLX55S&t=2721