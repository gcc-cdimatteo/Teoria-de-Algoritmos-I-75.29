## Problem
Given a company that sells $k$ products and has a database containing the purchase histories of a large number of customers, it is wished to conduct a survey, sending customized questionnaires to a particular group of $n$ of its customers, to try determining which products people like overall.
Guidelines:
- each customer will receive questions about a certain subset of the products
- a customer can only be asked about products that he or she has purchased
- each customer $i$ should be asked about a number of products between $c_i$ and $c_i'$
- there must be between $p_j$ and $p_j$ distinct customers asked about each product $j$
Given a bipartite graph $G$ whose nodes are the customers and the products, and there is an edge between customer $i$ and product $j$ if he or she has ever purchased product $j$. For each customer $i = 1, . . . , n$, there are limits $c_i ≤ c_i'$ on the number of products he or she can be asked about; for each product $j=1,...,k$, there are limits $p_j ≤ p_j$ on the number of distinct customers that have to be asked about it. 
##### Goal
Decide if there is a way to design a questionnaire for each customer so as to satisfy all these conditions.
## Solution
Reduce the problem to [[Circulations with Demands]]:
1. Obtain $G'$ from $G$:
	1. orient the edges of $G$ from customers to products
	2. add nodes $s$ and $t$ with edges $(s,i)$ for each customer $i=1,...,n$, edges $(j,t)$ for each product $j = 1, . . . , k$, and an edge $(t, s)$
2. flow on the edge $(s, i)$ is the number of products included on the questionnaire for customer $i$, so this edge will have a 
	1. capacity of $c_i'$ 
	2. lower bound of $c_i$ 
3. flow on the edge $(j, t)$ will correspond to the number of customers who were asked about product $j$, so this edge will have a 
	1. capacity of $p_j'$
	2. lower bound of $p_j$
4. each edge $(i, j)$ going from a customer to a product he or she bought has 
	1. capacity of $1$
	2. lower bound of $0$
5. flow carried by the edge $(t , s)$ corresponds to the overall number of questions asked and can have a 
	1. capacity of $\sum_{i}{c_i'}$
	2. lower bound of $\sum_{i}{c_i}$
Check whether it has a feasible circulation.