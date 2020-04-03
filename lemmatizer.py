import pymorphy2
morph = pymorphy2.MorphAnalyzer()
file = open('gold_general.txt', "r")
file2 = open('gold_general_lemmatized.txt', "w")

lemmas = set()
for line in file:
    word = line.rstrip()
    p = morph.parse(word)[0]
    #print( word + "\t" + p.normal_form)
    lemmas.add(p.normal_form)

for lemma in lemmas:
    file2.write(str(lemma) + "\n")

print(len(lemmas))

