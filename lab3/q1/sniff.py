#!/usr/bin/python3

from scapy.all import *

# Put the interface of loopback interface.
# use ifconfig command and find interface which has "inet 127.0.0.1"
interfaces = ['lo']

pkt = sniff(iface=interfaces, filter='tcp', count=10, prn=lambda x: x.show())


