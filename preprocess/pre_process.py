
try: 
    import csv
    import pandas as pd
except ImportError:
    print("Install Modules")


def preprocess_animals_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter='\n') #read animals.csv with '\n' as the delimiter
        animal_list = list(reader)
        
    animal_list = [x[0] for x in animal_list] # make a list of the animals
    lowercase_animal_list = [x.lower() for x in animal_list] # lowercase
    lowercase_animal_list = list(dict.fromkeys(lowercase_animal_list)) # remove duplicates
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


all_animals = preprocess_animals_csv('./nounbanks/ANIMALS.csv')
usa_states = preprocess_states_csv('./nounbanks/USA_STATES.csv')
all_countries = preprocess_countries_csv('./nounbanks/COUNTRIES.csv')
all_elements = preprocess_elements_csv('./nounbanks/ELEMENTS.csv')
greek_gods = preprocess_animals_csv('./nounbanks/GREEKGODS.csv')
roman_gods = preprocess_animals_csv('./nounbanks/ROMAN_GODS.csv')
cosmetic_items = preprocess_animals_csv('./nounbanks/COSMETIC_ITEMS.csv')
office_supplies = preprocess_animals_csv('./nounbanks/OFFICE_SUPPLIES.csv')



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