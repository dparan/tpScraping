import os
from unittest import result
import re
import Exercice3.cleaneval_tool as clt
import json

jsonFile = open("../doc_lg.json", "r")
json = json.load(jsonFile)


def compute_intrinsic(folder_path):
    rs = []
    file_list = os.listdir(folder_path)
    for f in file_list:
        file_name = folder_path + "/" + f
        golden_file_name = "../Corpus_detourage/clean/" + f.strip(".txt")
        result = clt.evaluate_file(file_name, golden_file_name)

        element = {
            "filename": f,
            "f-score": result["f-score"],
            "precision": result["precision"],
            "recall": result["recall"],
            "lang": json[f.strip(".txt")]
        }
        rs.append(element)
    return rs


def concat_by_lang(result_array):
    rs = {"English": {}, "Russian": {}, "Greek": {}, "Polish": {}}

    en_number = 0
    el_number = 0
    pl_number = 0
    ru_number = 0
    zh_number = 0

    file_number = 0

    for e in result_array:
        if e["lang"] == "English":
            en_number += 1
            file_number = en_number
        if e["lang"] == "Greek":
            el_number += 1
            file_number = el_number
        if e["lang"] == "Polish":
            pl_number += 1
            file_number = pl_number
        if e["lang"] == "Russian":
            ru_number += 1
            file_number = ru_number
        if e["lang"] == "Chinese":
            zh_number += 1
            file_number = zh_number

        old = rs[e["lang"]]

        # if rs doesn't have right keys
        if old.get("f-score") is None or old.get("precision") is None or old.get("recall") is None:
            element = {
                e["lang"]: {
                    "f-score": e["f-score"],
                    "precision": e["precision"],
                    "recall": e["recall"],
                    "numberOfFiles": file_number
                }
            }

        # if rs already have the right keys
        if old.get("f-score") is not None and old.get("precision") is not None and old.get("recall") is not None:
            element = {
                e["lang"]: {
                    "f-score": old.get("f-score") + e["f-score"],
                    "precision": old.get("precision") + e["precision"],
                    "recall": old.get("recall") + e["recall"],
                    "numberOfFiles": file_number
                }
            }

        rs.update(element)

    # compute average value
    for k, v in rs.items():
        element = {
            k: {
                "f-score": v["f-score"] / v["numberOfFiles"],
                "precision": v["precision"] / v["numberOfFiles"],
                "recall": v["recall"] / v["numberOfFiles"]
            }
        }
        rs.update(element)

    return rs


def concat_by_sources(result_array):
    map_sources = {}
    for elem in result_array:
        # find the source
        source = re.findall(r'_(.+?)_', elem["filename"])[0]
        if source in map_sources:
            map_sources[source]["f-score"].append(elem["f-score"])
            map_sources[source]["precision"].append(elem["precision"])
            map_sources[source]["recall"].append(elem["recall"])
        else:
            map_sources[source] = {'f-score': [elem['f-score']], 'precision': [elem['precision']],
                                   'recall': [elem['recall']]}

    # compute average values
    map_sources_mean = map_sources
    for source in map_sources:
        mean_fscore = sum(map_sources[source]["f-score"]) / len(map_sources[source]["f-score"])
        mean_precision = sum(map_sources[source]["precision"]) / len(map_sources[source]["precision"])
        mean_recall = sum(map_sources[source]["recall"]) / len(map_sources[source]["recall"])
        map_sources_mean[source]["f-score"] = mean_fscore
        map_sources_mean[source]["precision"] = mean_precision
        map_sources_mean[source]["recall"] = mean_recall

    return map_sources_mean


def main():
    result_array = compute_intrinsic("../Corpus_detourage/JT")
    print("By file : " + str(result_array))
    print("By lang : " + str(concat_by_lang(result_array)))
    print("By source : " + str(concat_by_sources(result_array)))


if __name__ == "__main__":
    main()
