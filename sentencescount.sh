#!/bin/bash

echo "------- START -------"

rm -r outputs/sentences/*

for entry in "./input"/*
do
  filename=$(basename $entry .txt)
  cat ./input/$filename.txt | ./package/shaper.py | ./package/sentencer.py | sort -k1,1 | ./package/reducer.py > ./outputs/sentences/$filename.csv
  echo $filename
done

echo "------- END -------"
