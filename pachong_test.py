# #爬虫 :
#         从互联网获取数据
#         urlopen(url,data,timeout="超时时间",cafile=none,cpath=)

from urllib import request
from urllib import *
from urllib import parse
from urllib.parse import urlparse



url = 'https://www.baidu.com'


# url = 'https://564654q.aa.io'


def download(url, user_restart=2, user_agent='bingbot'):
    headers = {'User_Agent': user_agent}
    try:
        resp = request(url, headers=headers)

        html = request.urlopen(resp)

    except request.URLError as e:
        print(e)
        hasattr(e, "code")
        print(hasattr(e, "code"))

# print(type(resp))
# print(dir(resp))


# # print(resp.read())
# # print(resp.getcode())
# # urlretrieve 下载代码到本地
# request.urlretrieve(url, "123.html")


# urlencode()  url 中有中文时使用
#  url = "https://cn.bing.com/search?q=按"  直接read()报错
# url = "https://cn.bing.com/search"
# parms = {"q": "按"}
#
# result = parse.urlencode(parms)
# print(result)
# 结果:   q=%E6%8C%89

# url = url + "?" + result
# print(url)
# resp = request.urlopen(url)
# print(resp.read())

# parse_qs

# parms = {"q": "按"}
# result = parse.urlencode(parms)
# print(result)
# # 结果:   q=%E6%8C%89
#
#
# re = parse.parse_qs(result)
# print(re)
# # 结果:  {'q': ['按']}
