import requests

# url = "https://fanyi.baidu.com/v2transapi"
# 发送请求get  post  get(在url中显示不安全)   post(安全   适合用户登录 大文件传送)
# response = requests.get(url)


# 发送heard请求
# header = {
#     "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36"
#
# }

# 浏览器传入请求
# data = {"query": "123", "from": "zh", "to": "en"}
# response = requests.post(url, data=data, headers=header)
#
# print(response.content.decode())

####    请求
# print(response.request.url)   #发送请求的url地址
# print(response.url)             # response响应的url地址
# print(response.request.headers)     #请求头
# print(response.headers)         #响应请求

###     使用超时参数  timeout s设置超时  超时会报错

# requests.get(url, headers=header, timeout=3)

# 获取网页的html
# response.encoding = "utf-8"
# print(response.text)


# 把相应的二进制文件转化成str字符类型
# print(response.text)

# 获取网页源码的正确打开方式
# response.content.decode("gbk")
# response.text

# print("------------retrving--------------")
# from retrying import retry
#
# @retry(stop_maxe_attemt_number=3)
# def run1():
#     print("this is func1")
#     raise ValueError("000")


### json
# json.loads  把json 字符串转换成python类型    json.loads(json字符)
# json.dumps  把python 类型转为 json          json.dumps({"a":"a"})
# json.dumps(json_str, ensure_ascii=False, indent=2)   ensure_ascii  不以ascii形式显示中文显示
#                                                indent   能够让下一行在上一行的基础上空格


# import json
#
#
#
# url = "https://m.douban.com/rexxar/api/v2/muzzy/columns/10018/items?start=0&count=3"
# header = {"User-Agent":
#               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36"
#
#           }
# response = requests.get(url, headers=header)
# str = response.content.decode()
# print(type(response.content.decode()))
# f = open("./log.txt", "w")
#
# json_str = json.loads(str)
#
# #
# f.write(json.dumps(json_str, ensure_ascii=False, indent=2))
# print(json.loads(str))
# print(response.content.decode())


###  xpath和lxml
# xpath
# 一门html中提取数据的语言
# xpath语法
# 1.选择节点(标签) /
#     /html/head/meta   :表示html下head下的所有meta标签
# 2.    //  从任意节点开始选择
#         //li    :表示当前页面的所有li标签
#           /html/head//li   :head下的所有li标签
#  3. []  对属性进行限定  @ 选择任意一个元素   @在[]中修饰一个值    单独出现获取属性的值
#           //div[@class="asd"]/li    选择div 中class = asd的div 底下的li
#       a/@href  获取a标签的href值
#  4. 获取文本
#       /a/text() 获取a标签下的文本
#     / a // text()  获取a标签下的所有文本
#
####  lxml
#  安装 pip  install  lxml
# 使用 python 中
# from lxml import etree
# element = erteee.HTML("html字符串")
# element.xpath()


