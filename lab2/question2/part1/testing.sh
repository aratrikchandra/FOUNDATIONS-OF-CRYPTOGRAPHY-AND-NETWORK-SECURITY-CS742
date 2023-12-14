#!/bin/bash

permissions_file="permissions.txt"
evil_permissions_file="evil-permissions.txt"

permissions_hash=$(md5sum $permissions_file | cut -c 1-4)

while true; do
    evil_permissions_hash=$(md5sum $evil_permissions_file | cut -c 1-4)
    if [ "$evil_permissions_hash" == "$permissions_hash" ]; then
        break
    fi
    echo -n " " >> $evil_permissions_file
done

echo "The first 16 bits of the MD5 hash of both files now match!"