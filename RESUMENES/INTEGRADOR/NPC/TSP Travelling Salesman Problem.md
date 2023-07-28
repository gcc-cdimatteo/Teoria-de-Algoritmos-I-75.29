#NPC #Sequencing
## Problem
Consider a salesman who must visit $n$ cities $v_1, v_2, . . . , v_n$. He starts in city $v_1$, his home, and wants to find a tour—an order in which to visit all the other cities and return home. 
##### Goal
Find a tour that causes him to travel as little total distance as possible.
## Decision Problem
For each ordered pair of cities $(v_i, v_j)$, specify a nonnegative number $d(v_i, v_j)$ as the distance from $v_i$ to $v_j$.
Order the cities into a tour $v_1 ,v_2 ,...,v_n$ to minimize the total distance $\sum_{j}{d(v_j,v_{j+1})}+d(v_n,v_1)$.
Given a set of distances on $n$ cities, and a bound $D$, is there a tour of length at most $D$?