#!/bin/bash
import xml.etree.ElementTree as ET
import codecs
import os
output = codecs.open("annot.txt", "w", "utf-8")
textlist = []
for file in os.listdir("/home/anastasiya/PycharmProjects/master/texts/"):
    tree = ET.parse(file)
    root = tree.getroot()
    for element in root.iter():
        if element.text is not None and not element.text.isspace():
           textlist.append(element.text)
output.write("\n".join(textlist))
output.close()




