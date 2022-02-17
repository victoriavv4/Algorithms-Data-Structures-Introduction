import random
import time


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selectionSort(arr):
    start = time.time()
    count = 0
    comp = 0
    x = len(arr)
    for i in range(x):
        min_index = i
        for j in range(i + 1, x):
            if arr[j] < arr[min_index]:
                min_index = j
            comp += 1

        swap(arr, min_index, i)
        count += 1
    elapsed_time = time.time() - start
    return arr, count, comp, elapsed_time


def bubbleSort(arr):
    start = time.time()
    x = len(arr)
    count = 0
    comp = 0
    for i in range(x - 1):
        for j in range(x - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j + 1, j)
                count += 1
                comp += 1
    elapsed_time = time.time() - start
    return arr, count, comp, elapsed_time


def insertionSort(arr):
    start = time.time()
    count = 0
    comp = 0
    # traverse through 1 to length of array
    for i in range(1, len(arr)):
        pointer = arr[i]
        # move elements of arr[0... i-1] that are greater than pointer to one position ahead of current position
        j = i - 1
        comp += 1
        while j >= 0 and pointer < arr[j]:
            swap(arr, j + 1, j)
            count += 1
            comp += 1
            j -= 1
    elapsed_time = time.time() - start
    return arr, count, comp, elapsed_time


def merge(left, right):
    count = 0
    comp = 0
    merge_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1
            count += 1
        comp += 1
    while i < len(left):
        merge_list.append(left[i])
        i += 1
    while j < len(right):
        merge_list.append(right[j])
        j += 1
    return merge_list, count, comp


def mergeSort(arr):
    start = time.time()
    exchange = 0
    comparison = 0

    if len(arr) < 2:
        elapsed_time = time.time() - start
        return arr, comparison, exchange, elapsed_time
    midpoint = len(arr) // 2
    left, comp_left, count_left, time_left = mergeSort(arr[:midpoint])
    right, comp_right, count_right, time_right = mergeSort(arr[midpoint:])

    merge_list, comp, count = merge(left, right)

    comp += comp_right + comp_left
    count += count_right + count_left

    elapsed_time = time.time() - start
    elapsed_time += time_left + time_right

    return merge_list,  count, comp, elapsed_time








def main():
    while True:
        user_method = int(input('Please enter\n'
                                '1 for Bubble Sort\n'
                                '2 for Selection Sort\n'
                                '3 for Insertion Sort\n'
                                '4 for Merge Sort\n'
                                '0 to Exit\n'))

        methods = [bubbleSort, selectionSort, insertionSort, mergeSort]

        list_method = int(input('Press 0 to enter your own list or press 1 '
                                'for the program to generate a random list: '))

        list_size = int(input('Enter the size of your list:'))

        user_list = []

        if list_method == 0:
            user_input = input("Enter your list values separated by a space: ")
            user_list = user_input.split()
            for val in range(len(user_list)):
                user_list[val] = int(user_list[val])
            if len(user_list) != list_size:
                print('given list length does not match pre-set list length! please try again\n')


        elif list_method == 1:
            user_list = [random.randint(0, 100) for i in range(list_size)]

        if user_method in range(1, 6):
            arr, exch, comp, elapsed = methods[user_method - 1](user_list)
            if list_size <= 10:
                print(arr)
            print(f'Problem size: {list_size}\n'
                  f'Elapsed time: {elapsed:.10f}\n'
                  f'Comparisons: {comp}\n'
                  f'Exchanges: {exch}\n')


if __name__ == "__main__":
    main()
