## Problem
Given $n$ points in the plane $P$, find the pair that is closest together.
## Solution
Sort all the points in $P$ by $x$ and $y$, producing lists $P_x$ and $P_y$.
Define $Q$ to be the set of points in the first $[n/2]$ positions of $P_x$ (the “left half”) and $R$ to be the set of points in the final $[n/2]$ positions of the $P_x$ (the “right half”).
Then define $Q_x$ to be the set of points in $Q$ sorted by increasing $x$, $Q_y$ to be the set of points in $Q$ sorted by increasing $y$, $R_x$ to be the set of points in $R$ sorted by increasing $x$, $R_y$ to be the set of points in $R$ sorted by increasing $y$.
If there exists $q \in Q$ and $r \in R$ for which $d(q,r)<δ$, then each of $q$ and $r$ lies within a distance $δ$ of $L$.
![[Pasted image 20230723214715.png]]
### Algorithm
```
Closest-Pair(P)  
	Construct Px and Py
	(p0∗, p1∗) = Closest-Pair-Rec(Px,Py)
```

```
Closest-Pair-Rec(Px, Py)
	If |P| ≤ 3 then
		find closest pair by measuring all pairwise distances
	Endif

	Construct Qx, Qy, Rx, Ry
	(q0∗,q1∗) = Closest-Pair-Rec(Qx, Qy)
	(r0∗,r1∗) = Closest-Pair-Rec(Rx, Ry)

	δ = min(d(q0∗,q1∗), d(r0∗,r1∗))  
	x∗ = maximum x-coordinate of a point in set Q
	L = {(x,y) : x = x∗}  
	S = points in P within distance δ of L

	Construct Sy
	For each point s ∈ Sy, compute distance from s
		to each of next 15 points in Sy  
	Let s, s′ be pair achieving minimum of these distances

	If d(s,s′) < δ then 
		Return (s,s′)
	Else if d(q0∗,q1∗) < d(r0∗,r1∗) then 
		Return (q0∗,q1∗)
	Else
		Return (r0∗,r1∗)
	Endif
```
### Recurrence Relation
$$T(n) ≤ 2*T(n/2) + O(n) = O(n\log{n})$$