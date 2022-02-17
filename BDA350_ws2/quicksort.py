import random
import time


def quickSort(arr):
    start_time = time.time()
    exchange = 0

    if len(arr) == 1:
        elapsed_time = time.time() - start_time
        return arr, exchange, elapsed_time

    pivot = arr[0]
    right = []
    left = []
    mid_point = len(arr) // 2

    for i in range(1, len(arr)):
        if arr[i] >= pivot:
            right.append(arr[i])
            if i < mid_point:
                exchange += 1

        else:
            left.append(arr[i])
            if i >= mid_point:
                exchange += 1


    left_r, l_exch, time_l = quickSort(left)
    right_r, r_exch, time_r = quickSort(right)

    exchange += r_exch + l_exch


    elapsed_time = time.time()- start_time
    elapsed_time += time_l + time_r

    return left_r + [pivot] + right_r, exchange, elapsed_time





def main():
    rand_num = [random.randint(0, 20) for i in range(5)]
    print(quickSort(rand_num))


if __name__ == "__main__":
    main()
