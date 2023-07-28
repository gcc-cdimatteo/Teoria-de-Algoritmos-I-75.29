Recall [[SAT Satisfiability Problem]] & [[Independent Set]].
## $3-SAT ≤_p Independent \space Set$
Let $\phi$ be a boolean expression representing a 3-SAT problem instance, express $\phi$ as a graph so that if the graph has an independent set then $\phi$ is satisfiable:
1. Create a vertex for each literal.
2. Connect each literal to other two in the same clause.
3. Connect each literal to it's complement ($x_i$ to $\bar{x_i}$).
Let $n$ be the number of variables in $\phi$ and $m$ be the number of boolean clauses, $\phi$ can be satisfied if and only if the graph has an independent set of size $m$.