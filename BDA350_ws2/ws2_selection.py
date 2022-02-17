import random
import time


def timer(func):
    def func_wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'\n{func.__name__} Elapsed time: {elapsed_time} s\n')
        return result

    return func_wrapper


@timer
def selectionSort(rand_num):
    x = len(rand_num)
    for i in range(x):
        min_index = i
        for j in range(i + 1, x):
            if rand_num[j] < rand_num[min_index]:
                min_index = j

        swap(rand_num, min_index, i)

    return rand_num


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def main():
    rand_num = [random.randint(0, 20) for i in range(10)]
    print(selectionSort(rand_num))


if __name__ == "__main__":
    main()
