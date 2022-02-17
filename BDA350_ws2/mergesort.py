import random
import time


def merge(left, right):
    exchange = 0
    temp_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp_list.append(left[i])
            i += 1
        else:
            temp_list.append(right[j])
            j += 1
            exchange += 1
    while i < len(left):
        temp_list.append(left[i])
        i += 1
    while j < len(right):
        temp_list.append(right[j])
        j += 1
    return temp_list, exchange


def mergeSort(arr):
    start_time = time.time()
    exchange = 0

    if len(arr) == 1:
        elapsed_time = time.time() - start_time
        return arr, exchange, elapsed_time
    midpoint = len(arr) // 2
    left, l_exch, time_l = mergeSort(arr[:midpoint])
    right, r_exch, time_r = mergeSort(arr[midpoint:])

    temp_list, exchange = merge(left, right)

    exchange += l_exch + r_exch

    elapsed_time = time.time() - start_time
    elapsed_time += time_l + time_r

    return f'{temp_list', exchange, elapsed_time


def main():
    rand_num = [random.randint(0, 20) for i in range(5)]
    print(mergeSort(rand_num))


if __name__ == "__main__":
    main()
