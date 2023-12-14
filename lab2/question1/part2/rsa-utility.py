#!/usr/bin/python3
from Crypto.PublicKey import RSA
import argparse
  
  
# Initialize the Parser
parser = argparse.ArgumentParser(description ='RSA Utility Tool')
  
# Adding Arguments
parser.add_argument('file', 
                    type = str,
                    help ='Private Key File Path')
fileName = parser.parse_args().file
with open(fileName, mode='rb') as privatefile:
    keydata = privatefile.read()
prkey = RSA.importKey(keydata)
print("n:", prkey.n, end="\n\n")
print("p:", prkey.p, end="\n\n")
print("q:", prkey.q, end="\n\n")
print("phi:", (prkey.p-1)*(prkey.q-1), end="\n\n")
print("e:", prkey.e, end="\n\n")
print("d:", prkey.d, end="\n\n")
