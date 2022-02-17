import matplotlib.pyplot as plt

# data
xaxis = [5, 10, 50, 100, 200, 1000]
selection_times = [0.000008, 0.000015, 0.000154, 0.000456, 0.001707, 0.075416]
bubble_times = [0.000013, 0.000018, 0.000698, 0.004025, 0.006630, 0.225285]

plt.plot(xaxis, selection_times, label="selection_sort", c="green")
plt.plot(xaxis, bubble_times, label="bubble_sort", c="blue")


# set chart title and axis labels
plt.title("Selection Sort vs Bubble Sort Run Times(sec)", fontsize=16)
plt.xlabel("Number of List Items")
plt.ylabel("TIme(seconds)")

plt.legend()
plt.show()












