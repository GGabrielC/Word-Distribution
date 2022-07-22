# EXAMPLE:
# python WordDistribution.py 2 inputTextFileOrDirectory

from collections import Counter
import fnmatch
import sys
import os

minimumRelevantWordFrequency = int(sys.argv[1])
pathInput = sys.argv[2]
wordSeparator = sys.argv[3] if len(sys.argv) > 3 else " "

def removeIrrelevantWords(counter, minimumRelevantWordFrequency):
    return Counter({k: c for k, c in counter.items() if c >= minimumRelevantWordFrequency})

def handleFile(pathFileInput, counter, BUFFER_SIZE = 1000):
    with open(pathFileInput) as f:
        data = f.read(BUFFER_SIZE)
        counter.update(data.split(wordSeparator))

def handleDirectory(pathDirectoryInput, counter):
    for root, _, files in os.walk(pathDirectoryInput):
        for file in fnmatch.filter(files, "*"):
            pathFileInput = os.path.join (root, file)
            handleFile(pathFileInput, counter)

def run():
    counter = Counter()
    if os.path.isdir(pathInput):
        handleDirectory(pathInput, counter)
    else:
        handleFile(pathInput, counter)
    counter = removeIrrelevantWords(counter, minimumRelevantWordFrequency)
    
    [print(c) for c in counter.most_common()]
    
run()