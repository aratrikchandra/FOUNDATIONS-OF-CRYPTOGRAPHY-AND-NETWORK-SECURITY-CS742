#!/usr/bin/python3

from scapy.all import *

# Put the interface of loopback interface.
# use ifconfig command and find interface which has "inet 127.0.0.1"
interfaces = ['ens33']

pkt = sniff(iface=interfaces, filter='udp', count=10, prn=lambda x: x.show())