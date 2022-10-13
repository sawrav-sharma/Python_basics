dict1 = {
    "vehicle": "Jonga",
    "color": "Black",
    "price": 1000,
    "year": 2022
}
print(dict1.values())
print(dict1.keys())
print(dict1.get("price"))

"""The items() method gets the items of a dictionary and return them as a Tuple:"""
for i in dict1.values():
    print(i)

"""Using the keys(), values(), and items() methods, a for loop can iterate over the keys, values, or key-value pairs 
in a dictionary, respectively. """
for key, value in dict1.items():
    print(f'Key : {key}, Value : {value}')

"""The get() method returns the value of an item with by using the key. If the key does not exist, it returns None:"""
print(f'I have {dict1.get("vehicle")} which is {dict1.get("color")} in color, and it costed me {dict1.get("price")} '
      f'dollars, manufactured in year {dict1.get("year")} and it manufacturer company is '
      f'"{dict1.get("vehicleCompany")}"')

"""You can also change the default None value for other of your choice"""
print(f'{dict1.get("companyName", "Nissan")}')
print(dict1)

"""Adding items with setdefault()
   It’s possible to add an item to a dictionary in this way"""
if 'seatingCapacity' not in dict1:
    dict1['seatingCapacity'] = 4
    print(dict1)

"""Checking keys in a Dictionary"""
print('color' in dict1.keys())

"""Checking values in a Dictionary"""
print('Black' in dict1.get("color"))

"""The pop() method removes and return an item based on a given key"""
print(f'Removing year using pop() method')
print(dict1.pop("year"))

"""The popitem() method remove the last item in a dictionary and returns it"""
print(dict1.popitem())

"""The del() method removes an item based on a given key"""
del dict1['color']
print(dict1)

"""The clear() method removes all the items in a dictionary"""

