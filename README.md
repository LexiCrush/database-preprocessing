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
[SQLalchemy, MySQLdb.connect(), .to_sql()](https://stackoverflow.com/a/48393139/21242190)

# Ethics 
1. We accept full responsibility for our work.
      The negative and positive aspects of our game are the product of our work. 
2. Provided service in our areas of competence, being honest and forthright about any limitations in our experience and education.
      We had to modify our original plan to account for some limitations in our knowledge. 
3. Strived to fully understand the specifications for software on which we worked.
      We looked through online documentation to understand the softwares used. 
4. Assisted colleagues in professional development.
      We helped each other overcome any obstacles or worked on certain parts together if we were struggling on our own. 
5. Credited fully the work of others and refrained from taking undue credit.
      We divided up tasks for each of us to avoid taking undue credit. 
6. Ensured proper and achievable goals and objectives for the project.
      We made sure our project consisted of tasks we can properly implement, even if this meant revising our original plan. 
7. Assigned work only after taking into account appropriate contributions of education and experienced tempered with a desire to further that education and experience.
      We each decided to work on parts of the project that we had some familiarity with and areas that we are interested in. 
8. Used only accurate data derived by ethical and lawful means and used it only in ways properly authorized.
      All data used to produce our game was obtained legally from publically accessible sites and was not used inappropriately.  
9. Improved our understanding of the software and related documents on which we worked and of the environment in which they will be used.
      We used online sources to understand how the softwares we used could be used to implement different aspects of our project.     
10. Did not influence others to undertake any action that involved a break of this Code.
      We ensured that each of us were abiding by this Code and did not convince anyone to go against this Code. 
