lyst = [1, 4, 6, None, None]
capacity = [1, 2, 3]

cap_len = len(capacity)

# length of list = 5 capacity length = 3 so 5 - 3 = 2, so it iterates 2 times and removes the last item at each of those
# iterations (2)
for x in range(len(lyst) - cap_len):
    lyst.pop()
    print(lyst)





















