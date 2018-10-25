import requests
from bs4 import BeautifulSoup


# news_24 news

news24_url = "http://feeds.news24.com/articles/news24/TopStories/rss"
resp = requests.get(news24_url)
soup = BeautifulSoup(resp.content,'lxml')
# print(soup.prettify())

item = soup.find_all('item')
# print(len(item))
# print(item[0].link.text)


fileName = "news_24.csv"
f = open(fileName,'w')

news = []
#
for items in item :
    news={}
    news['title'] = items.title.text
    news['description'] = items.description.text
    news['pub_date'] = items.find('pubdate').string.strip()
    # news['link'] = items.find('link')
    news['image'] = items.enclosure['url']
    # print(news,"\n")

    f.write("News title :"+news['title']+"\n"+"Description :"+news['description']+"\n"+"Publish date :"+news['pub_date']+"Image link :"+"\n"+news['image']+"\n\n")


f.close()


# daily star news

daily_url = "https://www.thedailystar.net/frontpage/rss.xml"
resp_dsn = requests.get(daily_url)
soup_dsn = BeautifulSoup(resp_dsn.content,'lxml')
item_dsn = soup_dsn.find_all('item')




fileNameTwo = "daily_star_news.csv"
f = open(fileNameTwo,'w')

news_dsn = []
#
for items in item_dsn :
    news_dsn={}
    news_dsn['title'] = items.title.text
    news_dsn['description'] = items.description.text
    news_dsn['pub_date'] = items.find('pubdate').string.strip()
    # news_dsn['link'] = items.find('link').text
    # news_dsn['image'] = items.namespace('thumbnail')
    # print(news_dsn,"\n")

    f.write("News title :"+news_dsn['title']+"\n"+"Description :"+news_dsn['description']+"\n"+"Publish date :"+news_dsn['pub_date']+"\n\n")


f.close()










