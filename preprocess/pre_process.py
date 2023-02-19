
try: 
    import csv
    import pandas as pd
except ImportError:
    print("Install Modules")


def preprocess_one_col_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\n') #read animals.csv with '\n' as the delimiter
        animal_list = list(reader)
    animal_list = [x[0] for x in animal_list] # make a list of the animals
    lowercase_animal_list = [x.lower() for x in animal_list] # lowercase
    lowercase_animal_list = list(dict.fromkeys(lowercase_animal_list)) # remove duplicates
    lowercase_animal_list = [x for x in lowercase_animal_list if x != ''] # remove empty strings
    lowercase_animal_list.sort() # sort alphabetically
    #convert to pandas dataframe
    df = pd.DataFrame(lowercase_animal_list, columns=['Animal'])
    return df

def preprocess_states_csv(filename):
    #read the csv file with pandas, the column names are 'state' and 'area (sq. mi)'
    df = pd.read_csv(filename, names=['state', 'area (sq. mi)','pop_2014'])
    df = df.iloc[1:].reset_index(drop=True) # remove the first row, which is the column names and reset the index
    return df

def preprocess_countries_csv(filename):
    #read the csv file with pandas, the column names are 'country' and 'area (sq. km)'
    df = pd.read_csv(filename, names=['country', 'area (sq. km)','pop_2021'])
    df = df.iloc[1:].reset_index(drop=True) # remove the first row, which is the column names and reset the index
    return df

def preprocess_elements_csv(filename):
    #read the csv file with pandas, the column names are 'element' and 'atomic number'
    df = pd.read_csv(filename)
    # df = df.iloc[1:].reset_index(drop=True) # remove the first row, which is the column names and reset the index
    return df


all_animals = preprocess_one_col_csv('./nounbanks/ANIMALS.csv')
usa_states = preprocess_states_csv('./nounbanks/USA_STATES.csv')
all_countries = preprocess_countries_csv('./nounbanks/COUNTRIES.csv')
all_elements = preprocess_elements_csv('./nounbanks/ELEMENTS.csv')
greek_gods = preprocess_one_col_csv('./nounbanks/GREEKGODS.csv')
roman_gods = preprocess_one_col_csv('./nounbanks/ROMAN_GODS.csv')
cosmetic_items = preprocess_one_col_csv('./nounbanks/COSMETIC_ITEMS.csv')
office_supplies = preprocess_one_col_csv('./nounbanks/OFFICE_SUPPLIES.csv')
disney_movies = preprocess_one_col_csv('./nounbanks/DISNEY_MOVIES.csv')
body_parts = preprocess_one_col_csv('./nounbanks/BODY_PARTS.csv')
college_majors = preprocess_one_col_csv('./nounbanks/COLLEGE_MAJORS.csv')
candy = preprocess_one_col_csv('./nounbanks/CANDY.csv')
dogs = preprocess_one_col_csv('./nounbanks/DOGS.csv')
mythical_creatures = preprocess_one_col_csv('./nounbanks/MYTHICAL_CREATURES.csv')




print(usa_states.head(20))
print("\n\n\n")
print(all_animals.head(20))
print("\n\n\n")
print(all_countries.head(20))
print("\n\n\n")
print(all_elements.head(20))
print("\n\n\n")
print(greek_gods.head(20))
print("\n\n\n")
print(roman_gods.head(20))
print("\n\n\n")
print(cosmetic_items.head(20))
print("\n\n\n")
print(office_supplies.head(20))
print("\n\n\n")
print(disney_movies.head(20))
print("\n\n\n")
print(body_parts.head(20))
print("\n\n\n")
print(college_majors.head(20))
print("\n\n\n")
print(candy.head(20))
print("\n\n\n")
print(dogs.head(20))
print("\n\n\n")
print(mythical_creatures.head(20))