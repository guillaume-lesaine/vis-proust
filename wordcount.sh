#!/bin/bash

echo "------- START -------"

rm -r output/*

for entry in "./input"/*
do
  filename=$(basename $entry .txt)
  cat ./input/$filename.txt | ./package/mapper.py | sort -k1,1 | ./package/reducer.py > ./output/$filename.csv
  echo $filename
done

echo "------- END -------"
