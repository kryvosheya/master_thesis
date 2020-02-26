#!/usr/bin/python
import codecs
from collections import Counter

file = codecs.open("general.txt", "r", "utf-8")
counter = Counter()
for line in file:
    words = line.split(" ")
    tempCounter = Counter(words)
    counter = counter + tempCounter
file.close()

print("All words: ", sum(counter.values()))
print("Uniq words: ", len(list(counter)))