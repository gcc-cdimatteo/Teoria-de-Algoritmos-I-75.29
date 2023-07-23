## Problem
Given a sequence of $n$ numbers $a_1,..., a_n$, define a measure which describes how far is the list from being in ascending order. The value of the measure should be $0$ if $a_1 < a_2 < ... < a_n$, and increase as the numbers become more scrambled.
![[Pasted image 20230723193251.png]]
## Solution
Set $m = [n/2]$ and divide the list into the two pieces: $a_1,...,a_m$ and $a_{m+1},...,a_n$. 
First count the number of inversions in each of the two halves separately. Then count the number of inversions $(a_i, a_j)$, where the two numbers belong to different halves. These first-half/second-half inversions are the pairs $(a_i, a_j)$, where $a_i$ is in the first half, $a_j$ is in the second half, and $a_i > a_j$.
Recursively sort the numbers in the two halves and count the inversion.
With two sorted lists $A$ and $B$ containing the first and second halves, produce a single sorted list $C$ from their union, while also counting the number of pairs $(a, b)$ with $a ∈ A$, $b ∈ B$, and $a > b$.
![[Pasted image 20230723201056.png]]
### Algorithm
```
Merge-and-Count(A,B)  

Maintain a Current pointer into each list, initialized to point to the front elements

Maintain a variable Count for the number of inversions, initialized to 0  

While both lists are nonempty:
	Let ai and bj be the elements pointed to by the Current pointer
	Append the smaller of these two to the output list  
	If bj is the smaller element then
		Increment Count by the number of elements remaining in A 
	Endif

	Advance the Current pointer in the list from which the smaller element was selected

EndWhile

Once one list is empty, append the remainder of the other list to the output

Return Count and the merged list
```
### Pseudocode
```
Sort-and-Count(L)  
	If the list has one element then
		there are no inversions
	Else

	Divide the list into two halves:  
		A contains the first [n/2] elements  
		B contains the remaining [n/2] elements

	(rA, A) = Sort-and-Count(A)
	(rB, B) = Sort-and-Count(B)
	(r, L) = Merge-and-Count(A,B)

	Endif
	
	Return r = rA + rB + r, and the sorted list L
```