from datetime import datetime as dt
from scapy.all import *
from scapy.layers.dot11 import Dot11

from collections import Counter

c = Counter()

conf.iface = "wlan1"

v = 0


def wireless_card_available():
    # TODO write this code. Try to do it without chatgpt
    return True

def is_monitor_mode(interface):
    # TODO Write this code. Try not to use chatgpt
    return True

def packet_handler(p):
    global v

    if p.haslayer(Dot11):
        
        # if p.addr1 not in c and p.addr1 is not None:
        #    print(p.addr1)
        

        if p.addr2 not in c and p.addr2 is not None:
       
            v += 1
            print(v,"\t" ,p.addr2,"\t", dt.now())
        
        #c[p.addr1]d += 1
        c[p.addr2] += 1
    else:
        print("no layer11")


if __name__ == "__main__":
    print("initializing")
    if wireless_card_available():
        interface = "wlan1" # TODO make this dynamic
        if is_monitor_mode(interface):
            sniff(iface=interface, prn=packet_handler, store=False)
        # TODO add log msg that interface is not in monitor mode
    # TODO add log that wireless card is not available
