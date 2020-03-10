from googletrans import Translator
translator = Translator()

file = open('filteredWords.txt', "r")
file2= open("seedlexocon_gen2.txt", "w")


# for line in file:
#     result = translator.translate(line, src='ru', dest='uk')
#     file2.write(line.rstrip() + " " + result.text + "\n")


