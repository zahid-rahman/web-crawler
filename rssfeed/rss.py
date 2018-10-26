import requests
from bs4 import BeautifulSoup
from bs4.builder._lxml import LXML


# news_24 news

news24_url = "http://feeds.news24.com/articles/news24/TopStories/rss"
resp = requests.get(news24_url)
soup = BeautifulSoup(resp.content, 'xml')
items = soup.find_all('item')

# daily star news
daily_url = "https://www.thedailystar.net/frontpage/rss.xml"
resp_dsn = requests.get(daily_url)
soup_dsn = BeautifulSoup(resp_dsn.content, 'xml')
item_dsn = soup_dsn.find_all('item')

# print(soup.prettify())


# print(len(item))
# print(item[0].link.text)


# fileName = "news_24.csv"
# f = open(fileName,'w')



fileName = "rssfeed.csv";
with open(fileName, "w") as f:

    f.write("NEWS 24"+"\n"+"link:"+news24_url+"\n\n")

    news = []

    for item in items:
        news={}
        news['title'] = item.title.text
        news['description'] = item.description.text
        news['pub_date'] = item.find('pubDate').string.strip()
        news['link'] = item.find('link').string
        news['image'] = item.enclosure['url']
        # print(news,"\n")

        f.write("News title :"+news['title']+"\n"+"Description :"+news['description']+"\n"+"Publish date :"+news['pub_date']+"\n"+"link: "+news['link']+"\n""Image link :"+news['image']+"\n\n")



    f.write("-------------------------------------------------------------------------------------\n\n\n")
    f.write("DAILY STAR NEWS" + "\n" + "link:" + daily_url + "\n\n")

    news_dsn = []

    for item in item_dsn :
        news_dsn={}
        news_dsn['title'] = item.title.text
        news_dsn['description'] = item.description.text
        news_dsn['pub_date'] = item.find('pubDate').string.strip()
        news_dsn['link'] = item.find('link').string

        # print(news_dsn,"\n")

        f.write("News title :"+news_dsn['title']+"\n"+"Description :"+news_dsn['description']+"\n"+"Publish date :"+news_dsn['pub_date']+"\n"+"link: "+news_dsn['link']+"\n\n")
        # f.write("News title :"+news_dsn['title']+"\n"+"Description :"+news_dsn['description']+"\n"+"Publish date :"+news_dsn['pub_date']+"\n\n")


f.close()
