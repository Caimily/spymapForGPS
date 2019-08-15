# encoding:utf-8
# from Ruby in 20190814 16:00

import requests
import sys
import json
import csv
import codecs

ty = sys.getfilesystemencoding()
token = "PWxyhjAkq0Zb880XA74FDcVeiHl84i5g"
# list = [下辖荆州区、沙市区、江陵县、松滋市、公安县、石首市、监利县、洪湖市8个县市区和荆州开发区、华中农高区、纪南文旅区3个功能区]
# list = ['学校','小学','中学']
# list = ['武汉'江岸区、江汉区、硚口区、汉阳区、武昌区、洪山区、青山区 蔡甸区、汉南区、江夏区、黄陂区、新洲区，东西湖区。]
keywords = '中学'
keyplace = '华中农高区'
ands = '&region='
pages= '&page_size=50&output=json&ak='

url = 'http://api.map.baidu.com/place/v2/search?query='
# 爬取部分
def Spy(url,token):
    r = requests.get(url + keywords + ands + keyplace + pages+ token)
    print(url + keywords + ands + pages+ token)
    response_dict = r.json()
    with open('searchschool.json', 'w') as f:
        json.dump(response_dict, f)
    results = response_dict["results"]
    return results

#打印结果
def printResult(results):
    out = open('searchResult.csv', 'a', newline='')
    csv_write = csv.writer(out, dialect='excel')
    # title = sh.row_values(0)
    for school in results:
        loc = school['location']
        lat = str(loc['lat'])
        lng = str(loc['lng'])
        print(school['name'] + ":" + school['address'] + ":(" + lat + "," + lng + ")")
        csv_str = ('湖北省','荆州市',keywords,keyplace,school['name'],school['address'],lat,lng)
        csv_write.writerow(csv_str)
    print("完成")

if __name__ == '__main__':
    printResult(Spy(url,token))


# 将json文件转为csv文件searchschool.json
# fr = open("result/searchschool.json", "r")  # 打开json文件
# ls = json.load(fr)  # 将json格式的字符串转换成python的数据类型，解码过程
# print(ls)
# data = [list(ls[2].keys())]  # 获取第二列信息,即key
# data = [list(data[0].keys())]  # 获取第二列信息,即key
# for item in ls:
#     data.append(list(item.values()))  # 获取每一行的值value
# fr.close()  # 关闭json文件

# fw = open("result/searchResult.csv", "w")  # 打开csv为文件
# for line in data:
#     fw.write(",".join(line) + "\n")  # 以逗号分隔一行的每个元素，最后换行
# fw.close()  # 关闭csv文件
