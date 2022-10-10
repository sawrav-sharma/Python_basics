thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# to get the value or print the particular field
print(thisdict.get("model"))
# to get the value or print the particular field
x = thisdict["model"]
print(x)

# to get the keys of dictionary
print(thisdict.keys())

# to add something in dictionary
thisdict["color"] = "red"
print(thisdict)
print(thisdict.get("color"))

# to update something in dictionary

print(thisdict)

# to change something in dictionary
thisdict["year"] = 1996
print(thisdict)

# to remove something from the dictionary
thisdict.pop("model")
print(thisdict)

# loop through dictionaries
for x, y in thisdict.items():
    print(x, " -> ", y)

for x in thisdict.keys():
    print(x)

for x in thisdict.values():
    print(x)

# copy dictionary
newdict = thisdict.copy()
print(newdict)

newdict = dict(thisdict)
print(newdict)
