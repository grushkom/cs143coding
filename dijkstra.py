from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os
''' Add your imports here ... '''
import csv



log = core.getLogger()
delayFile = "delay.csv"

''' Add your global variables here ... '''


class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    self.edges[from_node].append(to_node)
    self.edges[to_node].append(from_node)
    self.distances[(from_node, to_node)] = distance



class Dijkstra (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Dijkstra Module")

    def _handle_ConnectionUp (self, event):    
      visited = {initial: 0}
      path = {}

      nodes = set(graph.nodes)

      while nodes: 
        min_node = None
        for node in nodes:
          if node in visited:
            if min_node is None:
              min_node = node
            elif visited[node] < visited[min_node]:
              min_node = node

        if min_node is None:
          break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
          weight = current_weight + graph.distance[(min_node, edge)]
          if edge not in visited or weight < visited[edge]:
            visited[edge] = weight
            path[edge] = min_node

      return visited, path
        
    #log.debug("Dijkstra installed on %s", dpidToStr(pox.lib.revent.dpid))        

def launch ():
    '''
    Starting the Dijkstra module
    '''
    core.registerNew(Dijkstra)
