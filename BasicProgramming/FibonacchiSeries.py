"""Fibonacci series"""
N = int(input("Number of element: "))
fibonacciSeries = [0, 1]
if N > 2:
    for i in range(2, N):
        nextElement = fibonacciSeries[i - 1] + fibonacciSeries[i - 2]
        fibonacciSeries.append(nextElement)
print(fibonacciSeries)
