## Problem
[[Interval Scheduling]] in which each interval has a certain value (*weight*) and the goal is to accept a set of maximum value.
## Solution
Sort the requests in order of nondecreasing finish time.
Define $p(j)=i$ where $i$ is the leftmost interval that ends before $j$ begins.
![[Pasted image 20230724113525.png]]
### Recurrence Relation
$$OPT(0) = 0$$$$OPT(j) = max(v_j + OPT(p(j)), OPT(j − 1))$$
### Algorithm
```
Compute-Opt(j):
	If j = 0 then
		Return 0 
	Else If M[j] is not empty then
		Return M[j]
	Else
		M[j] = max(vj+Compute-Opt(p(j)), Compute-Opt(j−1))
		Return M[j]
	Endif
```
![[Pasted image 20230724114313.png]]
#### Looking for the Solution
```
Find-Solution(j): 
	If j = 0 then
		Output nothing
    Else
		If vj + M[p(j)] >= M[j−1] then  
			Output j together with the result of Find-Solution(p(j))
		Else  
			Output the result of Find-Solution(j−1)
		Endif
	Endif
```
### Time Complexity
Assuming the input intervals are sorted by their finish time $$O(n)$$