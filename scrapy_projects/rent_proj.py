from bs4 import BeautifulSoup   #用来解析html或者xml文件的库，支持元素选择器
import requests
import csv
import time

useragent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
url="https://wh.58.com/pinpaigongyu/pn/{page}/?minprice=2000_3000"

#已完成的页数序号，初时为0
page=0

#打开rent.csv文件
csv_file=open("rent.csv","w")
#创建writer对象，指定文件与列分隔符（，）
csv_writer=csv.writer(csv_file,delimiter=',')

while True:
    page +=1
    print("fetch: ", url.format(page=page))
    time.sleep(3)
    #抓取目标页面
    response=requests.get(url.format(page=page),headers={'User-agent':useragent})
    #获取页面正文,创建一个BeautifulSoup对象
    html=BeautifulSoup(response.text,"lxml")  #要指定解释器，否则会报错

    #获取class=list的元素下的所有li元素
    house_list=html.select(".list > li")

    #循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        #得到标签包裹着的文本
        house_title =house.select("h2")[0].string
        #得到标签内属性的值。得到的路径是相对路径，需要对路径进行拼接得到完整的url地址
        house_url="http://wh.58.com/%s"%(house.select("a")[0]["href"])
        house_info_list=house_title.split()

        #如果第二列是公寓名则取第一列作为地址
        if "公寓" in house_info_list[1] or "青年社区" in house_info_list[1]:
            house_location=house_info_list[0]
        else:
            house_location=house_info_list[1]

        house_money=house.select(".money")[0].select("b")[0].string
        csv_writer.writerow([house_title,house_location,house_money,house_url])

csv_file.close()