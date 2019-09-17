import requests,re,random
from lxml import etree

import time

class Taobao():
    def __init__(self):
        # self.url = 'https://s.taobao.com/search?spm=a217h.9580640.831011.4.7f8325aa9DUCkC&q=%E5%B0%8F%E7%B1%B3+6&app=detailproduct&app=d&through=1&from_type=3c&bcoffset=4&p4ppushleft=%2C48&s=0'
                   # 'https://s.taobao.com/search?spm=a217h.9580640.831011.4.7f8325aa9DUCkC&q=%E5%B0%8F%E7%B1%B3+6&app=detailproduct&app=d&through=1&from_type=3c&bcoffset=4&p4ppushleft=%2C48&s=44&ntoffset=4'
                   # 'https://s.taobao.com/search?spm=a217h.9580640.831011.4.7f8325aa9DUCkC&q=%E5%B0%8F%E7%B1%B3+6&app=detailproduct&app=d&through=1&from_type=3c&bcoffset=4&p4ppushleft=%2C48&s=88&ntoffset=4'
        # self.cookies = ['cna=DI1BFYv1/XMCAQFQwOL4d6b5; hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%A4%A9%E6%B0%94%E4%B8%8D%E9%94%9976368350; cq=ccp%3D0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; t=30d7d4d08bff0f03cdea45032a7bf6c6; enc=ix%2BQq1vLlMIJfYdE33tTpNX%2FG%2BTHRG9mje2nbMPS%2BKj8ugU%2BON8UQFOMfOcvv0aYAR6BjkVwBhhgy8Ne%2F6mmdQ%3D%3D; _tb_token_=35e643b50be6b; cookie2=127394d196c7f0a6e472d114be112643; dnk=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; _m_h5_tk=e93bdc346a536d41958342c249749724_1568400156515; _m_h5_tk_enc=4898898f3bf2a1b689e51c889d0fa2d8; whl=-1%260%260%260; isg=BDEx7cWbyLt8e2U72NKh56EpQL0LtqSzbPYMKBNGDvgZOlGMW205YGdYXI758j3I; l=cBEbkCRPvtdhNrFbBOCwVuI8Ll_ORIRAguPRwCxBi_5CC6L1YYbOkPbOyFp6cjWdTZLB4JuaUM29-etki0ILNztqTtrR.; uc1=cookie14=UoTaECUw8aQDTw%3D%3D&tag=8&pas=0&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&lng=zh_CN&existShop=false&cookie21=UtASsssme%2BBq; uc3=nk2=r7kg%2BU3fKYqLqFWsNKI7Kg%3D%3D&vt3=F8dByuPQWnhkEWN37pg%3D&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UUBc%2Bjc9PCnDKw%3D%3D; tracknick=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; _l_g_=Ug%3D%3D; uc4=id4=0%40U2LO7H80meMfFfGkDUWxeW0JUr%2BK&nk4=0%40rVtaEbtyo%2FuxCqz%2B60%2B3mySbBYc%2FtLQQsYno; unb=2841009050; lgc=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; cookie1=B0f7MvmKXNN1gks9%2FeqjOTeWQ%2FaJmKHUn25D4onaLkk%3D; login=true; cookie17=UUBc%2Bjc9PCnDKw%3D%3D; _nk_=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; sg=00f; csg=cb4fb8b8',
        #       'cna=eGXNFRhRSkkCAbfhJLKH8aWp; _m_h5_tk=7d827b7269161b2bec1e75221f12e13b_1565891528974; _m_h5_tk_enc=7a2b5c3133447a619a160b42f8bb9335; x=__ll%3D-1%26_ato%3D0; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTaHoqcxosmvA%3D%3D; uc3=nk2=1DsN4FjjwTp04g%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UondHPobpDVKHQ%3D%3D&vt3=F8dBy3K1GcD57BN%2BveY%3D; t=8d194ab804c361a3bb214233ceb1815c; tracknick=%5Cu4F0F%5Cu6625%5Cu7EA22013; lid=%E4%BC%8F%E6%98%A5%E7%BA%A22013; uc4=nk4=0%401up5I07xsWKbOPxFt%2Bwto8Y%2BdFcW&id4=0%40UOE3EhLY%2FlTwLmADBuTc%2BcF%2B4cKo; lgc=%5Cu4F0F%5Cu6625%5Cu7EA22013; enc=JY20EEjZ0Q4Aw%2BRncd1lfanpSZcoRHGHdAZmqrLUca8sEI9ku3vIBCYdT4Lvd9KJMVpk%2F1TnijPlCpUrJ2ncRQ%3D%3D; _tb_token_=553316e3ee5b5; cookie2=17126dd7c1288f31dc73b09697777108; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; l=cBj2amlRqUrFkhhjBOfgZuI8as7O6CvWGsPzw4_GjICP9H5cIxnlWZeaTSLkCnGVL6Dyr3RhSKO4B8YZjPathZXRFJXn9MpO.; isg=BBMTUm-GSmBFQQYmiWpbMPIdtpf9YKfi0yhVD8U0EzPgRD_mR5uf2DzSfvSPZP-C']
        # self.cookies = [
        #     'cna=DI1BFYv1/XMCAQFQwOL4d6b5; hng=CN%7Czh-CN%7CCNY%7C156; lid=%E5%A4%A9%E6%B0%94%E4%B8%8D%E9%94%9976368350; cq=ccp%3D0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; t=30d7d4d08bff0f03cdea45032a7bf6c6; enc=ix%2BQq1vLlMIJfYdE33tTpNX%2FG%2BTHRG9mje2nbMPS%2BKj8ugU%2BON8UQFOMfOcvv0aYAR6BjkVwBhhgy8Ne%2F6mmdQ%3D%3D; _tb_token_=35e643b50be6b; cookie2=127394d196c7f0a6e472d114be112643; dnk=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; _m_h5_tk=e93bdc346a536d41958342c249749724_1568400156515; _m_h5_tk_enc=4898898f3bf2a1b689e51c889d0fa2d8; whl=-1%260%260%260; isg=BDEx7cWbyLt8e2U72NKh56EpQL0LtqSzbPYMKBNGDvgZOlGMW205YGdYXI758j3I; l=cBEbkCRPvtdhNrFbBOCwVuI8Ll_ORIRAguPRwCxBi_5CC6L1YYbOkPbOyFp6cjWdTZLB4JuaUM29-etki0ILNztqTtrR.; uc1=cookie14=UoTaECUw8aQDTw%3D%3D&tag=8&pas=0&cookie15=V32FPkk%2Fw0dUvg%3D%3D&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&lng=zh_CN&existShop=false&cookie21=UtASsssme%2BBq; uc3=nk2=r7kg%2BU3fKYqLqFWsNKI7Kg%3D%3D&vt3=F8dByuPQWnhkEWN37pg%3D&lg2=UIHiLt3xD8xYTw%3D%3D&id2=UUBc%2Bjc9PCnDKw%3D%3D; tracknick=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; _l_g_=Ug%3D%3D; uc4=id4=0%40U2LO7H80meMfFfGkDUWxeW0JUr%2BK&nk4=0%40rVtaEbtyo%2FuxCqz%2B60%2B3mySbBYc%2FtLQQsYno; unb=2841009050; lgc=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; cookie1=B0f7MvmKXNN1gks9%2FeqjOTeWQ%2FaJmKHUn25D4onaLkk%3D; login=true; cookie17=UUBc%2Bjc9PCnDKw%3D%3D; _nk_=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; sg=00f; csg=cb4fb8b8', ]

        self.cookies_yonghu =         [
            'hng=CN%7Czh-CN%7CCNY%7C156; t=30d7d4d08bff0f03cdea45032a7bf6c6; thw=cn; cookie2=127394d196c7f0a6e472d114be112643; _tb_token_=35e643b50be6b; _uab_collina=156845545177502934397034; alitrackid=www.taobao.com; swfstore=266185; _m_h5_tk=e922dcd48bffa562e415e89fc52dcc2d_1568713958638; _m_h5_tk_enc=829d0639b2e228c60c81fcfcd0c07b14; x5sec=7b227365617263686170703b32223a22366666393235376131343532643338346237373939653362336163333932346443492f6a67757746454d4c6f36386a4d736133547a774561444449344e4445774d446b774e5441374d513d3d227d; cna=DI1BFYv1/XMCAQFQwOL4d6b5; v=0; unb=647387948; uc3=vt3=F8dByuKxpTjYbhjRsZI%3D&id2=VWsvF%2FsfJwfF&nk2=GhI1pONF&lg2=UtASsssmOIJ0bQ%3D%3D; csg=33c0f048; lgc=yyjyyl; cookie17=VWsvF%2FsfJwfF; dnk=yyjyyl; skt=170f34add0b8cea6; existShop=MTU2ODcxNjU2Nw%3D%3D; uc4=nk4=0%40GJ6HWFIdml9iEbKpJp%2BdXJ4%3D&id4=0%40V8o7fy8dC4QYCRknKsGiEzxWixM%3D; tracknick=yyjyyl; _cc_=VT5L2FSpdA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=l86; _nk_=yyjyyl; cookie1=VAXcdE7LSU7%2BD6%2FwN%2FflvZli%2BuxfyUexHva2lBsMeII%3D; enc=NydPg52UctX17m97OcdzCCULlvhuaoj7F%2BttCa0%2Fwtiw0qiTjTC7o0iW6Nq0akmmYKnP%2BtLpALsAHuU4S%2BNeyQ%3D%3D; JSESSIONID=CF8601F0E1A72FEA90375786EAD8F1E8; lastalitrackid=login.taobao.com; uc1=cookie16=W5iHLLyFPlMGbLDwA%2BdvAGZqLg%3D%3D&cookie21=W5iHLLyFe3xm&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&existShop=false&pas=0&cookie14=UoTaECEhF6D8lA%3D%3D&tag=8&lng=zh_CN; mt=ci=36_1; whl=-1%260%260%260; isg=BHBwrawk2fORkYULoaHy9_4rQT4CEVUgVfnti2rBXkueJRHPEsp_kmoXeW3gswzb; l=cBL166RlqcghV2akBOCaVuI8Ll_9hIRYouPRwCxBi_5B96Ysn87Oks3lhFv6cjWd9VTB4JuaUMv9-etkihX_Ju--g3fP.; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0']

        # w\无用户名
        # self.cookies = [
        #     'cna=IKHYFN36P2wCASQoDLOSv/T2; isg=BObmQIgFh_GSeVIrHZym-wb0NFyobyuiUkyHJtCOu4kTU4NtOFQNkIRlq4_6YCKZ; l=cBP1QAHIvQ-cTOpABOfamuI8Ll_TCIOVhkPzw4OMDICP_HCfok9cWZCx86YWCn1VL6bBR3JceFJJBfLiYy4EhZXRFJXn9MpO.; lid=%E5%A4%A9%E6%B0%94%E4%B8%8D%E9%94%9976368350; enc=PMxh%2Fv4DyjT30Ls9dB8sXL3uoN7ylvukwBXYsGIsLK8TbMp1C1G4MDlG9myq5%2FWx%2BzPbrC0cCczvT8gT87lolQ%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; t=d1e6d7e9be8ebebf64053d51f758fd93; uc3=vt3=F8dByuPQWntrfkl85z4%3D&id2=UUBc%2Bjc9PCnDKw%3D%3D&nk2=r7kg%2BU3fKYqLqFWsNKI7Kg%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; uc4=nk4=0%40rVtaEbtyo%2FuxCqz%2B60%2B3mySbBYc%2FtLQXwX52&id4=0%40U2LO7H80meMfFfGkDUWxeW0OIe%2Fo; lgc=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; _tb_token_=77ed85b83b718; cookie2=158e2cc5ad36ed3fade106c73c607fb2; x5sec=7b22726174656d616e616765723b32223a226130336563303239353163303739353762376633653339343137386434303135434f6e3767757746454a6d4b6c38724c394a655448513d3d227d']
        # w\无用户名
        self.cookies_noyong_hu = [
            'cna=IKHYFN36P2wCASQoDLOSv/T2; isg=BP__ibagnracY5vUnJ8v3PfnjdNJTFKlW0BKGZHMLa4YoBwimbe01gX24rD74yv-; l=cBP1QAHIvQ-cTCMfBOfZVuI8Ll_teIRV1kPzw4OMDICP_9fluXbcWZCYG_8DCn1VK6JyR3Pio2zJBcLGLyCVokb4d_Bkdl5..; lid=%E5%A4%A9%E6%B0%94%E4%B8%8D%E9%94%9976368350; enc=PMxh%2Fv4DyjT30Ls9dB8sXL3uoN7ylvukwBXYsGIsLK8TbMp1C1G4MDlG9myq5%2FWx%2BzPbrC0cCczvT8gT87lolQ%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; x5sec=7b22726174656d616e616765723b32223a226130336563303239353163303739353762376633653339343137386434303135434f6e3767757746454a6d4b6c38724c394a655448513d3d227d; t=d1e6d7e9be8ebebf64053d51f758fd93; uc3=vt3=F8dByuPQWntrfkl85z4%3D&id2=UUBc%2Bjc9PCnDKw%3D%3D&nk2=r7kg%2BU3fKYqLqFWsNKI7Kg%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; uc4=nk4=0%40rVtaEbtyo%2FuxCqz%2B60%2B3mySbBYc%2FtLQXwX52&id4=0%40U2LO7H80meMfFfGkDUWxeW0OIe%2Fo; lgc=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; _tb_token_=35559e3b3717; cookie2=1cd3f63d695e190494afc1a3d27082c5']
        # self.cookies = ['cna=IKHYFN36P2wCASQoDLOSv/T2; isg=BI-PwqN-DgaAUwuEjK-_LOeXHSNZHOL1S3D6qaGdFP6ncKpyqYcpJwYmcmDrE7tO; l=cBP1QAHIvQ-cTGDfBOfaiuI8Ll_O2IOVhkPzw4OMDICP_m1v13p1WZCYA38JCn1VLsGpR3Pio2zJB0TgAyznhZXRFJXn9MpO.; lid=%E5%A4%A9%E6%B0%94%E4%B8%8D%E9%94%9976368350; enc=PMxh%2Fv4DyjT30Ls9dB8sXL3uoN7ylvukwBXYsGIsLK8TbMp1C1G4MDlG9myq5%2FWx%2BzPbrC0cCczvT8gT87lolQ%3D%3D; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; x=__ll%3D-1%26_ato%3D0; t=d1e6d7e9be8ebebf64053d51f758fd93; uc3=vt3=F8dByuPQWntrfkl85z4%3D&id2=UUBc%2Bjc9PCnDKw%3D%3D&nk2=r7kg%2BU3fKYqLqFWsNKI7Kg%3D%3D&lg2=UIHiLt3xD8xYTw%3D%3D; tracknick=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; uc4=nk4=0%40rVtaEbtyo%2FuxCqz%2B60%2B3mySbBYc%2FtLQXwX52&id4=0%40U2LO7H80meMfFfGkDUWxeW0OIe%2Fo; lgc=%5Cu5929%5Cu6C14%5Cu4E0D%5Cu951976368350; _tb_token_=35559e3b3717; cookie2=1cd3f63d695e190494afc1a3d27082c5; x5sec=7b22726174656d616e616765723b32223a223637306163386165316532316566373137353536646638623564626636613765434e7261672b7746454c507a2b38756e744937717541453d227d']
        self.user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36',]
    def get_proxy(self):
        res = requests.get(
            'http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=1&time=100&pro=&city=&port=1&format=json&ss=5&css=&ipport=1&dt=1&specialTxt=3&specialJson=&usertype=2')
        # 'http://t.11jsq.com/index.php/api/entry?method=proxyServer.generate_api_url&packid=0&fa=0&fetch_key=&groupid=0&qty=1&time=101&pro=&city=&port=1&format=json&ss=5&css=&ipport=1&dt=1&specialTxt=3&specialJson=&usertype=2'
        a = res.text
        pattern = re.compile(r'"IP":"(.*?)"')
        ip_list = pattern.findall(a)
        ip = random.choice(ip_list)
        print(ip)
        ip = {'http': 'http://{}'.format(ip),
     'https': 'http://{}'.format(ip), }

        return ip

    def get_header_yonghu(self):
        cookie = random.choice(self.cookies_yonghu)
        user_agent = random.choice(self.user_agents)
        header={
            'cookie': cookie,
            "referer":"https://item.taobao.com",
            "user-agent":user_agent,
        }
        return header

    def get_header_noyong_hu(self):
        cookie = random.choice(self.cookies_noyong_hu)
        user_agent = random.choice(self.user_agents)
        header={
            'cookie': cookie,
            "referer":"https://item.taobao.com",
            "user-agent":user_agent,
        }
        return header

    def get_content(self):
        f = open('taobao_comments.txt', 'w', encoding='utf8')
        for page in range(20):
            print('这是第',page+1,'页')
            url = 'https://s.taobao.com/search?spm=a217h.9580640.831011.4.7f8325aa9DUCkC&q=小米+6&app=detailproduct&app=d&through=1&from_type=3c&bcoffset=4&p4ppushleft=%2C48&ntoffset=4&s={}'.format(page*44)
            response = requests.get(url=url, headers=self.get_header_yonghu())
            html_doc = response.content.decode('utf-8')
            # print(html_doc)
            pattern = re.compile(r'"detail_url":"(.*?)"')
            all = pattern.findall(html_doc)
            # print(all)
            for i in all:
                i =  i.encode('utf-8').decode("unicode_escape")
                i = 'https:' + i
                print(i)
                res2 = requests.get(url=i,headers=self.get_header_noyong_hu()).text
                # pattern2 = re.compile(r'"itemId":(.*?),"sellerId":(.*?),".*?"spuId":(.*?)')

                pattern2 = re.compile(r'itemId:"(.*?)"')
                itemId = pattern2.findall(res2)
                if itemId == []:
                    pattern2 = re.compile(r'itemid="(.*?)"')
                    itemId = pattern2.findall(res2)
                itemId = itemId[0]

                pattern2 = re.compile(r'sellerId:"(.*?)"')
                sellerId = pattern2.findall(res2)
                if sellerId == []:
                    pattern2 = re.compile(r'sellerid="(.*?)"')
                    sellerId = pattern2.findall(res2)
                sellerId = sellerId[0]

                pattern2 = re.compile(r'"spuId":"(.*?)"')
                spuId = pattern2.findall(res2)
                if spuId == []:
                    pattern2 = re.compile(r'spuId=(.*?)')
                    spuId = pattern2.findall(res2)
                spuId = spuId[0]
                print(itemId,sellerId,spuId)
                sellerId_comments = {}
                comments_lists = []
                for comments in range(1, 3):
                    # url = 'https://s.taobao.com/search?spm=a217h.9580640.831011.4.7f8325aa9DUCkC&q=%E5%B0%8F%E7%B1%B3+6&app=detailproduct&app=d&through=1&from_type=3c&bcoffset=4&p4ppushleft=%2C48&s={}'.format(j*44)
                    # 'https://rate.tmall.com/list_detail_rate.htm?itemId=598173320467&spuId=1318143549&sellerId=1714128138&order=3&currentPage=1&append=0&content=1&tagId=&posi=&picture=0&groupId=&ua=098%23E1hvd9vpvB6vUvCkvvvvvjiPRFLw1jYPPL5Ozj3mPmPOgjlRRFqUljiPRFdZgjDP9phvHHiao8mXzHi47keQt1s479D4NYGBdphvmpvW%2FOArdpvf9u6Cvvyv2j6nazwvhtejvpvhvvpvv8wCvvpvvUmmKphv8vvvvvCvpvvvvvmm86CvCvyvvUUdphvWvvvv9krvpv3Fvvmm86CvmVREvpvVmvvC9jaCuphvmvvv9bX%2F09zumphvLCv%2BupvjOrjxAfyp%2B3%2BSaNoxfBkKf9033wynrsUDXnV9D704deDHD7zOaXT4ahxtD7zpd3ODNrClYh6TRoDj5fkXAfJ0v0KHAp0YWdUCvpvVvmvvvhCv2QhvCvvvMMGtvpvhvvvvv86CvvyvmjAm3IOv4dorvpvEvv3K2ZxHvRULdphvmpvWmIAQ%2BvvsAsyCvvpvvvvv&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1568714068798_3406&callback=jsonp3407'
                    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId={}&spuId={}&sellerId={}&order=3&currentPage={}&append=0&content=1&tagId=&posi=&picture=0&groupId=&callback=jsonp3337'.format(itemId,spuId,sellerId,comments)
                    response = requests.get(url=url, headers=self.get_header_noyong_hu())
                    html_doc = response.content.decode('utf-8')
                    # print(html_doc)
                    pattern3 = re.compile(r'"rateContent":"(.*?)"')
                    b = pattern3.findall(html_doc)
                    print(b)
                    comments_lists.append(b)
                    sellerId_comments[sellerId] = comments_lists

                f.write(str(sellerId_comments) + '\n')
        f.close()





tb = Taobao()
tb.get_content()



