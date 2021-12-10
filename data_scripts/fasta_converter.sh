#! /bin/bash

mapfile -d $'\0' myArray < <(find ../../data/*/*/* -name "*" -print0)

for i in "${myArray[@]}"; do
   gzip -d -v "$i"
done

mapfile -d $'\0' newArray < <(find ../../data/*/*/* -name "*" -print0)

for i in "${newArray[@]}"; do
   sed -n '1~4s/^@/>/p;2~4p' "$i" > "${i%.*}.fasta"
   rm "$i"
done
