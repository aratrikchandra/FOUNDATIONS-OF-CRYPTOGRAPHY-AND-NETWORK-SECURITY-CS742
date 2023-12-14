#!/bin/bash

# Encryption
openssl enc -aes-128-ecb -e -in secret.txt -out output_ecb.bin -K 55110062015112014aaff2d1f
openssl enc -aes-128-ctr -e -in secret.txt -out output_ctr.bin -K 55110062015112014aaff2d1f -iv 01020304055040302010
openssl enc -aes-256-cbc -e -in secret.txt -out output_cbc.bin -K 55110062015112014aaff2d1f -iv 01020304055040302010
openssl enc -aes-256-cfb -e -in secret.txt -out output_cfb.bin -K 55110062015112014aaff2d1f -iv 01020304055040302010
openssl enc -aes-256-ofb -e -in secret.txt -out output_ofb.bin -K 55110062015112014aaff2d1f -iv 01020304055040302010

# MD5 Sum
md5sum output_ecb.bin | cut -d ' ' -f 1 > flags.txt
md5sum output_ctr.bin | cut -d ' ' -f 1 >> flags.txt
md5sum output_cbc.bin | cut -d ' ' -f 1 >> flags.txt
md5sum output_cfb.bin | cut -d ' ' -f 1 >> flags.txt
md5sum output_ofb.bin | cut -d ' ' -f 1 >> flags.txt

