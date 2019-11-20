from bs4 import BeautifulSoup
from math import *
import os

def readDirJT(path):
    print('lol')


def readDirClean(path):
    # Gets files from clean folder
    fileList = os.listdir(path)
    # creates results vars
    resultsArray = []
    noiseArray = []
    silenceArray = []
    totalLines = 0
    totalCars = 0
    # First for loop which will gets basic vars
    for f in fileList:
        filename: str = 'Corpus_detourage/clean/' + f
        # opens file
        currentFile = open(filename, 'r', encoding='utf8').read()
        soup = BeautifulSoup(currentFile, "html.parser")
        # Gets number of line
        lines = soup.find_all()
        lineNumber = len(lines) - 1
        # Counts number of char
        carNumber = 0
        for line in lines:
            carNumber += len(line)
        # sets results values
        resultsArray.append([filename, lineNumber, carNumber])
        totalLines += lineNumber
        totalCars += carNumber
    return [resultsArray, totalLines, totalCars, len(fileList)]

def readDirBS(path):
    # Gets files from clean folder
    fileList = os.listdir(path)
    # creates results vars
    resultsArray = []
    totalLines = 0
    totalCars = 0
    # First for loop which will gets basic vars
    for f in fileList:
        filename: str = path + f
        # opens file
        currentFile = open(filename, 'r', encoding='UTF-8', errors="ignore").read()
        soup = BeautifulSoup(currentFile, "html.parser")
        # Gets number of line
        lines = soup.find_all('p')
        lineNumber = len(lines) - 1
        # Counts number of char
        carNumber = 0
        newFileName = "Corpus_detourage/BS/" + f + ".txt"
        newFile = open(newFileName, "w", encoding="UTF-8")
        for line in lines:
            currentLine = '<p>'+str(line.getText())+'</p>'
            print(currentLine)
            carNumber += len(currentLine)
            newFile.write(currentLine)
        newFile.close()
        # sets results values
        resultsArray.append([filename, lineNumber, carNumber])
        totalLines += lineNumber
        totalCars += carNumber
    return [resultsArray, totalLines, totalCars, len(fileList)]

def calculatesValues(path, typeLib):
    array = []
    if(typeLib == 'BS') :
        array = readDirBS(path)
    if (typeLib == 'clean'):
        array = readDirClean(path)
    if (typeLib == 'JT'):
        array = readDirJT(path)
    resultsArray = array[0]
    totalLines = array[1]
    totalCars = array[2]
    fileListLen = array[3]
    # for lines
    moyLines = totalLines/ fileListLen
    # calculates the standart deviation of lines
    sum = 0
    for res in resultsArray:
        sum += (res[1] - moyLines)**2
    sum /= len(resultsArray)
    standartDeviationLines = sqrt(sum)

    # for cars
    moyCars = totalCars / fileListLen
    # calculates the standart deviation of lines
    sum = 0
    for res in resultsArray:
        sum += (res[2] - moyCars)**2
    sum /= len(resultsArray)
    standartDeviationCars = sqrt(sum)
    return [typeLib, moyLines, totalLines, standartDeviationLines, moyCars, totalCars, standartDeviationCars]

def getFetchingList(path,part):
    bruit = []
    silence = []
    cleanPath="Corpus_detourage/clean/"
    fileListClean = os.listdir(cleanPath)
    fileList = os.listdir(path+part)
    for file in fileList:
        if(file.replace('.txt','') in fileListClean):
            with open(path+part+file, 'r', encoding='ISO-8859-1') as fileE:
                with open(cleanPath+file.replace('.txt',''),'r', encoding="UTF-8") as cleanFile:
                    if (len(list(fileE))>len(list(cleanFile))):
                        bruit.append(file.replace('.txt',''))
                    elif (len(list(fileE))<len(list(cleanFile))):
                        print("silence")
                        silence.append(cleanFile)
    return [bruit,silence]

def getFetchingLists():
    BS = getFetchingList("Corpus_detourage","/BS/")
    JT = getFetchingList("Corpus_detourage","/JT/")
    return [BS,JT]
    
getFetchingLists()