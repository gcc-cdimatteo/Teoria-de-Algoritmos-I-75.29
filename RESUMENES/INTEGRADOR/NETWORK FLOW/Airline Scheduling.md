## Problem
Given a set of $m$ particular flight segments, flight segment $j$ is specified by four parameters:
- origin airport
- destination airport
- departure time
- arrival time
It is possible to use a single plane for a flight segment $i$, and then later for a flight segment $j$, provided that
1. the destination of $i$ is the same as the origin of $j$, and there's enough time to perform maintenance on the plane in between; or
2. a flight segment can be added in between that gets the plane from the destination of $i$ to the origin of $j$ with adequate time in between