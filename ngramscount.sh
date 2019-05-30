#!/bin/bash

echo "------- START -------"

rm -r output_ngrams/*

for entry in "./input"/*
do
  filename=$(basename $entry .txt)
  cat ./input/$filename.txt | ./package/shaper.py | ./package/ngrammer.py | sort -k1,1 | ./package/reducer.py > ./output_ngrams/$filename.csv
  echo $filename
done

echo "------- END -------"
