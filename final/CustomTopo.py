#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.node import OVSSwitch
from mininet.topolib import TreeNet

class CustomTopo(Topo):
	"Simple Data Center Topology"
	"linkopts - (1:core, 2:aggregation, 3: edge) parameters"
	"fanout - number of child switch per parent switch"
	def __init__(self, linkopts1 = 1, linkopts2 = 2, linkopts3 = 4, fanout=2, **opts):
		# Initialize topology and default options
		Topo.__init__(self, **opts)
		# Add your logic here ...
		setLogLevel( 'info' )
		network = TreeNet(depth = 3, fanout = 2, switch = OVSSwitch)
		network.run(CLI, network)

        
                    
topos = { 'custom': ( lambda: CustomTopo() ) }

def simpleTest():
	"Create and test a simple network"
	topo = CustomTopo(linkopts1 = 1, linkopts2 = 2, linkopts3 = 4, fanout=2)
	net = Mininet(topo)
	net.start()
	print("Dumping host connections")
	dumpNodeConnections(net.hosts)
	print("Testing network connectivity")
	net.pingAll()
	net.stop()
	

setLogLevel('info')
simpleTest()