import urllib.request
from urllib import *
import time
import os
import re

# https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html
headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	}
url = 'https://search.51job.com/list/200200,000000,0000,00,9,99,{},2,{}.html'
start_page = int(input('请输入起始页码：'))
end_page = int(input('请输入结束页码：'))
job = input('请输入查找工作：')
d = 0
alllong = 0
for page in range(start_page,end_page+1):
    new_url = url.format(parse.quote(job),page)
    request = urllib.request.Request(url=new_url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('gbk')
# pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)" alt="(.*?)" />.*?</div>', re.S)
# ret = pattern.findall(content)
# 1.5-3万/月
    pattern1 = re.compile(r'.*?<span class="t4">(\S{1,4})-(\S{1,4})万/月</span>.*?',re.S)
    ret1 = pattern1.findall(content)[1:]
    long1 = len(ret1)
   
    for t in ret1:
        a = float(t[0])
        b = float(t[1])     
        c = (a + b)/2
        d += c
    alllong += long1


    pattern2 = re.compile(r'.*?<span class="t4">(\S{1,4})-(\S{1,4})千/月</span>.*?',re.S)
    ret2 = pattern2.findall(content)[1:]
    long2 = len(ret2)
   
    for t in ret2:
        a = float(t[0])
        b = float(t[1])     
        c = ((a + b)/2)*0.1
        d += c
    alllong += long2

e = d/alllong
        

    # with open('salary.txt','w',encoding='utf8') as f:
    #     f.write(all)
print(e)

