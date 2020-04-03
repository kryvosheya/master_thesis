import codecs

from docx import Document

wordDoc = Document('general_gold.docx')

keyList = []
valueList = []
tupleList = {}
for table in wordDoc.tables:
    for row in table.rows:
        keyList.extend(row.cells[0].text.splitlines())
        valueList.extend(row.cells[1].text.splitlines())
        # for cell in row.cells:
        #     print(cell.text)

print("keys: ", len(keyList))
print("values: ", len(valueList))
n = 0

for k in keyList:
    # print(k, "-", valueList[n])
    tupleList[k]=valueList[n]
    n = n + 1
n = 1
file = codecs.open("general_gold.txt", "a", "utf-8")
for k, v in tupleList.items():
    print(n, k, v)
    n = n + 1
    file.write(k+", "+v+"\n")
file.close()