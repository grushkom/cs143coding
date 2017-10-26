from mininet.topo import Topo

class Q9Topo(Topo):
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        # Add your logic here ...
        
                    
topos = { 'custom': ( lambda: Q9Topo() ) }