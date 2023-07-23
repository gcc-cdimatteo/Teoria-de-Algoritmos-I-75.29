Backward version of [[Kruskal's MST]].
Start with the full graph $(V, E)$ and begin deleting edges in order of decreasing cost. As the edge $e$ is reached (starting from the most expensive), delete it as long as doing so would not actually disconnect the graph.
### Pseudocode
#incomplete 
### Proof of Optimality
#incomplete 
### Time Complexity
Because of the edge sorting by decreasing cost $$O(E \log{E})$$