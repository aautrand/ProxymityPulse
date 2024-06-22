from scapy.all import *
from scapy.layers.dot11 import Dot11

from collections import Counter

c = Counter()

conf.iface = "wlan1"


v = 0

def packet_handler(p):
    global v

    if p.haslayer(Dot11):
        
        #if p.addr1 not in c and p.addr1 is not None:
            #print(p.addr1)
        

        if p.addr2 not in c and p.addr2 is not None:
       
            v += 1
            print(v, p.addr2)
        
        #c[p.addr1]d += 1
        c[p.addr2] += 1
        

sniff(iface="wlan1", prn=packet_handler, store=False)


