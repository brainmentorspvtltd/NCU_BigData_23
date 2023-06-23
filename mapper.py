#!C:/Python310/python
import sys

# user_input = sys.stdin
# print(user_input)
for line in sys.stdin:
    # remove leading and trailing white space
    line = line.strip()
    # tokenize line into individual words
    words = line.split()
    for word in words:
        print(f"{word}\t{1}")