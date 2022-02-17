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



    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


@timer
def selectionSort(arr):
    count = 0
    x = len(arr)
    for i in range(x):
        min_index = i
        for j in range(i + 1, x):
            if arr[j] < arr[min_index]:
                min_index = j

        swap(arr, min_index, i)
        count += 1

    return arr


@timer
def bubbleSort(arr):
    x = len(arr)
    count = 0
    for i in range(x - 1):
        for j in range(x - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j + 1, j)
                count += 1

    return arr


@timer
def insertionsSort(arr):
    count = 0
    # traverse through 1 to length of array
    for i in range(1, len(arr)):
        pointer = arr[i]
        # move elements of arr[0... i-1] that are greater than pointer to one position ahead of current position
        j = i - 1
        while j >= 0 and pointer < arr[j]:
            swap(arr, j + 1, j)
            count += 0
            j -= 1

    return arr


@timer
def mergeSort(arr):
    if len(arr) > 1:
        # find the midpoint of array
        mid = len(arr) // 2
        # dividing the array elements
        left = arr[:mid]
        right = arr[mid:]

        # sorting the first half
        mergeSort(left)
        # sorting the second half
        mergeSort(right)

        # initializing variable
        i = j = k = 0

        # copy data to temp arrays left[] right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # checking if there are any remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


@timer
def quickSort(arr):
    count = 0
    # base case
    if len(arr) < 2:
        return arr

    # position of the partitioning element
    current_pos = 0

    # partitioning loop
    for i in range(1, len(arr)):
        if arr[i] <= arr[0]:
            current_pos += 1
            swap(arr, i, current_pos)
            count += 1

    swap(arr, 0, current_pos)
    count += 1
    # bring pivot to appropriate position

    # sorts elements to the left of pivot
    left = quickSort(arr[:current_pos])

    # sorts elements to right of pivot
    right = quickSort(arr[current_pos + 1: len(arr)])

    # merging left and right sides together
    arr = left + [arr[current_pos]] + right

    return arr


# def exchange(arr):


def comparisons(arr):
    comp = (len(arr) * (len(arr) - 1)) // 2
    return comp


def main():
    new = '\n'
    user_input1 = int(input(f'Please enter{new} 1 for Bubble Sort{new} 2 for Selection Sort{new} 3 for Insertion Sort/'
                            f'{new} 4 for Merge Sort{new} 5 for Quick Sort{new} 0 to Exit{new}'))

    if user_input1 >= 1:
        user_input = int(input(f'Press 0 to enter your own list or press 1 for the program to generate its own list'))

        if user_input == 0:
            user_input_size = int(input(f'Please enter the size of your list: '))
            user_input_list = input(f'Please enter your list: ')
            user_list = user_input_list.split()
            for val in range(len(user_list)):
                user_list[val] = int(user_list[val])

            if user_input == 1:
                if len(user_list) <= 10:
                    print(bubbleSort(user_list))
            elif user_input == 2:
                if len(user_list) <= 10:
                    print(selectionSort(user_list))
            elif user_input == 3:
                if len(user_list) <= 10:
                    print(insertionsSort(user_list))
            elif user_input == 4:
                if len(user_list) <= 10:
                    print(mergeSort(user_list))
            else:
                if len(user_list) <= 10:
                    print(quickSort(user_list))
            print(f'Problem Size: {user_input_size}')
            print(f'Comparisons:{comparisons(user_list)}')
            print(f'Exchanges:{count}')

        else:
            user_input_size2 = int(input(f'Please enter the size of your list: '))
            arr = [random.randint(0, 100) for i in range(user_input_size2)]
            if user_input == 1:
                print(bubbleSort(arr))
            elif user_input == 2:
                print(selectionSort(arr))
            elif user_input == 3:
                print(insertionsSort(arr))
            elif user_input == 4:
                print(mergeSort(arr))
            else:
                print(quickSort(arr))
            print(f'Problem Size: {user_input_size2}')
            print(f'Comparisons:{comparisons(arr)}')
            # print(f'Exchanges:{count}')


if __name__ == "__main__":
    main()
