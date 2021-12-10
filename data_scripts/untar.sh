#! /bin/bash
for dir in ../../data/*/*/*; do
   #gzip -d "$dir"
   echo gzip $dir
done
