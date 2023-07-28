Recall [[Hamilton Cycle]] & [[TSP Travelling Salesman Problem]].
## $Hamilton \space Cycle \leq_p TSP$
Given a directed graph $G = (V , E)$, a city $v_i'$ for each node $v_i$ of the graph $G$. Define $d(v_i', v_j')$ to be $1$ if there is an edge $(v_i, v_j)$ in $G$, and we define it to be $2$ otherwise.
$G$ has a *Hamiltonian cycle* if and only if there is tour of length at most $n$ in the *Traveling Salesman* instance. For if $G$ has a Hamiltonian cycle, then this ordering of the corresponding cities defines a tour of length $n$.