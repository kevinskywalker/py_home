# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 20:43:03 2017

@author: HOME
"""

import requests as req
import  bs4


"""
warning:
hx_tougu
hx_attention
hx_gegu
"""


def hx_crawl():
    
    url = 'http://www.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'newsList'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
  
    
def hx_news():
    
    url = 'http://news.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'m_news'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_event():
    
    url = 'http://news.hexun.com/events/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'w_620'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
    
def hx_stock():
    
    url = 'http://stock.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'newsList'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_yanbao():
    
    url = 'http://yanbao.stock.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'yb_list03'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_yanbao():
    
    url = 'http://yanbao.stock.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'yb_list03'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_opinion():
    
    url = 'http://opinion.hexun.com/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'style':'display:none;'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    
def hx_mingjia():
    
    url = 'http://news.hexun.com/socialmedia/'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('gbk')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'newsTitle'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
'''
===============================================================
'''
    
    
def hx_gegu():
    
    url = 'http://stockdata.stock.hexun.com/000001.shtml'
    
    headers = {'Accept': 'image/png, image/svg+xml, image/jxr, image/*; q=0.8, */*; q=0.5',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN',
               'Connection': 'Keep-Alive',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032037441461c6ebdf8d5e64f828e96646fd3165cb7&CITY=11&TOWN=0; ADVC=352a875e1969f9; ADVS=352a875e37062f; ASL=17320,0000z,d3640bae; UM_distinctid=15c6df61fae234-097d0f1f3b96e6-572f7b6e-100200-15c6df61fafc0b',
               'Host': 'i0.hexun.com',
               'Referer': 'http://www.hexun.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'}
    
    re = req.get(url,headers).content.decode('utf-8')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'newsTitle'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    

    
    
def hx_attention():
    
    url = 'http://focus.stock.hexun.com/000815.html'
    
    headers = {'Host': 'focus.stock.hexun.com',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'Accept-Encoding': 'gzip, deflate',
               'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032221440740765dbe6476b4af798503d2e583b1aa9&CITY=11&TOWN=0; ADVC=352a95e6595542; ADVS=352a95e6595542; ASL=17320,0000z,d3640bae; UM_distinctid=15c6e555e29c5-055b5cc221ffb28-1263684a-100200-15c6e555e2a283; cn_1261777628_dplus=%7B%22distinct_id%22%3A%20%2215c6e555e29c5-055b5cc221ffb28-1263684a-100200-15c6e555e2a283%22%2C%22sp%22%3A%20%7B%22userID%22%3A%20%22%22%2C%22userName%22%3A%20%22%22%2C%22userType%22%3A%20%22nologinuser%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201496500625%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201496500625%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D%2C%22initial_view_time%22%3A%20%221496499374%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fwww.hexun.com%2F%22%2C%22initial_referrer_domain%22%3A%20%22www.hexun.com%22%7D; JSESSIONID=03BA38CB186C980798EBBEE4831E58E9; hxck_webdev1_general=stocklist=000001_2; __utma=194262068.1101011300.1496501877.1496501877.1496501877.1; __utmb=194262068.4.9.1496501938471; __utmc=194262068; __utmz=194262068.1496501877.1.1.utmcsr=hexun.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1',
               'Connection': 'keep-alive',
               'Upgrade-Insecure-Requests': '1'}
    
    re = req.get(url,headers,allow_redirects=False)
    print(re)
    print('+++++++++++++++++++')
    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'id':'gzdadd1'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
        
        
hx_attention()
        
        
def hx_tougu():
    
    url = 'http://tg.hexun.com/'
    
    headers = { 'Host': 'tg.hexun.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                'Accept-Encoding': 'gzip, deflate',
                'Cookie': 'hxck_sq_common=LoginStateCookie=; HexunTrack=SID=201706032221440740765dbe6476b4af798503d2e583b1aa9&CITY=11&TOWN=0; ADVC=352a95e6595542; ADVS=352a95e6595542; ASL=17320,0000z,d3640bae; UM_distinctid=15c6e555e29c5-055b5cc221ffb28-1263684a-100200-15c6e555e2a283; __jsluid=c5947ef5c9ec91df8971dc16cbb74336; ASP.NET_SessionId=i5iuhe51rjtedhukxt1osipl; Hm_lvt_ad7eb127614b0630cd8ab3125e08ad22=1496500128,1496500495; Hm_lpvt_ad7eb127614b0630cd8ab3125e08ad22=1496500613; CNZZDATA1261777628=1273169254-1496499374-http%253A%252F%252Fwww.hexun.com%252F%7C1496496967; CNZZDATA1261308438=701379351-1496496904-http%253A%252F%252Fwww.hexun.com%252F%7C1496496904; cn_1261777628_dplus=%7B%22distinct_id%22%3A%20%2215c6e555e29c5-055b5cc221ffb28-1263684a-100200-15c6e555e2a283%22%2C%22sp%22%3A%20%7B%22userID%22%3A%20%22%22%2C%22userName%22%3A%20%22%22%2C%22userType%22%3A%20%22nologinuser%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201496500625%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201496500625%2C%22%24recent_outside_referrer%22%3A%20%22%24direct%22%7D%2C%22initial_view_time%22%3A%20%221496499374%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fwww.hexun.com%2F%22%2C%22initial_referrer_domain%22%3A%20%22www.hexun.com%22%7D',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'If-Modified-Since': 'Sat, 03 Jun 2017 14:34:30 GMT',
                'If-None-Match': 'W/"2216ae8276dcd21:2565"',
                'Cache-Control': 'max-age=0'}
    
    re = req.get(url,headers).content.decode('utf-8')

    
    print(re)
    print('+++++++++++++++++++')
    soup = bs4.BeautifulSoup(re)
    results = soup.find_all(attrs={'class':'list-nes-a.mt14'})
    
    final=[]
    for result in results :
        result_news = result.get_text()
        print(result.get_text())
        final.append(result_news)
    
    
    
    print(final)
    
    
    




    


