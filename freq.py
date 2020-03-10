
Text = open("general.txt").read()
Freq = open("freq_general_ru.txt", "w")

#replace punctuation at the end of the words with space + lowcase
for char in '!?»—-«.,\n':
    Text = Text.replace(char, ' ')
Text = Text.lower()

# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = Text.split()

# Initializing Dictionary
d = {}

# counting number of times each word comes up in list of words (in dictionary)
for word in word_list:
    d[word] = d.get(word, 0) + 1

#Make a list (frew,word) with decreasing frequency
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
word_freq.sort(reverse=True)

freqwords = word_freq [0:4999]
for (freq, word) in freqwords:
    Freq.write(word + "\n")


