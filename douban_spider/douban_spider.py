#coding:utf-8
import sys
import time
import urllib
import urllib2
import requests
import random
from bs4 import BeautifulSoup

headers=[   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
        "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
        "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 "]

def douban_spider(book_tags):
    book_lists = []
    for tag in book_tags:
        title_set = set({})
        page = 0
        book_list = []
        retry = 0
        while True:
            url = 'http://www.douban.com/tag/%s/book' %tag+'?start='+str(page*15)
            try:
                request = urllib2.Request(url,headers={'User-Agent':headers[random.randint(0,8)]})
                html = urllib2.urlopen(request,timeout=10).read()
                html = str(html)
            except (urllib2.HTTPError, urllib2.URLError), e:
                print e
                continue
            
            soup = BeautifulSoup(html)
            list = soup.find('div',{'class':'mod book-list'})
            retry +=1
            if list == None and retry <100:
                continue
            elif retry >= 100 or len(list) <= 1:
                break
            for book_info in list.findAll('dd'):
                title = book_info.find('a',{'class': 'title'}).string.strip()
                if title in title_set: continue
                title_set.add(title)
                book_url = book_info.find('a',{'class': 'title'}).get('href')
                desc = book_info.find('div',{'class': 'desc'}).string.strip().split('/')
                try:
                    author_info = '/'.join(desc[0:-3])
                except:
                    author_info = '暂无'
                
                try:
                    publish_info = desc[-3]
                except:
                    publish_info = '暂无'
                    
                try:
                    data = desc[-2]
                except:
                    data = '暂无'
                    
                try:
                    price = desc[-1]
                except:
                    price = '暂无'
                    
                try:
                    rating = book_info.find('span',{'class':'rating_nums'}).string.strip()
                except:
                    rating = '0.0'
                
                book_list.append([title,rating,author_info,publish_info,data,price])
                retry = 0
            page += 1
            print 'Download the information from page %d' %page
        book_list=sorted(book_list,key=lambda x:x[1],reverse=True)
        book_lists.append(book_list)            
    return book_lists
        
    
