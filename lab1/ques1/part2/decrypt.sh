#!/bin/bash

openssl enc -aes-128-cbc -d -in secret.bin -out plaintext_cbc.txt -K 11152569842abcfdd5116 -iv 102030506070ddff
openssl enc -aes-128-ecb -d -in secret.bin -out plaintext_ecb.txt -K 11152569842abcfdd5116
openssl enc -aes-128-cfb -d -in secret.bin -out plaintext_cfb.txt -K 11152569842abcfdd5116 -iv 102030506070ddff
openssl enc -aes-128-ofb -d -in secret.bin -out plaintext_ofb.txt -K 11152569842abcfdd5116 -iv 102030506070ddff
openssl enc -aes-128-ctr -d -in secret.bin -out plaintext_ctr.txt -K 11152569842abcfdd5116 -iv 102030506070ddff

