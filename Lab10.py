# Lab 10
# Author: Maksym Fedenko

# Lab 10 will show demonstrate how Dictionary's work in Python.

# 1. Create a dictionary called my_dict with the following key value pairs:
# Key: "name", Value: "John"
# Key: "age", Value: 30
# Key: "city", Value: "Trenton"
# Key: "state", Value: "New Jersey"
my_dict = {"name": "Jhon", "age": 30, "city": "Trenton", "state": "New Jersey"}

# 2. Print out the dictionary.
print(my_dict)

# 3. Print out the value for the key "name".
print(my_dict["name"])
# 4. Lookup the key associated with the value "New Jersey" and print it out.
# Hint 1: You will need to loop through the dictionary.
# Hint 2: remember you can use the .items() method to get the key and value.
for key, value in my_dict.items():
    if value  == "New Jersey":
        print(key)
# 5. Add a new key value pair to the dictionary.
# Key: "country", Value: "USA"
my_dict["country"] = "USA"

# 6. Print out the dictionary.
print(my_dict)
# 7. Remove the key value pair with the key "city".
my_dict.pop("city")
# 8. Print out the dictionary.
print(my_dict)
# 9. Create a dictionary called cities with an key as the City name and values as a list that contains the state, population, and country.
# use the following data:
# Trenton, New Jersey, 84,913, USA
# New York City, New York, 8,336,817, USA
# Los Angeles, California, 3,979,576, USA
# Chicago, Illinois, 2,693,976, USA
# Houston, Texas, 2,320,268, USA
# Phoenix, Arizona, 1,680,992, USA
# Philadelphia, Pennsylvania, 1,584,138, USA
# San Antonio, Texas, 1,547,253, USA
# San Diego, California, 1,423,851, USA
cities = {
    "Trenton": {"state": "New Jersey", "population": 84913, "country": "USA"},
    "New York City": {"state": "New York", "population": 8336817, "country": "USA"},
    "Los Angeles": {"state": "California", "population": 3979576, "country": "USA"},
    "Chicago": {"state": "Illinois", "population": 2693976, "country": "USA"},
    "Houston": {"state": "Texas", "population": 2320268, "country": "USA"},
    "Phoenix": {"state": "Arizona", "population": 1680992, "country": "USA"},
    "Philadelphia": {"state": "Pennsylvania", "population": 1584138, "country": "USA"},
    "San Antonio": {"state": "Texas", "population": 1547253, "country": "USA"},
    "San Diego": {"state": "California", "population": 1423851, "country": "USA"}
}


# 10. Print a table of the data using the pandas library.
# pip install pandas
import pandas as pd

df = pd.DataFrame(cities)
print ("________________________________")
print(df)
# 11. Use the tabulate library to print out the table.
# pip install tabulate
from tabulate import tabulate

# 12. Print out the population for the city of Chicago.
pretty_table = tabulate(df, headers="keys", tablefmt="psql")
print("___________________________")

print(pretty_table)

print(cities["Chicago"].get("population"))
# 13. **Extra** An alternative to converting a dictionary into a pandas df then tabulate, you can use dictionary unpacking and tabulate.
# Dictionary unpacking is a new feature in Python 3.9 and allows you to unpack a dictionary into a list of dictionaries.
# You can then use tabulate to print out the table.

# In our case, {"City": city, **info} creates a new dictionary that includes a "City" key with the city name and all the key-value pairs from the info dictionary.

# For example, if city is "Chicago" and info is {"state": "Illinois", "Population": 2693976, "Country": "USA"}, the new dictionary will be {"City": "Chicago", "state": "Illinois", "Population": 2693976, "Country": "USA"}. This is the same as {"City": city, **info}.
# The ** operator unpacks the info dictionary into the new dictionary

# Transform the data
data = [{"City": city, **info} for city, info in cities.items()]
# Print the table using tabulate
print(tabulate(data, headers= "keys", tablefmt="psql"))

# 14. How many cities have a population greater than 1 million? Use a for loop to iterate through the dictionary.
count = 0

for city in cities:
    if cities[city]["population"] > 1000000:
        count +=1
print(f"cities with population greater then 1 million: {count}")
# 15.  How many cities are in the USA? Use .items() to get a list of tuples. Use a for loop to iterate through the list of tuples.
# Hint 1: You will need to use the second item in the tuple. The second item is a dictionary. IE. for city, info in cities.items():

count = 0
print(cities.items())
for city, info in cities.items():
    if info["country"] == "USA":
        count += 1
print(f"cities that are in USA: {count}")