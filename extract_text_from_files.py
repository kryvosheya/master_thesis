#!/usr/bin/python

import xml.etree.ElementTree as ET
import codecs
import os, sys, getopt


def run(source, target):
    start_extractor(source, target)


def start_extractor(path, target):
    if os.path.isfile(path):
        extract_text_from_file(path, target)
    elif os.path.isdir(path):
        entries = os.scandir(path)
        for entry in entries:
            start_extractor(entry, target)
    else:
        raise Exception('This is neither file nor directory')

#!/bin/bash
def extract_text_from_file(fsource, ftarget):
    tree = ET.parse(fsource)
    root = tree.getroot()

    file = codecs.open(ftarget, "a", "utf-8")
    textlist = []
    for element in root.iter():
        if element.text is not None and not element.text.isspace():
            textlist.append(element.text)
    file.write("\n".join(textlist))
    file.close()
    print('Text extracted from: ', fsource)


if __name__ == '__main__':
    # Map command line arguments to function arguments.
    try:
        run(*sys.argv[1:])
    except TypeError:
        print(
            'You should define input and target parameters. The comand should look like: textExtractor.py <inputfile/dir> <outputfile>')
