abc = "Jack Challengingly"
list_1 = []
list_2 = []

for i in range(len(abc)):
    if i % 2 == 0:
        list_2.append(abc[i])
    else:
        list_1.append(abc[i])

print("Even", list_2)
print("odd", list_1)
