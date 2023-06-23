#!C:/Python310/python
import sys

currentCount = 0
currentWord = None

for line in sys.stdin:
    line = line.strip()
    word, count = line.split("\t",1)
    # by default type of count will be string
    # type cast count into int
    count = int(count)
    if currentWord == word:
        currentCount += count
    else:
        if currentWord:
            print(f"{currentWord}\t{currentCount}")
        currentCount = count
        currentWord = word

# print the last remaining word if it is left
if currentWord == word:
    print(f"{currentWord}\t{currentCount}")