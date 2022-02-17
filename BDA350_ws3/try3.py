x = [1, 2, 4, 5, 6, 3, 5, 4]

i = 1
while i < len(x):
    insert_item = x[i]
    j = i - 1
    while j >= 0:
        if insert_item < x[j]:
            x[j + 1] = x[j]
            j -= 1
        else:
            break
    x[j + 1] = insert_item
    i += 1

print(x)

