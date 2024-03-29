# Data-Structure-Python

## Algorithm Complexity 
Let X = algorithm and n = size of input data 
Time and Space used by algorith X are two main factors which decide efficiency of X. 

1) Time Factor : Measured by counting the number of key operations . 
2) Space Factor : Measured by counting the maximum memory space required by algorithm. 

## Time Complexity
The time required by the algorithm to solve given problem is called time complexity  of the algorithm.It quantifies the amount of time taken by an algorithm to run as a function of the length of the input. 
Tc(n) = c * n 
where, n = no. of steps in algorithm 
       c = time taken in each step 


## Asymptotic Analysis
To conclude Best, Average and Worst case based on Runtime execution.

Time requiered by an algorithm falls under 3 types: 
1) Best Case - Minimum time required for program execution. 
2) Average Case - Average time required for program execution. 
3) Worst Case - Maximum time required for program execution. 

Commonly Used Asymptotic notation to calculate the time complexity of Algorithm. 

### 1) Big Oh Notation(O) - 
Defines upper bound of an algorithm's running time. 
Measures worst case time complexity or the longest amount of time an algorithm can possibly take to complete. 

Mathematical Expression: 
0 <= f(n) <= c*g(n) for all n >= no
where , f(n) = Time Algorithm for function
        g(n) = function 
        
### 2) Big Omega(Ω):
Defines lower bound of algorithm's running time. 
Measures best case time complexity .

Mathematical Expression: 
0 <= c*g(n) <= f(n) for all n >= no
where , f(n) = Time Algorithm for function
        g(n) = function 

### 3) Big Theta(Θ): 
Express lower and upper bound of algorithm's running time. 
Used to describe avearge case. 

Mathematical Expression: 
c2*g(n) <= f(n) <= c1*g(n) for all n >= no
where , f(n) = Time Algorithm for function
        g(n) = function 


### Increasing order of Common Runtimes: 
1 < logn < n < nlogn < n**2 < n**3 < 2**n < n**n

#### Quick Sort 
Average Case Time complexity - O(nlogn) as array is partitioned into 2 sub-arrays around the pivot (median value of array) element and recursively sorts each sub-array. 
Worst Case Tiem Complexity - O(n**2) 

#### Binary Search 
Time Complexity = O(logn) as it follows divide-and-conquer algorithm. 
        
