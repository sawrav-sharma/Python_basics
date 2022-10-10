string1 = "olo"
string2 = ''.join(reversed(string1))
print(string2)
if string2 == string1:
    print(True)
else:
    print(False)
