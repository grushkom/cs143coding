# cs143coding

## Question 7

## Question 8

## Question 9
###Usage:
python dijkstra.py topo.csv

For this question, we were unable to implement Dijkstra's algorithm in a method that would allow the algorithm to interface with OpenFlow and POX. As an alternative, we implemented Dijkstra's algorithm in Python, and instantiated a graph with the same topology and delays as specified in question 9. We then ran Dijkstra's algorithm on each possible host-host path.

The code for dijkstra.py takes in a command line argument, topo.csv, which specifies the links and their respective delays.