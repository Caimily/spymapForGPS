# encoding:utf-8
# from Ruby in 20190815 14:43

import csv
import json

def json_to_csv(path):
    with open(path + '.json', "r") as f:
        data = f.read()
    jsonData = json.loads(data)

    csvfile = open(path + ".csv", "w", newline='')
    keys_write = True
    writer = csv.writer(csvfile)
    print(jsonData)
    for dic in jsonData:
        if keys_write:
            keys = list(dic.keys())
            print(keys)
            writer.writerow(keys)
            keys_write = False
        writer.writerow(list(dic.values()))
        print(list(dic.values()))
    csvfile.close()

if __name__ == '__main__':
    path = "searchschool"  # 文件的路径
    json_to_csv(path)