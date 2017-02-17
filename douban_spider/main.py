#coding:utf-8
from douban_spider import douban_spider
from save_book_lists_in_excel import save_book_lists_in_excel
if __name__ == '__main__':
    book_tags =['二次元','东野圭吾']  #在此输入想要搜索的标签,输入几个都可以，记得加''
    book_lists = douban_spider(book_tags)
    save_book_lists_in_excel(book_tags,book_lists)