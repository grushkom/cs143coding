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
policyFile = "%s/pox/pox/misc/firewall-policies.csv" % os.environ[ 'HOME' ]

''' Add your global variables here ... '''
# Create a list of src/dst MAC Addr pairs to be blocked
blockList=list()

with open(policyFile) as f:
    reader = csv.reader(f,delimiter=',') 
    # For each row in the csv file, read in all columns except for the 1st one
    for row in reader:
        blockList.append(row[1:])

# Delete the first row since it is just header, not data
blockList.pop(0)


class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp (self, event):
        ''' Add your logic here ... '''
        for sublist in blockList:
            # Create a block match
            # Not specifying action means "no action" or drop by default
            blockRule = of.ofp_match()
            blockRule.dl_src = EthAddr(sublist[0])
            blockRule.dl_dst = EthAddr(sublist[1])
            
            # Create a message containing blockRule and send to OpenFlow Switch
            fm = of.ofp_flow_mod()
            fm.match = blockRule
            event.connection.send(fm)
            
            
            
            
        
        

    
        log.debug("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    '''
Starting the Firewall module
'''
    core.registerNew(Firewall)s