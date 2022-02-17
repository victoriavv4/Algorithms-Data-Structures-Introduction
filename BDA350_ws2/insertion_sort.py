import random


def insertionsSort(arr):
    # traverse through 1 to length of array
    for i in range(1, len(arr)):
        pointer = arr[i]
        # move elements of arr[0... i-1] that are greater than pointer to one position ahead of current position
        j = i - 1
        while j >= 0 and pointer < arr[j]:
            swap(arr, j + 1, j)
            j -= 1

    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def main():
    rand_num = [random.randint(0, 20) for i in range(5)]
    print(insertionsSort(rand_num))


if __name__ == "__main__":
    main()
