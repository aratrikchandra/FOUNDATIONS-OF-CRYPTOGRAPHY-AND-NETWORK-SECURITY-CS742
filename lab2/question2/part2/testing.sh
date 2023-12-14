#!/bin/bash

permissions1_file="permissions1.txt"
permissions2_file="permissions2.txt"

# Calculate the initial hashes
permissions1_hash=$(md5sum $permissions1_file | cut -c 1-4)
permissions2_hash=$(md5sum $permissions2_file | cut -c 1-4)

# If the hashes are the same, make an initial modification to the files
if [ "$permissions1_hash" == "$permissions2_hash" ]; then
    echo -n " " >> $permissions1_file
    echo -n "  " >> $permissions2_file
fi

# Now start the loop to find matching hashes
while true; do
    permissions1_hash=$(md5sum $permissions1_file | cut -c 1-4)
    permissions2_hash=$(md5sum $permissions2_file | cut -c 1-4)
    if [ "$permissions1_hash" == "$permissions2_hash" ]; then
        break
    fi
    echo -n " " >> $permissions1_file
    echo -n "  " >> $permissions2_file
done

echo "The first 16 bits of the MD5 hash of both files now match!"