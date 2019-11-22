import os
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


# compute the average value of f-score, precision and recall from a dict
# input example :   {{key: {'f-score': [_, _], 'precision': [_, _], 'recall': [_, _]}, another_key: {...}}
# output example :  {{key: {'f-score': _, 'precision': _, 'recall':_}, another_key{...}}
def stats_from_dict(raw_dict):
    # compute average values
    map_mean = raw_dict
    for element in raw_dict:
        mean_f_score = sum(raw_dict[element]["f-score"]) / len(raw_dict[element]["f-score"])
        mean_precision = sum(raw_dict[element]["precision"]) / len(raw_dict[element]["precision"])
        mean_recall = sum(raw_dict[element]["recall"]) / len(raw_dict[element]["recall"])

        map_mean[element]["f-score"] = mean_f_score
        map_mean[element]["precision"] = mean_precision
        map_mean[element]["recall"] = mean_recall

    return map_mean


# regroup score into a dict mapped by the given key
# input example :   key = 'English'
#                   element = {'filename': _, 'f-score': 10, 'precision': 15, 'recall': 55, 'lang': 'English'}
#                   raw_dict = {'English': {'f-score': [5], 'precision': [7], 'recall': [2]}}
# output example :  result = {'English': {'f-score': [5, 10], 'precision': [7, 15], 'recall': [2, 55]}}
def concat_dict_by_key(key, element, raw_dict):
    if key in raw_dict:
        raw_dict[key]["f-score"].append(element["f-score"])
        raw_dict[key]["precision"].append(element["precision"])
        raw_dict[key]["recall"].append(element["recall"])
    else:
        raw_dict[key] = {'f-score': [element['f-score']], 'precision': [element['precision']],
                         'recall': [element['recall']]}

    return raw_dict


# compute average score from an array of dict containing files score and regroup by language
def compute_by_lang(result_array):
    map_lang = {}
    for elem in result_array:
        language = elem["lang"]
        map_lang = concat_dict_by_key(language, elem, map_lang)

    return stats_from_dict(map_lang)


# compute average score from an array of dict containing files score and regroup by source
def compute_by_sources(result_array):
    map_sources = {}
    for elem in result_array:
        # find the source
        source = re.findall(r'_(.+?)_', elem["filename"])[0]
        map_sources = concat_dict_by_key(source, elem, map_sources)

    return stats_from_dict(map_sources)


def main():
    print("================ JT ================")
    result_array = compute_intrinsic("../Corpus_detourage/JT")
    print("By file : " + str(result_array))
    print("By lang : " + str(compute_by_lang(result_array)))
    print("By source : " + str(compute_by_sources(result_array)))

    print("================ JT with langid ================")
    result_array = compute_intrinsic("../Corpus_detourage/JT_langid")
    print("By file : " + str(result_array))
    print("By lang : " + str(compute_by_lang(result_array)))
    print("By source : " + str(compute_by_sources(result_array)))

    print("================ JT with true lg ================")
    result_array = compute_intrinsic("../Corpus_detourage/JT_trueLg")
    print("By file : " + str(result_array))
    print("By lang : " + str(compute_by_lang(result_array)))
    print("By source : " + str(compute_by_sources(result_array)))

    print("================ BS ================")
    result_array = compute_intrinsic("../Corpus_detourage/BS")
    print("By file : " + str(result_array))
    print("By lang : " + str(compute_by_lang(result_array)))
    print("By source : " + str(compute_by_sources(result_array)))

    print("================ UF ================")
    result_array = compute_intrinsic("../Corpus_detourage/uf")
    print("By file : " + str(result_array))
    print("By lang : " + str(compute_by_lang(result_array)))
    print("By source : " + str(compute_by_sources(result_array)))


if __name__ == "__main__":
    main()
