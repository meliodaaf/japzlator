#!/usr/bin/env python3


import time

def prog_bar(progress, total):
    percent = 100 * (progress / float(total))
    percent = int(percent)
    bar = "█" * percent + "-" * (100 - percent)
    print(f"\r|{bar}| {percent:.2f}%", end="\r")


# numbers = [x * 5 for x in range(2000, 3000)]
# results = []

# prog_bar(0, len(numbers))
# for i, x in enumerate(numbers):
#     results.append(math.factorial(x))
#     prog_bar(i + 1, len(numbers))

with open("words.txt", "r") as file:
    words = file.readlines()
    lines = []
    prog_bar(0, len(words))

    for i, x in enumerate(words):
        lines.append(x)
        prog_bar(i + 1, len(words))