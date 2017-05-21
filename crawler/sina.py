

import re
import requests as req
import bs4 as bs4
import pandas as pd 



#Global
url='http://finance.sina.com.cn/touzi/lhpromote/lhstocks.js'
#url='http://finance.sina.com.cn/realstock/company/hotstock_daily_a.js'
headers={
'Host': 'finance.sina.com.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Cookie': 'U_TRS1=000000ae.9411fad.590eff32.9b60b75f; SINAGLOBAL=211.100.11.174_1494508995.147859; UOR=www.baidu.com,blog.sina.com.cn,; ULV=1495348149816:8:8:8:211.100.11.174_1495348148.715317:1495348145262; sinaGlobalRotator_http%3A//finance.sina.com=492; SR_SEL=1_511; lxlrttp=1494936652; SUB=_2A250JUZRDeRhGeBM7lcZ8ibPyTmIHXVX5moZrDV_PUJbm9ANLVXwkW0xljnzx2NC7lRyUGS7Pr7Ndr2nOg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhuSHJ3YGJGfbSaDopfsiWX5JpX5KzhUgL.FoqESK-Reon0eo-2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMceo-f1hzRe0zf; U_TRS2=000000ae.48766508.5921338e.62e507e9; Apache=211.100.11.174_1495348148.715317; ArtiFSize=14; hqEtagMode=1; UM_distinctid=15c29f5c90a337-0e51effc864402-1263684a-100200-15c29f5c90b27b',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1'
}


#Sina
class sina_crawl:
    
    def sina_crawl1(url):

        raw_data=req.get(url=url,headers=headers).text

    
  
        process_data=raw_data.split(';')[0][23:]
        print(type(process_data))   
        list_data = eval(process_data)
        print(process_data)
        print('ok')

        #Data format
    
    
        format_data=pd.DataFrame(list_data)
    
        print(format_data)
    
    def sina_crawl2(url):

        raw_data=req.get(url=url,headers=headers).text

    
  
        process_data=raw_data.split(';')[0][27:]
        print(type(process_data))
        list_data = eval(process_data)
        print(process_data)
        print('ok')

        #Data format
    
    
        format_data=pd.DataFrame(list_data)
    
        print(format_data)
    
    
    sina_crawl2(url)





sina_crawl
