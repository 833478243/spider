from concurrent.futures import ThreadPoolExecutor
from time import sleep
import requests,re
import json,time,random
from openpyxl import Workbook

# url="https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv151&productId=53198361568&score=0&sortType=5&page=2&pageSize=10&isShadowSku=0&rid=0&fold=1"
# header={
#     "referer":"https://item.jd.com",
#     "user-agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36",
# }
#
# req=requests.get(url,headers=header).text
# # print(req)
# pattern = re.compile(r'"guid":".*?","content":"(.*?)"')
# b = pattern.findall(req)
# print(b)
def jd(l):

    d = {}

    # proxy = {
    #     'http': 'http://122.194.249.38:18810',
    #     'https': 'http://122.194.249.38:18810',
    # }

    proxy = [
        # { 'http': 'http://119.114.147.248:10830',
        # 'https': 'http://119.114.147.248:10830',},
        # {    'http': 'http://115.226.232.192:24006',
        # 'https': 'http://115.226.232.192:24006',},
        # {    'http': 'http://202.109.169.4:19259',
        # 'https': 'http://202.109.169.4:19259',},
        {    'http': 'http://114.99.9.173:19275',
        'https': 'http://114.99.9.173:19275',},
        {    'http': 'http://60.169.151.172:18642',
        'https': 'http://60.169.151.172:18642',}
    ]
    user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',]

    url="https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv151&productId={}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&rid=0&fold=1".format(l)

    header={
        "referer":"https://item.jd.com",
        "user-agent":random.choice(user_agents),
    }

    req1=requests.get(url,headers=header,proxies=random.choice(proxy))

    print(req1.status_code)

    req = req1.text

    # print(req)
    pattern = re.compile(r'"guid":".*?","content":"(.*?)"')
    b = pattern.findall(req)
    time.sleep(2)
    d[l] = list(set(b))
    return d





def main():
    l = []
    f = open("999999.txt", "r")  # 设置文件对象
    for z in f.readlines():
        l.append(z.replace('\n', ''))

    executor = ThreadPoolExecutor(50)
    # future = executor.submit(task, 100)
    future = executor.map(jd,l)
    dic = {}
    for j in future:
       dic.update(j)
    print(dic)
    f = open('zuizhong.txt', 'w', encoding='utf-8')
    for k, v in dic.items():
        f.write(k + ':' + str(v) + '\n')
    f.close()

# def task(message):
#    a = []
#    for i in range(message):
#        a.append(i)
#    return a
# l = [100,200]
# def main():
#    executor = ThreadPoolExecutor(5)
#    # future = executor.submit(task, 100)
#    future = executor.map(task,l)
#    for j in future:
#        print(j)



if __name__ == '__main__':
    begin = time.time()
    main()
    end = time.time()
    t = end - begin
    print(t)
