Recall [[Vertex Cover]] & [[Set Cover]].
## $Vertex \space Cover ≤_p Set \space Cover$
Our goal is to cover the edges in $E$, so we formulate an instance of Set Cover in which the ground set $U$ is equal to $E$. Each time we pick a vertex in the Vertex Cover Problem, we cover all the edges incident to it; thus, for each vertex $i ∈ V$, we add a set $S_i ⊆ U$ to our Set Cover instance, consisting of all the edges in $G$ incident to $i$.
We now claim that $U$ can be covered with at most $k$ of the sets $S_1,...,S_n$ if and only if $G$ has a vertex cover of size at most $k$.
Given our instance of Vertex Cover, we formulate the instance of Set Cover described above, and pass it to our black box. We answer yes if and only if the black box answers yes.