#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'admin'
import requests  # 用于获取网页
from bs4 import BeautifulSoup  # 用于解析网页
from qbittorrent import Client

# 替换成自己的qbWbe地址
clientUrl = ''
# 替换成自己的username
clientUserName = ''
# 替换成自己的password
clientPassWord = ''
# 替换成自己的user_agent
user_agent = ''
# 替换成自己的cookie
cookie = ''
savePath = '/Users/admin/Downloads/ggn'


def fun():
    qb = Client(clientUrl)
    qb.login(clientUserName, clientPassWord)
    # print(qb.qbittorrent_version)
    # qb.download_from_link(link, paused=True, savepath=savePath, skip_checking=False)

    headers = {
        'User-Agent': user_agent,
        'Cookie': cookie
    }
    i = 1
    page = 25 + 3
    linkList = []
    while i <= page:
        urlAddr = 'https://gazellegames.net/'
        url = 'https://gazellegames.net/torrents.php?page={page}&artistname=&action=advanced&groupname=&year=&remastertitle=&remasteryear=&releasetitle=&releasegroup=&filelist=&userrating=&metarating=&ignrating=&gsrating=&encoding=&format=&region=&language=&rating=&miscellaneous=&scene=&dupable=&freetorrent=&gamedox=&gamedoxvers=Version+%28x.x.x.x%29&taglist=&tags_type=1&hide_dead=1&order_by=size&order_way=asc&empty_groups=filled' \
            .format(page=i)
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        # print(res.text)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup)  # 可以看到网页的内容
        #
        t1 = soup.find_all('a', title="Download")
        j = 1
        for t2 in t1:
            t3 = t2.get('href')
            if j > 5:
                linkList.append(urlAddr + t3)
            j += 1
        if linkList.__len__() > 2100:
            break
        print(i, j, linkList.__len__())
        i += 1
    try:
        qb.download_from_link(linkList, paused=True, savepath=savePath, skip_checking=False)
    except Exception as e:
        print(e, 'error')
    print(i, linkList.__len__())


if __name__ == '__main__':
    fun()
