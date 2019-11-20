import os
import justext
import langid


def convertISO(ISOcode):
    switcher = {
        "fr": 'French',
        "en": 'English',
        "el": 'Greek',
        "pl": 'Polish',
        "ru": 'Russian',
        "zh": 'English'
    }
    return switcher.get(ISOcode, "Invalid ISO code")


fileList = os.listdir("../Corpus_detourage/html")
for f in fileList:
    filename: str = '../Corpus_detourage/html/' + f
    response = open(filename, "r", encoding="UTF-8", errors="ignore").read()
    lang = langid.classify(response)
    paragraphs = justext.justext(response, justext.get_stoplist(convertISO(lang[0])))
    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            newFileName = "../Corpus_detourage/JT_langid/" + f + ".txt"
            newFile = open(newFileName, "a", encoding="UTF-8")
            newFile.write("<p>" + paragraph.text + "</p>\n")
            newFile.close()
