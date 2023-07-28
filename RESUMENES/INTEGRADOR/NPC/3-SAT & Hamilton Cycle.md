Recall [[SAT Satisfiability Problem#3-SAT]] & [[Hamilton Cycle]].
## $3-SAT \leq_p Hamilton \space Cycle$
For a 3-SAT expression containing $n$ variables, there are $2^n$ possible assignments.
Model the $2^n$ possible assignments using a graph with $2^n$ different *Hamiltonian Cycles*:
1. Construct Paths
	1. Construct $n$ paths $P_1, P_2, ..., P_n$ corresponding to the $n$ variables.
	2. Each path $P_i$ should consist of $2k$ nodes where $k$ is the number of clauses in the expression.
	3. Add edges from $v_{i,j-1}$ to $v_{i,j}$ on $P_i$ corresponding to $x_i=True$
	4. Add edges from $v_{i,j}$ to $v_{i,j-1}$ on $P_i$ corresponding to $x_i=False$
![[Pasted image 20230728192413.png]]
2. Inter-connect the paths: add edges from $v_{i,1}$ and $v_{i,n}$ to $v_{i+1,1}$ and $v_{i+1,n}$
3. Add source and target nodes: 
	1. add edges from $s$ to $v_{1,1}$ and $v_{1,n}$
	2. add edges from $v_{i,1}$ and $v_{i,n}$ to $t$
	3. add an edge from $t$ to $s$
![[Pasted image 20230728193150.png]]
4. Add nodes corresponding to clauses:
5. Connect clauses to the paths
	1. if a clause $C_j$ contains the variable $x_i$ (left to right):
		1. add an edge from $v_{i,2j-1}$ to $c_j$
		2. add an edge from $c_j$ to $v_{i,2j}$
	2. if a clause $C_j$ contains the variable $\bar{x_i}$ (right to left):
		1. 1. add an edge from $v_{i,2j}$ to $c_j$
		2. add an edge from $c_j$ to $v_{i,2j-1}$
![[Pasted image 20230728193830.png]]
If there exists a Hamiltonian Cycle $H$ in the constructed graph $G$:
- if $H$ traverses $P_i$ from left to right, $x_i=True$
- if $H$ traverses $P_i$ from right to left, $x_i=False$
Since $H$ visits each clause node $C_j$, at least one of $P_i$ was traversed in the right direction relative to the node $C_j$ and the assignment satisfies the 3-SAT instance.