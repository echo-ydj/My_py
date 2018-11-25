'''
专门请求url地址的方法
'''

import requests
from retrying import retry
header = {
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3573.0 Safari/537.36"

}

#让装饰函数反复执行三次,三次全部报错才会报错,中间有一次正常
@retry(stop_max_attempt_number=3)
def _pares_url(url):
    response = requests.get(url,headers=header,timeout=5)
    return response.content.decode()

def pares_url(url):
    try:
        html_str = _pares_url(url)
    except:
        html_str = None
    return html_str
if __name__ == '__main__':
    url ="http://www.baidu.com"
    print(pares_url(url)[:20])