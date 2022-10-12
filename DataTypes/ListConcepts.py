# used to store multiple items, ordered, changeable, allow duplicates

# syntax
thislist = ["apple", "banana", "cherry"]
print(thislist)

# length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# list with duplicate and multiple data types elements
dup_list = ["apple", "banana", "cherry", "apple", "cherry", 34, 34, True]
print(dup_list)

# list constructor
thislist = list(("apple", "banana", "cherry"))
print(thislist)

# append method
thislist = ["apple", "banana", "cherry"]
thislist.append("mango")
print(thislist)

# reverse method
thislist = ["apple", "banana", "cherry"]
thislist.reverse()
print(thislist)

# pop method
thislist = ["apple", "banana", "cherry"]
thislist.pop(2)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.extend ("mango")
print(thislist)



