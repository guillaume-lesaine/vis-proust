#!/bin/bash

echo "------- START -------"

rm -r output_tokens/*

for entry in "./input"/*
do
  filename=$(basename $entry .txt)
  cat ./input/$filename.txt | ./package/mapper.py | sort -k1,1 | ./package/reducer.py > ./output_tokens/$filename.csv
  echo $filename
done

echo "------- END -------"
