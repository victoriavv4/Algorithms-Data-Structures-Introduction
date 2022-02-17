import random
import time


def bubbleSort(nums):
    start2 = time.time()
    x = len(nums)

    for i in range(x - 1):
        for j in range(x - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j + 1, j)


    end2 = time.time()
    total2 = end2 - start2
    print(f"{total2:8f}")
    return nums


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def main():
    nums = [random.randint(0, 20) for i in range(5)]
    print(bubbleSort(nums))


if __name__ == "__main__":
    main()
