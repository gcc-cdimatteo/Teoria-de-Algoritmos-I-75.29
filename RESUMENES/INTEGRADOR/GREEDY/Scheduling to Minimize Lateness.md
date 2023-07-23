## Problem
Set of requests $R = \{1,2,...,n\}$, $i^{th}$ has a deadline $d_i$ & a duration $t_i$. A request $i$ is late if it misses the deadline: $s(i) + t_i = f(i) > d_i$. The lateness is defined to be $l_i = f(i) - d_i$, $l_i=0$ if $i$ is not late.
###### Goal
Minimize the maximum lateness $L=max_i l_i$.
## Solution
Schedule all requests in order. 
Request $1$ will start at $s=s(1)$ and end at $f(1)=s(1)+t_1$.
Request $2$ will start at $s(2) = f(1)$ and end at $f(2) = s(2) + t_2$.
$f$ denote the finishing time of the last scheduled request.
### Pseudocode
```
Sort the requests by their deadlines  

f = s

For each request i=1,...,n
	Assign request i to the time interval from s(i)=f to f(i)=s(i)+ti
	Let f = f(i)
Endfor

Return the set of scheduled intervals [s(i), f (i)] for i = 1,...,n
```
### Proof of Optimality
###### the schedule have no idle time
###### schedules with no inversions and no idle time have the same maximum lateness
Schedule $A'$ has an inversion if a request $i$ with deadline $d_i$ is scheduled before another request $j$ with earlier deadline $d_j < d_i$. 
The schedule $A$ produced by greedy has no inversions. If there are requests with identical deadlines then there can be many different schedules with no inversions.
Consider such a deadline $d$. In both schedules, the requests with deadline $d$ are all scheduled consecutively (after all jobs with earlier deadlines and before all jobs with later deadlines). Among the requests with deadline $d$, the last one has the greatest lateness, and this lateness does not depend on the order of the requests.
#incomplete
