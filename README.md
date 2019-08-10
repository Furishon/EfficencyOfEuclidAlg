# Efficency of the Euclidian Algorithm
Investigating the efficiency of the Euclidean algorithm for finding gcd(a, b), as a function of integers a & b.


## The Euclidean Algorithm
The algorithm is a method for finding the gcd of two integers a & b. It works as follows:

Let r<sub>0<\sub> = a and r<sub>1<\sub> = b. Then r<sub>2<\sub> = r<sub>0<\sub> % r<sub>1<\sub>; r<sub>3<\sub> = r<sub>1<\sub> % r<sub>2<\sub>, ..., r<sub>n<\sub> = r<sub>n-2<\sub> % r<sub>n-1<\sub>, r<sub>n+1<\sub> = r<sub>n-1<\sub> % r<sub>n<\sub>, where r<sub>n+1<\sub> = 0. Then r<sub>n<\sub> = gcd(a, b).
  
  
## Evaluating efficency
This package evaluates the efficency by plotting the number of iterations required by the algorithm (the value of n+1) as a function of both a & b in a 3D-plot. The range of a & b is between 0 and a user-defined value.

Erik Göransson, Sweden
August 2019
