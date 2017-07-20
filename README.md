# Traveling Salesman Problem Simulated Annealing

## Cities
The grid_2d_cities class is designed to construct a two dimensional traveling salesman problem. It does this by generating an user-specified number of cities on a 2-D grid of user-specified size. The class can find a brute-force solution to the traveling salesman problem too, but there's a hard-coded cap for the maximum number of cities for which it will implement the brute-force solution. The class also plots the cities and any path specified by the user (if a brute force solution has been found, this gets plotted by default).

## Simulated Annealing
This solves the traveling salesman problem using a simple simulated annealing algorithm. Running main() will find a solution and compare it to the brute force solution, if the brute force solution is allowable (brute force solver is capped since number of paths grows as (n-1)!).

## Results
![alt text](https://github.com/prashil2792/)
![alt text](https://github.com/prashil2792/)


**References**
[Kirkpatrick et al. 1983: "Optimization by Simulated Annealing"](http://leonidzhukov.net/hse/2013/stochmod/papers/KirkpatrickGelattVecchi83.pdf)
