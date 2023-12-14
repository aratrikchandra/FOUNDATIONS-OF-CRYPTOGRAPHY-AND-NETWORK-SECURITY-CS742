import binascii

# Extract the values
P1 = binascii.unhexlify('48656c6c6c6f20576f726c64215f356631326337653033643934633034656330316663613530')
C1 = binascii.unhexlify('ad54d05f895432b864121e0e4786220fb8e03e6ac306c595ef6cf87db82dc0990e37c8d4d528')
C2 = binascii.unhexlify('835ddd549e4d2396522b42182a95661dc09a6d19916483b2e03fa822c52f92f05b15eee3d465')

# Calculate the keystream used in OFB mode
keystream = bytes([p1 ^ c1 for p1, c1 in zip(P1, C1)])

# Decrypt C2 using the keystream to get P2
P2 = bytes([c2 ^ ks for c2, ks in zip(C2, keystream)])

# Convert P2 from bytes to ASCII
P2 = P2.decode('ascii')

print(P2)

