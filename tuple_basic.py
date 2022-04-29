# are unchangeable, allow duplicates, ordered
# tuple constructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# len method
thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

# tuple with different data types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5 ,3, 7, 9)
tuple3 = (True, False, True) 
print(tuple1, tuple2, tuple3)

# can contain different data types
tuple_m = ("apple", 23, True, 100, "male")
print(tuple_m)

# type()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
