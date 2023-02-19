# Generate-Noun-Banks

## Setup Env & Run

1. Install Python >= 3.7.
2. Install **Pandas** with pip: `pip install pandas`.
3. Import **'csv'** Module: (Built-In)



## Pre-Processing

1. Load harvested files into `./nounbanks/`.
2. Clean each nounBank (unnecessary characters, duplicate entries, or violations of *LexiCrush* game logic).
3. Convert each noun bank into a Pandas dataframe.
4. Setup up a connection using MySQLdb.
```(python)
from pandas.io import sql 
import MySQLdb
con = MySQLdb.connect()
```
5. Use `df.to_sql()` method to populate a mySQL (configurable) style DB with contents from df.

## Data Sources
[USA States Surface Area](https://github.com/jakevdp/data-USstates/blob/master/state-areas.csv)<br>
[World Countries - Population](https://data.worldbank.org/indicator/SP.POP.TOTL)<br>
[Word Countries - Surface Area](https://data.worldbank.org/indicator/AG.SRF.TOTL.K2)<br>
[Big List of Animals](https://gist.github.com/atduskgreg/3cf8ef48cb0d29cf151bedad81553a54)<br>

## Helpful Links
[SQLalchemy, MySQLdb.connect(), & .to_sql()](https://stackoverflow.com/a/48393139/21242190)
