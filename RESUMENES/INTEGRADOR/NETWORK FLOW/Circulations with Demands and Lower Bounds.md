## Problem
Given a flow network $G = (V, E)$ with a capacity $c_e$ and a lower bound $l_e$ on each edge $e$, meaning that the flow value on e must be at least $l_e$. We will assume $0 ≤ l_e ≤ c_e$ for each $e$. Each node $v$ will also have a demand $d_v$, which can be either positive or negative.
1. *Capacity conditions*: for each $e∈E$, $l_e≤f(e)≤c_e$
2. *Demand conditions*: for each $v∈V$, $f_{in}(v)−f_{out}(v)=d_v$
Decide whether there exists a *feasible circulation* that satisfies the conditions.
## Solution
Having $$L_v=\sum_{e \space into \space v}{l_e} - \sum_{e \space out \space of \space v}{l_e}$$
1. Copy $G$ into $G'$ without lower bounds
2. The capacity of edge $e$ will be $c_e-l_e$
3. The demand of node $v$ will be $d_v-L_v$