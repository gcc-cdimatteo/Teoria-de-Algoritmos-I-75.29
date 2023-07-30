- **Complexity class $P$**: set of decision problems for which exists an algorithm that can solve any instance of a problem in polynomial time.
- **Complexity class $NP$**: set of decision problems for which exists a certifier that can verify any instance of a problem with evidence in polynomial time.
- $P ⊆ NP$: if a problem is contained in $P$ exists an algorithm that can solve it in polynomial time; therefore exists a certifier that can certify the problem in polynomial time.
- $Y ≤_p X$: if $X$ can be solved in polynomial time, then $Y$ can be solved in polynomial time.
- $Y ≤_p X$: if $Y$ cannot be solved in polynomial time, then $X$ cannot be solved in polynomial time.
- **Transitivity of Reductions**: if $Z≤_p Y ∧ Y≤_p X \implies Z≤_p X$
- $𝑋 \in 𝑁𝑃-𝐻ard ⇔ ∀ 𝑌∈𝑁𝑃: 𝑌 ≤_p 𝑋$
- $𝑋∈𝑁𝑃-𝐶omplete ⇔ 𝑋∈𝑁𝑃 ∧ 𝑋∈𝑁𝑃-𝐻ard$
- $Y∈𝑁𝑃-𝐶omplete ∧ X∈𝑁𝑃: Y\leq_p X \implies X \in NP-Complete$
## Problems
[[Independent Set]]
[[Vertex Cover]]
[[Set Cover]]
[[Set Packing]]
[[SAT Satisfiability Problem]]
[[TSP Travelling Salesman Problem]]
[[Hamilton Cycle]]
[[3-D Matching]]
[[Subset Sum]]
[[k-Coloring]]
## Reductions
[[Independent Set & Vertex Cover]]
[[Vertex Cover & Set Cover]]
[[Independent Set & Set Packing]]
[[3-SAT & Independent Set]]
[[3-SAT & Hamilton Cycle]]
[[Hamilton Cycle & TSP]]
[[3-SAT & 3-D Matching]]
[[3-SAT & k-Coloring]]

$3-SAT ≤_p Independent \space Set ≤_p Vertex \space Cover ≤_p Set \space Cover$
$3-SAT \leq_p Hamilton \space Cycle \leq_p TSP$
$3-SAT \leq_p 3-D \space Matching$
$3-SAT \leq_p 3-Coloring \leq_p k-Coloring$