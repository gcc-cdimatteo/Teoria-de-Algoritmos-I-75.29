#Theorem
Total minimum weight needed to disconnect a graph (connected for undirected graphs, weakly connected for directed).    
If the graph is non-weighted, it corresponds to the number of edges (such as considering all as weight = 1).    

*==If the graph corresponds to a flow network, then the minimum cut has a capacity equal to the maximum flow. It will happen that the source and the sink are in opposite sets.==*

## Algorithm
1. Grab the residual graph
2. See all the vertices reached from the source
3. All the edges (of the original graph) that go from a vertex that can be reached (in the residual) to one that cannot, are part of the cut