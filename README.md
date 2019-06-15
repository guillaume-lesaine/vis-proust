# vis-proust

**Marcel Proust** wrote **"À la recherche du temps perdu"** ("In Search of the Lost Time") between 1906 and 1922. It is considered to be one of the master-pieces of the French Litterature. The text spans over seven volumes and thousands of pages. Being an admirer of the book, I decided do some statistics around its structure and content using **Python** for the data processing and **Observable** for the presentation of the results.

Available in this repository:
- Python Map / Reduce code to do the extraction of text features
- Python code relying on pandas to do the data crunching
- Package functions tests written with Pytest
- The source CSV data and the refined CSV files feeding the notebook

# Setup

All the following commands must be run from the root of the directory.

To create the virtual environement run :

```console
virtualenv -p python3 proust_env
```

To access it run :

```console
source proust_env/bin/activate
```

The install the required packages with the requirements :

```console
pip install
```

Run this initial command to setup directory structure

```console
./setup.sh
```

The initial data processing scripts are launched with bash. In order to make a script executable on macOS, run:

```console
chmod 755 ./path/file.ext
```
# Usage

## Map Reduce - Tokens counter

To generate the text outputs for the count of tokens, run:

```console
./tokens_counter.sh
```

## Map Reduce - Ngrams counter

To generate the text outputs for the count of ngrams, with n in [2, 3, 4, 5], run:

```console
./ngrams_counter.sh n
```

## Map Reduce - Sentences counter

To generate the text outputs for the count of words in sentences, run:

```console
./sentences_counter.sh
```

## Map Reduce - Sentences extractor

To generate the sentences of the text, run:

```console
./sentences_extractor.sh
```

## Data Processing - main.py

```console
python3 consolidator.py --case tokens
```

```console
python3 searcher.py --case tokens_cities
```
