## Problem
Set of requests $R = \{1,2,...,n\}$, $i^{th}$ starts at $s(i)$ & finishes at $f(i)$, $i_1$ & $i_2$ are *compatible* if they don't overlap in time.
###### Goal
$|S|\in max$
## Solution
Accept $i / f(i) \in min$ to maximize the time left to satisfy other requests so then the resource becomes free as soon as possible.
### Pseudocode
![[Pasted image 20230717174801.png]]
![[Pasted image 20230717175031.png]]
### Proof of Optimality
$S \in$ greedy solution, $O \in$ optimal solution, $|S|=k$, $|O|=m$.
We want to prove that greedy rule *stays ahead*, meaning each of its intervals finishes at least as soon as the corresponding interval in the optimal set:
$$\forall r ≤ k / f(i_r) ≤ f(j_r)$$
![[Pasted image 20230717181602.png]]
#### Induction
Assuming $f(i_{r−1})≤f(j_{r−1})$, the optimal solution has to be proven for $r$.
Given that $i_{r−1}$ has been chosen by $S$, $i_r$ & $j_r$ are both possible elections for $S$; but because the greedy heuristic selects the available interval with smallest finish time, $i_r$ won't be chosen due to $f(i_r)>f(j_r)$.
#### Contradiction
If $S \notin optimal \therefore m>k$, having $r = k \implies f(i_k) ≤ f(j_k) \implies f(i_k) ≤ f(j_{k+1})$ because of which $j_{k+1}$ is still in the set of possible requests for $S$; but the greedy algorithm stopped with request $i_k$, and it is only supposed to do it when $R$ is empty $\implies ABS!$
### Time Complexity
Sort the $n$ requests in order of *finishing time* $$O(n\log{n})$$
Construct an array with the *starting time* values $S[1,...,n]$ $$O(n)$$
Select requests by processing the intervals in order of increasing $f(i)$. Select the first interval; then iterate through the intervals in order until reaching the first $j$ for which $s(j) ≥ f (1)$.
## Related
[[Interval Partitioning]]