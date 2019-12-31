#-*- encoding: gb18030 -*-
'''
Created on 2019年12月31日

@author: sanoi
'''
import collections
url = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "http://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]

splited_url = [i.split('/')[-1] for i in url]
counter = collections.Counter(splited_url)
counter = counter.most_common(3)
for p in counter:
    print('{} {}'.format(p[0], p[1]))