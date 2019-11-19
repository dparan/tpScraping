import os
import justext
import json

jsonFile = open("Corpus_detourage/doc_lg.json", "r")
json = json.load(jsonFile)

fileList = os.listdir("Corpus_detourage/html")
for f in fileList:
    filename: str = 'Corpus_detourage/html/' + f
    response = open(filename, "r", encoding="UTF-8", errors="ignore").read()

    language = "English"
    if json[f] != "Chinese":
        language = json[f]

    paragraphs = justext.justext(response, justext.get_stoplist(language))
    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            newFileName = "Corpus_detourage/JT_trueLg/" + f + ".txt"
            newFile = open(newFileName, "a", encoding="UTF-8")
            newFile.write("<p>" + paragraph.text + "</p>\n")
            newFile.close()
