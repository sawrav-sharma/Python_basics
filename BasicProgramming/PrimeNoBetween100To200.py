lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Prime Numbers in the range are: ")

for i in range(lower_value, upper_value + 1):
    if i > 1 and i % 2 == 0:
        pass
    else:
        print("Prime numbers between 100 to 200 : ", + i)
