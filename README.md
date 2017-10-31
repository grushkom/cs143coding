# CS143 Coding Assignment
# Mikhail Grushko and Matthew Li
# README.md

## Question 7
### Usage:

In order to run the custom topology, run the following command in your virtual machine:

    $ sudo mn --custom CustomTopo.py --topo custom --test pingall


## Question 8
### Usage:

Run the following set of commands in the VM:

    $ cd ~
    $ pox.py forwarding.l2_learning misc.firewall &
    $ sudo mn --topo single,3 --controller remote --mac
    mininet> h1 ping -c1 h2


## Question 9
### Usage:

    python dijkstra.py topo.csv

For this question, we were unable to implement Dijkstra's algorithm in a method that would allow the algorithm to interface with OpenFlow and POX. As an alternative, we implemented Dijkstra's algorithm in Python, and instantiated a graph with the same topology and delays as specified in question 9. We then ran Dijkstra's algorithm on each possible host-host path.

The code for dijkstra.py takes in a command line argument, topo.csv, which specifies the links and their respective delays.
