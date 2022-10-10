def findPeak(peakElement, n):
    if n == 1:
        return 0
    if peakElement[0] >= peakElement[1]:
        return 0
    if peakElement[n - 1] >= peakElement[n - 2]:
        return n - 1

    for i in range(1, n - 1):
        if peakElement[i] >= peakElement[i - 1] and peakElement[i] >= peakElement[i + 1]:
            return i


arr = [1, 3, 20, 4, 1, 0]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
