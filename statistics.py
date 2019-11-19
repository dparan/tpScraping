import os
from math import *
import jusText

def file_char(filename):
    with open(filename, encoding="UTF-8") as f:
        characters = 0
        for line in f:
            # unicode_data = line.decode('utf8')
            characters += len(line)
    return characters


def file_len(fileName):
    with open(fileName, encoding="UTF-8") as f:
        for i, l in enumerate(f):
            pass
    return i + 1


resultsArray = []
cleanArray = []

def calculatesValues():
    jusText.createFiles()
    #TREATMENT
    fileListJT = os.listdir("Corpus_detourage/JT")
    lineNumberJT = 0
    charNumberJT = 0
    fileNumberJT = len(fileListJT)

    # Calcul des statistiques pour les fichiers jusText
    for f in fileListJT:
        filename: str = 'Corpus_detourage/JT/' + f
        lineNumberJT += file_len(filename)
        charNumberJT += file_char(filename)
        resultsArray.append([f, file_len(filename), file_char(filename)])

    moyLineJT = lineNumberJT / fileNumberJT

    moyCharJT = charNumberJT / fileNumberJT

    # calculates the standard deviation of lines
    sum = 0
    for res in resultsArray:
        sum += (res[1] - moyLineJT)**2
    sum /= len(resultsArray)
    standardDeviationLines = sqrt(sum)

    # calculates the standard deviation of characters
    sum = 0
    for res in resultsArray:
        sum += (res[2] - moyCharJT)**2
    sum /= len(resultsArray)
    standardDeviationChars = sqrt(sum)
    return ['JT', moyLineJT, lineNumberJT, standardDeviationLines, moyCharJT, charNumberJT, standardDeviationChars]
