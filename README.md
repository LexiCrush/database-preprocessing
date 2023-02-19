# Generate-Noun-Banks

## Setup Env

1. Install Python >= 3.7
2. Install Pandas with pip: `pip install pandas`
3. Import Built In 'csv' Module



## Data Preprocessing

The data preprocessing process consists of three steps:

1. Load Nouns from harvested .csv files.
2. Clean the data by removing any unnecessary characters, duplicate entries, or violations of *LexiCrush's game logic*.
3. Load each NounBank as a Pandas Dataframe.

The code for the data preprocessing process is located in the preprocess directory.

To run the code, clone this repo and enter the following command in the terminal:

```
➜  Generate-Noun-Banks git:(main) ✗ python preprocess/pre_process.py
```

DO STUFF

## Data Harvesting
[USA States Surface Area](https://github.com/jakevdp/data-USstates/blob/master/state-areas.csv)<br>
[World Countries - Population](https://data.worldbank.org/indicator/SP.POP.TOTL)<br>
[Word Countries - Surface Area](https://data.worldbank.org/indicator/AG.SRF.TOTL.K2)<br>
[Big List of Animals](https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54)<br>
