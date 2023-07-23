## Problem
Set of intervals $I = \{I_1,I_2,...,I_n\}$, set of resources $R = \{1,2,...,d \}$. Those intervals which pass over a common point on the time-line must be scheduled on a different resource, so the whole instance needs at least $d$ resources.
###### Goal
Schedule all intervals using the minimum possible number of resources.
## Solution
Having that the number of resources needed is at least the depth of the set of intervals, the greedy algorithm will schedule all intervals using $d$ resources.
### Pseudocode
```
Sort the intervals by their start times
Let I1, I2, . . . , In denote the intervals

For j = 1,2,3,...,n

	 For each Ii before Ij 
		If Ii overlaps Ij
			Exclude the label of Ii from consideration for Ij
	Endfor  

	If there is any label that has not been excluded
		Assign the first nonexcluded label to Ij
	Else
		Leave Ij unlabeled
	Endif

Endfor
```
### Proof of Optimality
###### no interval ends up unlabeled
Consider $I_j$ and $t$ intervals earlier that overlap it. As the $t+1$ all pass over a common point on the time-line, and so $t+1 \leq d \implies t \leq d-1$, at least one of the $d$ labels is not excluded by the set of $t$ intervals and can be assigned to $I_j$.
###### no two overlapping intervals are assigned the same label
If any two intervals $I$ & $I'$ overlap, and $I$ precedes $I'$. When $I'$ is considered by the algorithm, $I$ is in the set of intervals whose labels are excluded from consideration so the algorithm will not assign to $I'$ the label that it used for $I$.
###### minimum possible number of labels
The greedy algorithm schedules every interval on a resource, using a number of resources equal to the depth of the set of intervals which is the optimal number of resources needed.
### Time Complexity
Sort the $n$ requests in order of *starting time* $$O(n\log{n})$$
Iterate for each interval
$$O(n)$$
Iterate for each preceded interval
$$O(n)$$
Total complexity
$$O(n^2)$$