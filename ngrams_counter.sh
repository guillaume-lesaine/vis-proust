#!/bin/bash

ngrams=$1

echo "------- START -------"

rm -r outputs/ngrams$ngrams/*

for entry in "./input"/*
do
  filename=$(basename $entry .txt)
  cat ./input/$filename.txt | ./package/shaper.py | ./package/ngrammer.py $ngrams | sort -k1,1 | ./package/reducer.py > ./outputs/ngrams$ngrams/$filename.csv
  echo $filename
done

echo "------- END -------"
