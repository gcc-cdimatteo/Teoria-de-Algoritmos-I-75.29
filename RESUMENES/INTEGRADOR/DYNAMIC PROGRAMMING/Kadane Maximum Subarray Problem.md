## Problem
Finde a contiguous subarray with the largest sum, within a given one-dimensional array of numbers.
## Solution
### Recurrence Relation
$$OPT(arr,0)=arr[0]$$
$$OPT(arr,i) = \max(arr[i], arr[i]+OPT(i-1))$$
### Time Complexity
![[Pasted image 20230724155717.png]]