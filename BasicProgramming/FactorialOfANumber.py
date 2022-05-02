"Factorial of a number"
num = 7
factorial = 1
if num<=0:
    print("Sorry, this factorial does not exist")
else:
    for i in range(1,num+1):
        factorial = factorial * i
        print("The factorial of ",num,"is",factorial)
