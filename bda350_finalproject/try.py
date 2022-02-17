def print_anagrams(self):
    rows = []

    for item in self.words_grouped:
        temp = []
        left = ', '.join(self.words_grouped[item].keys())
        right = sum(self.words_grouped[item].values())
        temp.append(left)
        temp.append(right)
        rows.append(temp)

    headers = ["Anagrams", "Frequency"]
    x = '-'
    print(x * 10, "Anagram Finder", x * 10)
    print(tabulate(rows, headers, tablefmt="fancy_grid"))