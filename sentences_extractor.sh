#!/bin/bash

echo "------- START -------"

rm -r outputs/sentences/*

for entry in "./input"/*
do
  filename=$(basename $entry .txt)
  cat ./input/$filename.txt | ./package/shaper.py | ./package/sentencer.py > ./outputs/sentences_extractor/$filename.txt
  echo $filename
done

echo "------- END -------"
