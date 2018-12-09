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


####  lxml
#  安装 pip  install  lxml
# 使用 python 中
# from lxml import etree
# element = erteee.HTML("html字符串")
# element.xpath(" //div[@class="asd"]/li")

# r 的使用原始含义

# import re
# s="\\nas"
# print(s)
# print(re.match(r"\\n",s))


#    |  匹配任意表达式
#     (ab) 将括号中的字符作为一个分组
#     \num 引用分组num匹配的字符串
#     (?P<name>) 分组起别名
#     (?P=name)  引用别名


import re

# s = "<html><h1>HELLO WORD</h1></html>"
# p = r"<(.+)><(.+)>(.+)</\2></\1>$"
# p1 = r"<(?P<key1>.+)><(?P<key2>.+)>.+</(?P=key2)></(?P=key1)>"   #注意 </ (?P=key)>  /在()外
# r1 = re.match(p1, s)
# print(r1)
#
# str = "<h1>NNNNN</h1>"
# result = re.match(r"<(?P<key1>.+)>(.+)</(?P=key1)>$", str)
# print(result)
# print(result.group(1))

# s = "<html><h1>HELLO WORD</h1></html>"
# r=re.search(r"\s",s)
# print(dir(r))


# re.sub("替换字符(正则)","被替换为(可以为函数)","字符串")

# def replace(result):
#     num = int(result.group())
#     return str(num + 50)
#
#
# print(re.sub(r"\d+", replace, "python=100,php=0"))


# str = """<div>
# <p>12</p>
# <p>qw</p>
# <p>vv</p></div>"""
#
#
# def replace(result):
#     return result.group(2)
#
#
# # print(re.sub(r"<(?P<key1>.+)>(.+)</(?P=key1)>", replace, str))
#
# print(re.sub("</?\w+>", "", str))


# s = "this is num 12-10-23"
# 贪婪模式  最多匹配
# r =re.match(r"(.+)(\d+-\d+-\d+)", s)
# print(r.group(2))       #  2-10-23

# 非贪婪模式  后加?  匹配最少
# r = re.match(r"(.+?)(\d+-\d+-\d+)", s)
# print(r.group(2))  # 12-10-23
