## Problem
Given a flow network $G = (V, E)$ with capacities on the edges, where each node $v ∈ V$ has a demand $d_v$:
- if $d_v > 0$, $v$ is a **sink** and has a demand of $d_v$
- if $d_v < 0$, $v$ is a **source** and has a supply of $−d_v$
- if $d_v = 0$, $v$ is neither a source nor a sink
$S$ denote the set of all nodes with negative demand.
$T$ denote the set of all nodes with positive demand.
#### Feasibility Problem
A circulation with demands $d_v$ is a function that assigns a nonnegative real number to each edge and satisfies:
1. *Capacity conditions*: for each $e∈E$, $0≤f(e)≤c_e$
2. *Demand conditions*: for each $v∈V$, $f_{in}(v)−f_{out}(v)=d_v$
Find whether exists a circulation that meets both conditions.
### Feasible Circulation
The total supply must equal the total demand: $$D=\sum_{v:d_v>0}{d_v}= \sum_{v:d_v<0}{-d_v}$$
## Solution
1. Copy $G$ into $G'$
2. Attach in $G'$ a *super-source* $s*$ to each node in $S$ with capacity $-d_v$
3. Attach in $G'$ a *super-sink* $t*$ to each node in $T$ with capacity $d_v$
4. Use Ford-Fulkerson to find the maximum flow in $G'$
There is a **feasible circulation** with demands $d_v$ in $G$ if and only if the maximum $s∗-t∗$ flow in $G'$ has value $D$.