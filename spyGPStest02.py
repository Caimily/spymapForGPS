# -*- coding: utf-8 -*-
import urllib.request
import json
import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
print('中文')

#生成Josn数据
def create_json(url):
    url_file = urllib.request.urlopen(url)
    json_file = url_file.read()
    json_dict = json.loads(json_file)
    return json_dict

#解析Josn数据，并返回为List
def read_json(json_dict,pois_list):
    #依次读取Json数据，保存到List中
    for text in json_dict["results"]:
        poi_list = []
        #只获取目标地点的名称和坐标，用于后续计算
        poi_list.append(text["name"])
        poi_list.append(text["location"])
        pois_list.append(poi_list)
    return pois_list

#程序主函数
if __name__ == "__main__":
    # 设置URL参数
    ak = "PWxyhjAkq0Zb880XA74FDcVeiHl84i5g" #访问AK，注意可能会被限制
    #加Fir前缀的均为首要查询目标数据
    Fir_KeyWord = "中学"
    Fir_region = "武昌区"
    # 加Sec前缀的均为次要查询目标数据
    Sec_KeyWord = "中小学"
    page_size = 20
    Fir_page_num = 0
    Fir_url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + \
          str(Fir_KeyWord) + "&region=" + str(Fir_region) + "&page_size=" + str(page_size) + "&page_num=" + str(Fir_page_num)
    # 查取URL的信息，并将数据保存在List中
    Fir_pois_list = []
    Fir_json_dict = create_json(Fir_url)
    Fir_pois_list = read_json(Fir_json_dict, Fir_pois_list)
    Fir_total = int(Fir_json_dict["total"])  # 记录数据总数
    print(str(Fir_region) + "共有" + str(Fir_total) + "个" + str(Fir_KeyWord) + "!")
    # 将数据写入TXT文件
    f = open('result.txt', 'w')
    f.write(str(Fir_region) + "共有" + str(Fir_total) + "个" + str(Fir_KeyWord) + "! 周边" + str(Sec_KeyWord) + "具体信息如下：\n")

    #记录数据页数
    Fir_Page = Fir_total / page_size + 1
    while (Fir_page_num < Fir_Page):
        Fir_num = Fir_page_num * page_size  # 定义学校个数
        for Fir_poi_list in Fir_pois_list:
            Fir_num += 1
            f.write(str(Fir_num) + "," + Fir_poi_list[0].encode("utf-8") + "\n")
            # 获取每个学校的经纬度坐标
            Sec_location_lat = Fir_poi_list[1]["lat"]
            Sec_location_lng = Fir_poi_list[1]["lng"]
            # 设置半径为500
            radius = 500
            Sec_page_num = 0
            Sec_url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + \
                      str(Sec_KeyWord) + "&location=" + str(Sec_location_lat) + "," + str(Sec_location_lng) + "&page_size=" + \
                      str(page_size) + "&page_num=" + str(Sec_page_num) + "&radius=" + str(radius)
            Sec_pois_list = []
            Sec_json_dict = create_json(Sec_url)
            Sec_pois_list = read_json(Sec_json_dict, Sec_pois_list)
            Sec_total = int(Sec_json_dict["total"])  #记录这一学校周边网吧总数
            Sec_Page = Sec_total / page_size + 1 #记录数据页数
            while (Sec_page_num < Sec_Page):
                Sec_num = Sec_page_num * page_size  # 定义网吧个数
                for Sec_poi_list in Sec_pois_list:
                    Sec_num += 1
                    f.write(str(Fir_num) + "-" + str(Sec_num) + "," + Sec_poi_list[0].encode("utf-8") + "\n")
                Sec_page_num += 1
                #再次定义URL，读取后面页面的数据
                Sec_url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + \
                          str(Sec_KeyWord) + "&location=" + str(Sec_location_lat) + "," + str(Sec_location_lng) + "&page_size=" + \
                          str(page_size) + "&page_num=" + str(Sec_page_num) + "&radius=" + str(radius)
                Sec_pois_list = []
                Sec_json_dict = create_json(Sec_url)
                Sec_pois_list = read_json(Sec_json_dict, Sec_pois_list)
        Fir_page_num += 1
        #再次定义URL，读取后面页面的数据
        Fir_url = "http://api.map.baidu.com/place/v2/search?ak=" + str(ak) + "&output=json&query=" + \
                  str(Fir_KeyWord) + "&region=" + str(Fir_region) + "&page_size=" + str(page_size) + "&page_num=" + str(Fir_page_num)
        # 查取URL的信息，并将数据保存在List中
        Fir_pois_list = []
        Fir_json_dict = create_json(Fir_url)
        Fir_pois_list = read_json(Fir_json_dict, Fir_pois_list)

    f.close()
    print("Success!")