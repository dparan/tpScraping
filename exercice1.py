import statistics
import operations
import csv


array = [['lib / Dossier','moyenne ligne','total lignes','ecart type lignes','moyenne caractère','total caractère','ecart type caractère']]
array.append(operations.calculatesValues('Corpus_detourage/clean/', 'clean'))
array.append(operations.calculatesValues('Corpus_detourage/html/', 'BS'))
array.append(statistics.calculatesValues())


with open('generatedDatas/ex1/datas.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(array)