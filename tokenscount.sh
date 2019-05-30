#!/bin/bash

echo "------- START -------"

rm -r outputs/tokens/*

for entry in "./input"/*
do
  filename=$(basename $entry .txt)
  cat ./input/$filename.txt | ./package/mapper.py | sort -k1,1 | ./package/reducer.py > ./outputs/tokens/$filename.csv
  echo $filename
done

echo "------- END -------"
