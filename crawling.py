from selenium import webdriver
import requests
from bs4 import BeautifulSoup as BS
from urllib.request import urlopen
import re

driver_path='C:/Users/youji/Desktop/유딘/데청 경기대/crawling/chromedriver'
# url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1'
# browser = webdriver.Chrome(executable_path=driver_path) # Chrome driver
# browser.get(url)
# base_url = requests.get('https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1')
# html = BS(base_url.text, 'html.parser')
# 올바른 코드 but 100개이상?
# tr_list = html.select('form > table > tbody > tr')
# for tr in tr_list:
#         rank = tr.find('td', {'class':'rank'}).text
#         category = tr.find('td', {'class': 'subject'}).find('p',{'class':'category'}).text
#         title = tr.find('td', {'class': 'subject'}).find('a').text
#
#         subs = tr.find('td', {'class': 'subscriber_cnt'}).text
#         views = tr.find('td', {'class': 'view_cnt'}).text
#         print(rank, category, title, subs, views)
#

for i in range(1):
    base_url = requests.get('https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page='+str(i+1))
    html = BS(base_url.text, 'html.parser')
    tr_list = html.select('form > table > tbody > tr')

    rank_list=[]

    for tr in tr_list:
        totalvalue=tr.find('td', {'class': 'subject'}).text
        pattern = re.compile(r'\s+')
        totalvalue = re.sub(pattern, '', totalvalue)
        rank_list.append(totalvalue)
    print("리스트는=",rank_list[0][])

        # rank = tr.find('td', {'class':'rank'}).text
        # category = tr.find('td', {'class': 'subject'}).find('p',{'class':'category'}).text
        # title = tr.find('td', {'class': 'subject'}).find('a').text

        # subs = tr.find('td', {'class': 'subscriber_cnt'}).text
        # views = tr.find('td', {'class': 'view_cnt'}).text
        # videos = tr.find('td', {'class': 'video_cnt'}).text
        # videos = videos.strip('개')
        # print(i*100+int(rank), "category=", category, " title=", title, " 구독자수=", subs, " View수=", views, " 비디오수=", videos)

    print("="*30, "다음페이지", "="*30)


# ranks = browser.find_element_by_css_selector("tr. ")
# name = ranks.find_element_by_css_selector("a").text #왜 a가 분류가 나오지? 이름 어떻게?
# names = ranks.find_element_by_css_selector(".category").text
# print(name)
# print(names)


