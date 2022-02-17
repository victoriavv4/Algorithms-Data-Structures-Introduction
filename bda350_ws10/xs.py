import random


def insertionSort_mod(values):
    k = 0
    n = len(values) - 1
    comparisons = 0
    while k + 1 <= n:
        i = k + 1
        curr_val = values[i]
        comparisons += 1
        while i > 0 and values[i - 1] > curr_val:
            values[i] = values[i - 1]
            i = i - 1
            comparisons += 1
        values[i] = curr_val
        k = k + 1
    return comparisons, values


print(insertionSort_mod([1, 2, 3, 55, 5, 6, 8, 7, 9, 111]))
