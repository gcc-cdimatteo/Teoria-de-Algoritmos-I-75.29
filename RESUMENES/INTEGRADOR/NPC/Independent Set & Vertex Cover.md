Recall [[Independent Set]] & [[Vertex Cover]].

Let $G = (V , E)$ be a graph, $S$ is an independent set if and only if its complement $V-S$ is a vertex cover.
![[Pasted image 20230728094400.png]]
Suppose that $S$ is an independent set. Consider an arbitrary edge $e = (u, v)$. Since $S$ is independent, it cannot be the case that both $u$ and $v$ are in $S$; so one of them must be in $V − S$. It follows that every edge has at least one end in $V − S$, and so $V − S$ is a vertex cover.
Suppose that $V − S$ is a vertex cover. Consider any two nodes $u$ and $v$ in $S$. If they were joined by edge $e$, then neither end of $e$ would lie in $V − S$, contradicting our assumption that $V − S$ is a vertex cover. It follows that no two nodes in $S$ are joined by an edge, and so $S$ is an independent set.
## Reduction
$$Independent \space Set ≤_p Vertex \space Cover$$
If we have a black box to solve *Vertex Cover*, then we can decide whether $G$ has an independent set of size at least $k$ by asking the black box whether $G$ has a vertex cover of size at most $n − k$.
$$Vertex \space Cover ≤_p Independent \space Set$$
If we have a black box to solve *Independent Set*, then we can decide whether *G* has a vertex cover of size at most $k$ by asking the black box whether $G$ has an independent set of size at least $n − k$.