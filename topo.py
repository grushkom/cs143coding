from mininet.topo import Topo

class Q9Topo(Topo):
    def __init__(self, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s14 = self.addSwitch('s14')
        s16 = self.addSwitch('s16')
        s18 = self.addSwitch('s18')
        h13 = self.addHost('h13')
        h15 = self.addHost('h15')
        h17 = self.addHost('h17')
        h19 = self.addHost('h19')
        g = self.addLink(s11, s12, bw=10, delay='10ms',  max_queue_size=1000, use_htb =True)
        h = self.addLink(s12, s14, bw=10, delay='50ms',  max_queue_size=1000, use_htb =True)
        i = self.addLink(s14, s16, bw=10, delay='10ms',  max_queue_size=1000, use_htb =True)
        j = self.addLink(s16, s18, bw=10, delay='30ms',  max_queue_size=1000, use_htb =True)
        k = self.addLink(s18, s11, bw=10, delay='30ms',  max_queue_size=1000, use_htb =True)
        l = self.addLink(s18, s12, bw=10, delay='10ms',  max_queue_size=1000, use_htb =True)
        m = self.addLink(s12, s16, bw=10, delay='100ms',  max_queue_size=1000, use_htb =True)
        n = self.addLink(s18, s14, bw=10, delay='20ms',  max_queue_size=1000, use_htb =True)
        self.addLink(h13, s12)
        self.addLink(h15, s14)
        self.addLink(h17, s16)
        self.addLink(h19, s18)
        # Add your logic here ...
        
                    
topos = { 'custom': ( lambda: Q9Topo() ) }