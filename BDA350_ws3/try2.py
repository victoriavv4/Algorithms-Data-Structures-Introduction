x = [1, 2, 4, 5, 6, 5, 5, 5]
# i will equal like second last item in the array
i = x[- 2]
index = 3
value = 11

while i >= 0:
    x[i + 1] = x[i]
    i -= 1
x[index] = value

print(x)
""" To begin, i is equal to the second last """

