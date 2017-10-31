# from pox.core import core
# import pox.openflow.libopenflow_01 as of
# from pox.lib.revent import *
# from pox.lib.util import dpidToStr
# from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
import csv
import sys

# Usage: python dijkstra.py [topo.csv]

# parse csv
me, topo_file = sys.argv
read = csv.DictReader(open(topo_file))

def Dijkstra(graph, init, dstn, vstd=[], dists={}, prevs={}):
    
    # instantiate empty data structures
    path = []
    unvstd = {}

    # base case, for when we've reached the end
    if init == dstn:
        # output shortest path
        prev = dstn
        while prev != None:
            path.append(prev)
            prev=prevs.get(prev, None)
        print("Shortest path from {start} to {end} is through {path}: {length} ms.".format(start = str(path[len(path)-1]), end = str(dstn), path = str([path]), length = str(dists[dstn] - 1)))

    # keep searching
    else :
        # determine distance in first run
        if not vstd: 
            dists[init]=0
        # visit the node's neighbors
        for nbr in graph[init]:
            if nbr not in vstd:
                cur_dist = dists[init] + graph[init][nbr]
                if cur_dist < dists.get(nbr,float('inf')):
                    dists[nbr] = cur_dist
                    prevs[nbr] = init
        
        # add to visited set
        vstd.append(init)
        
        # run Dijkstra starting from n
        for i in graph:
            if i not in vstd:
                unvstd[i] = dists.get(i,float('inf'))        
        n = min(unvstd, key=unvstd.get)
        Dijkstra(graph, n, dstn, vstd, dists, prevs)

if __name__ == "__main__":

    # instantiate dictionary
    topo_list =  {}

    for line in read:
        topo_list[line["link"]] = line["delay"]
    print topo_list

    # makes graph with the specified topo and delays
    graph = {
        'h13': {'s12': 0},
        'h15': {'s14': 0},
        'h17': {'s16': 0},
        'h19': {'s18': 0},
        's11': {'s12': int(topo_list["g"]) , 's18': int(topo_list["k"])},
        's12': {'h13': 1, 's14': int(topo_list["h"]) , 's16': int(topo_list["m"]) , 's18': int(topo_list["l"])},
        's14': {'h15': 1, 's12': int(topo_list["h"]) , 's18': int(topo_list["n"]) , 's16': int(topo_list["i"])},
        's16': {'h17': 1, 's12': int(topo_list["m"]) , 's14': int(topo_list["i"]) , 's18': int(topo_list["j"])},
        's18': {'h19': 1, 's12': int(topo_list["l"]) , 's16': int(topo_list["j"]) , 's14': int(topo_list["n"])},
        }

    # run Dijkstra on all paths between hosts
    Dijkstra(graph, 'h13', 'h15', [], {}, {})
    Dijkstra(graph, 'h13', 'h17', [], {}, {})
    Dijkstra(graph, 'h13', 'h19', [], {}, {})
    Dijkstra(graph, 'h15', 'h17', [], {}, {})
    Dijkstra(graph, 'h15', 'h19', [], {}, {})
    Dijkstra(graph, 'h17', 'h19', [], {}, {})