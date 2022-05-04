#!/bin/sh
Source=$1
Size=$2
Chips=$3
Weight=$4

printf "Source,Size,Chips,Weight\n%s,%s,%s,%s" "$Source" "$Size" "$Chips" "$Weight" > /app/data/new.csv
sleep 0.2;cat /app/data/result.txt;rm /app/data/result.txt