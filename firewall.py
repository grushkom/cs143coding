from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
import pox.lib.packet as pkt
from collections import namedtuple
import os
import csv

log = core.getLogger()
policyFile = "/pox/pox/misc/firewall-policies.csv"

class Firewall (EventMixin):

    def __init__ (self):
        self.listenTo(core.openflow)
        log.info("Enabling Firewall Module")
        self.firewall = {}

    def sendRule (self, src, dst, duration = 0):
        if not isinstance(duration, tuple):
            duration = (duration,duration)
        msg = of.ofp_flow_mod()
    match = of.ofp_match(dl_type = 0x800,
                 nw_proto = pkt.ipv4.ICMP_PROTOCOL)
        match.nw_src = IPAddr(src)
        match.nw_dst = IPAddr(dst)
        msg.match = match
        msg.idle_timeout = duration[0]
        msg.hard_timeout = duration[1]
        msg.priority = 10
        self.connection.send(msg)

    def AddRule (self, src=0, dst=0, value=True):
        if (src, dst) in self.firewall:
            log.info("Rule already present drop: src %s - dst %s", src, dst)
        else:
            log.info("Adding firewall rule drop: src %s - dst %s", src, dst)
            self.firewall[(src, dst)]=value
            self.sendRule(src, dst, 10000)

    def DeleteRule (self, src=0, dst=0):
        try:
            del self.firewall[(src, dst)]
            sendRule(src, dst, 0)
            log.info("Deleting firewall rule drop: src %s - dst %s", src, dst)
        except KeyError:
            log.error("Cannot find in rule drop src %s - dst %s", src, dst)

    def _handle_ConnectionUp (self, event):
        self.connection = event.connection

        ifile  = open(policyFile, "rb")
        reader = csv.reader(ifile)
        rownum = 0
        for row in reader:
            if rownum == 0:
                header = row
            else:
                colnum = 0
                for col in row:
                    colnum += 1
                self.AddRule(row[1], row[2])
            rownum += 1
        ifile.close()

        log.info("Firewall rules installed on %s", dpidToStr(event.dpid))

def launch ():
    core.registerNew(Firewall)