import random
from time import time


def selection_sort(lst):
    time_start = time()

    exchange = 0
    comparison = 0
    for i in range(len(lst) - 1):
        min_index = i  # create the index of minimum number

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
            comparison += 1
        # compare the current number and the next number,
        # re-designate the minimum number index if next number is smaller

        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i]
            exchange += 1
        # swap with next number when the next number is smaller as min_index will be re-designated

    time_end = time()
    time_spend = time_end - time_start

    return lst, comparison, exchange, time_spend


def bubble_sort(lst):
    time_start = time()

    exchange = 0
    comparison = 0
    for i in range(1, len(lst)):
        for j in range(0, len(lst) - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                exchange += 1
            comparison += 1
    # compare current number with the next number, swap positions if next number is smaller

    time_end = time()
    time_spend = time_end - time_start

    return lst, comparison, exchange, time_spend


def insertionSort(lst):
    time_start = time()

    exchange = 0
    comparison = 0

    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            exchange += 1
            comparison += 1
            # shift all elements greater than current key one position forward(to the right)

        lst[j + 1] = key  # re-assign the key to one position ahead of the shifted elements
        comparison += 1

    time_end = time()
    time_spend = time_end - time_start

    return lst, comparison, exchange, time_spend


def merge(left, right):
    count = 0
    comp = 0
    merged_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_list.append(left[i])
            i += 1
        else:
            .append(lst_right[j])
            j += 1
            exchange += 1
        comparison += 1
    while i < len(lst_left):
        concat_lst.append(lst_left[i])
        i += 1
    while j < len(lst_right):
        concat_lst.append(lst_right[j])
        j += 1
    return concat_lst, comparison, exchange


def mergeSort(arr):
    start = time.time()
    count = 0
    comp = 0

    if len(lst) == 1:
        elapsed_time = time.time() - start
        return lst, comparison, exchange, time_spend
    middle = len(lst) // 2
    left, comparison_left, exchange_left, time_left = merge_sort(lst[:middle])
    right, comparison_right, exchange_right, time_right = merge_sort(lst[middle:])

    concat_lst, comparison, exchange = merge(left, right)

    comparison += comparison_right + comparison_left
    exchange += exchange_right + exchange_left

    time_end = time()
    time_spend = time_end - time_start
    time_spend += time_left + time_right

    return concat_lst, comparison, exchange, time_spend


def main():
    while True:
        try:
            method_selection = int(input('Please enter\n'
                                         '1 for Bubble Sort\n'
                                         '2 for Selection Sort\n'
                                         '3 for Insertion Sort\n'
                                         '4 for Merge Sort\n'
                                         '5 for Quick Sort\n'
                                         '0 to Exit\n'))

            if method_selection not in range(0, 6):
                raise ValueError

            if method_selection == 0:
                print("bye, have a nice day!")
                break

            method_lst = [bubble_sort, selection_sort, insertionSort, merge_sort, quickSort]

            list_selection = input('Press 0 to enter your own list or press 1 '
                                   'for the program to generate a random list\n')

            if list_selection not in ['0', '1']:
                raise ValueError

            list_size = int(input('Enter the size of your list:'))

            input_lst = []

            if list_selection == '0':
                input_lst = [int(x) for x in input('Enter your list: (example: 1 3 4 5 6)\n').split()]
                if len(input_lst) != list_size:
                    print('given list length does not match pre-set list length! please try again\n')
                    continue

            elif list_selection == '1':
                input_lst = random.sample(range(1, list_size + 50), list_size)

            if method_selection in range(1, 6):
                result_lst, result_comparison, result_exchange, result_time_spend \
                    = method_lst[method_selection - 1](input_lst)
                if list_size <= 10:
                    print(result_lst)
                print(f'Problem size: {list_size}\n'
                      f'Elapsed time: {result_time_spend:.10f}\n'
                      f'Comparisons: {result_comparison}\n'
                      f'Exchanges: {result_exchange}\n')
                continue

        except ValueError:
            print('invalid input! please try again.\n')
            continue


if __name__ == '__main__':
    main()

