if user_input == 0:
    user_input_size = int(input(f'Please enter the size of your list: '))
    user_input_list = input(f'Please enter the values of the list separated by a space: ')
    user_list = user_input_list.split()
    for val in range(len(user_list)):
        user_list[val] = int(user_list[val])

    if user_input1 == 1:
        if user_input_size <= 10:
            print(bubbleSort(user_list))
    else:
        bubbleSort(user_list)
    print(f'Problem Size: {user_input_size}')
    print(f'Comparisons:{comparisons(user_list)}')
elif user_input1 == 2:
    if len(user_list) <= 10:
        print(selectionSort(user_list))
    else:
        selectionSort(user_list)
    print(f'Problem Size: {user_input_size}')
    print(f'Comparisons:{comparisons(user_list)}')
elif user_input1 == 3:
    if len(user_list) <= 10:
        print(insertionsSort(user_list))
    else:
        insertionsSort(user_list)
    print(f'Problem Size: {user_input_size}')
    print(f'Comparisons:{comparisons(user_list)}')
elif user_input1 == 4:
    print(mergeSort(user_list))
else:
    size = len(user_list)
    quickSort(user_list, 0, size - 1)
    print(user_list)
print(f'Problem Size: {user_input_size}')
print(f'Comparisons:{comparisons(user_list)}')

else:
user_input_size2 = int(input(f'Please enter the size of your list: '))
arr = [random.randint(0, 100) for i in range(user_input_size2)]
if user_input1 == 1:
    if user_input_size2 <= 10:
        print(bubbleSort(arr))
    else:
        bubbleSort(arr)
elif user_input1 == 2:
    if user_input_size2 <= 10:
        print(selectionSort(arr))
    else:
        selectionSort(arr)
elif user_input1 == 3:
    if user_input_size2 <= 10:
        print(insertionsSort(arr))
    else:
        insertionsSort(arr)
elif user_input1 == 4:
    if user_input_size2 <= 10:
        print(mergeSort(arr))
    else:
        mergeSort(arr)
else:
    size = len(arr)
    quickSort(arr, 0, size - 1)
    if user_input_size2 <= 10:
        print(arr)
    else:
        quickSort(arr, 0, size - 1)
print(f'Problem Size: {user_input_size2}')
print(f'Comparisons:{comparisons(arr)}')