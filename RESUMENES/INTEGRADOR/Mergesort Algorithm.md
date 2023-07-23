## Problem
Sort an array.
## Solution
Once the input has been reduced to size 2, stop the recursion and sort the two elements by comparing them to each other.
### Recurrence Relation
$$T(n) ≤ 2*T(n/2) + O(n) = O(n\log{n})$$