#NPC
Given a set $X$ of $n$ Boolean variables $x_1, . . . , x_n$ and a clause as a disjunction of distinct terms $t_1 ∨ t_2 ∨ . . . ∨ t_l$ with length $l$ if it contains $l$ terms: an assignment satisfies a clause $C$ if it causes $C$ to evaluate to $1$ requiring that at least one of the terms in $C$ should receive the value $1$; it also satisfies a collection of clauses $C_1, . . . , C_k$ if it causes all of the $C_i$ to evaluate to $1$causing the conjunction $C_1 ∧ C_2 ∧ . . . ∧ C_k$ to evaluate to $1$.
## Decision Problem
Given a set of clauses $C_1,...,C_k$ over a set of variables $X ={x_1,...,x_n}$, does there exist a satisfying truth assignment?
## 3-SAT
### Decision Problem
Given a set of clauses $C_1,...,C_k$, each of length 3, over a set of variables $X ={x_1,...,x_n}$, does there exist a satisfying truth assignment?
### Class Complexity
$$3-SAT \in NPC$$