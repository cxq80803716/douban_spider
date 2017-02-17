#coding:utf-8
from openpyxl import Workbook
from time import sleep
import os

path = 'D:\\BOOK\\'#第二个\是对'的转义
def save_book_lists_in_excel(book_tags,book_lists):
    wb = Workbook()
    wc = []
    for book_tag in book_tags:
        wc.append(wb.create_sheet(title=book_tag.decode()))
    for i in range(len(book_tags)):
        wc[i].append(['序号','书名','评分','作者/译者','出版社','日期','价格'])
        count = 1
        for books in book_lists[i]:
            wc[i].append([count,books[0],books[1],books[2],books[3],books[4],books[5]])
            count +=1
    if not os.path.exists(path):
        os.makedirs(path)
    list_name = path + 'book-list'
    for book_name in book_tags:
        list_name +=('-'+book_name.decode())
    list_name +='.xlsx'
    wb.save(list_name)
    print u'书籍已经存入excel中,5秒后程序自动退出'
    sleep(5)