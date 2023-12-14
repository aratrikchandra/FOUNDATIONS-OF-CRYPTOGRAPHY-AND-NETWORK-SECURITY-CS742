#!/usr/bin/python3

from scapy.all import *

# Create IP Packet
ippacket = IP()
# Put IP address to spoof here
ippacket.src = '192.168.14.12'

# Your ethernet IP address, typically the one with interface eth0, ensXX, wlan0, or equivalent.
# Do no use localhost or 127.0.0.1 since with scapy it won't work 
ippacket.dst = '192.168.220.128'

# Create UDP Packet
udppacket = UDP()

udppacket.dport=2005;

#Create Final packet
packetToSend = ippacket/udppacket

# Send the packet
send(packetToSend)