# encoding:utf-8
# from Ruby in 20190814 16:00
# -*-coding:UTF-8-*-

import csv
import sys
import requests  # 导入requests库，这是一个第三方库，把网页上的内容爬下来用的

ty = sys.getfilesystemencoding()

# print(ty)#这个可以获取文件系统的编码形式

import time


lat_1 = 29.450404
lon_1 = 110.428233  #东经 114.251159,30.72299  114.950564,30.986777
lat_2 = 30.986777  #北纬 114.428233,30.450404
lon_2 = 112.251159  # 坐标范围
las = 1  # 给las一个值1

ak = 'PWxyhjAkq0Zb880XA74FDcVeiHl84i5g'

# push=r'D:\python'
out = open('j_str.csv', 'a', newline='')
csv_write = csv.writer(out, dialect='excel')
print(time.time())
print('开始')

urls = []  # 声明一个数组列表
lat_count = int((lat_2 - lat_1) / las + 0.1)
lon_count = int((lon_2 - lon_1) / las + 0.1)

for lat_c in range(0, lat_count):
    lat_b1 = lat_1 + las * lat_c
    for lon_c in range(0, lon_count):
        lon_b1 = lon_1 + las * lon_c
        for i in range(0, 20):
            page_num = str(i)
            url = 'http://api.map.baidu.com/place/v2/search?query=学校&region=武汉市&'\
                  ' bounds=' + str(lat_b1) + ',' + str(lon_b1) + ',' + str(lat_b1 + las) + ',' + str(
    lon_b1 + las) + '&page_size=5&page_num=' + str(page_num) + '&output=json&ak=' + ak
            urls.append(url)

# urls.append(url)的意思是，将url添加入urls这个列表中。
# f=open(r'D:\python\guiyangxuexiao.csv','a',encoding='utf-8')
print('url列表读取完成')
for url in urls:
    time.sleep(10)# 为了防止并发量报警，设置了一个10秒的休眠。
    print(url)
    html = requests.get(url)  # 获取网页信息
    data = html.json()# 获取网页信息的json格式数据
    print(data)
    for item in data['results']:
        jname1 = item['province']
        jname2 = item['city']
        jname3 = item['area']
        jname4 = item['name']
        jname = jname1 + jname2 + jname3 + jname4
        j_uid = item['uid']
        jstreet_id = item.get('street_id')
        jlat = item['location']['lat']
        jlon = item['location']['lng']
        jaddress = item['address']
        jphone = item.get('telephone')
        j_str = (jname, j_uid, jstreet_id, str(jlat), str(jlon), jaddress, jphone)
        print(j_str)
        csv_write.writerow(j_str)
        print("write over")
#  f.write(j_str)
    print(time.time())
# f.close()

print('完成')
