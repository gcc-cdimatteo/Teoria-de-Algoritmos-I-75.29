## Problem
Multiplication of two integers.
## Solution
In $base_2$: $$x*y = x_1y_1 * 2^n + (x_1y_0 + x_0y_1)*2^{n/2} + x_0*y_0$$
### Algorithm
```
Recursive-Multiply(x,y):
	Write 
		x = x1 * 2^(n/2) + x0  
		y = y1 * 2^(n/2) + y0

	Compute x1 + x0 and y1 + y0  
	p = Recursive-Multiply(x1 + x0, y1 + y0)
	x1y1 = Recursive-Multiply(x1, y1)  
	x0y0 = Recursive-Multiply(x0 , y0)  
	
	Return x1y1 * 2^n + (p − x1y1 − x0y0) * 2^(n/2) + x0y0
```
### Recurrence Relation
$$T(n) ≤ 3*T(n/2) + cn ≤ O(n^{log_{2}{3}}) = O(n^{1.59}) \approx O(n^2)$$
