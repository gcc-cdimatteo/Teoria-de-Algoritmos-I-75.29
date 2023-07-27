## Problem
Given a set of $m$ particular flight segments, flight segment $j$ is specified by four parameters:
- origin airport
- destination airport
- departure time
- arrival time
It is possible to use a single plane for a flight segment $i$, and then later for a flight segment $j$, provided that
1. the destination of $i$ is the same as the origin of $j$, and there's enough time to perform maintenance on the plane in between; or
2. a flight segment can be added in between that gets the plane from the destination of $i$ to the origin of $j$ with adequate time in between
## Solution
Extend the problem to a flow network where the units of flow will correspond to airplanes. Define a graph $G$ such as:
1. Include a source $s$ with demand of $-k$
2. and a sink $t$ with demand of $k$
3. For each flight $i$, create two nodes $u_i$ and $v_i$ with demand of $0$
The edge set $E$ is defined by:
1. *Each flight on the list must be served*: for each $i$
	1. $l_e(u_i , v_i)=1$
	2. $c_e(u_i , v_i)=1$
2. *The same plane can perform flights i and j*: for each $i$ and $j$ so that flight $j$ is reachable from flight $i$
	1. $l_e(v_i, u_j)=0$
	2. $c_e(v_i, u_j)=1$
3. *Any plane can begin the day with flight i*: for each $i$
	1. $l_e(s, u_i)=0$
	2. $c_e(s, u_i)=1$
4. *Any plane can end the day with flight j*: for each $j$
	1. $l_e(v_j , t)=0$
	2. $c_e(v_j , t)=1$
5. *If exists extra planes, don’t need to use them*:
	1. $l_e(s, t)=0$
	2. $c_e(s, t)=k$
==There is a way to perform all flights using at most k planes if and only if there is a feasible circulation in the network G.==
![[Pasted image 20230726205349.png]]