import os
import requests
import justext


def createFiles():
    fileList = os.listdir("Corpus_detourage/html")
    for f in fileList:
        filename: str = 'Corpus_detourage/html/' + f
        response = open(filename, "r", encoding="UTF-8", errors="ignore").read()
        paragraphs = justext.justext(response, justext.get_stoplist("English"))
        for paragraph in paragraphs:
            if not paragraph.is_boilerplate:
                newFileName = "Corpus_detourage/JT/" + f + ".txt"
                newFile = open(newFileName, "a", encoding="UTF-8")
                newFile.write("<p>" + paragraph.text + "</p>\n")
                newFile.close()
