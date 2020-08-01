import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")
data = soup.select(".storylink")
votes = soup.select(".subtext")

def sortByPoints(x):
    return sorted(x, key = lambda y : y["Points"])[::-1]

def hackerNews(data, votes):
    news = []
    for index, item in enumerate(data):
        title = item.getText()
        link = item.get("href")
        vote = votes[index].select(".score")
        if len(vote):
            points = int(vote[0].getText().replace(" points", ""))
            if points >= 100:
                news.append({"Title" : title, "Link" : link, "Points" : points})
    return sortByPoints(news)

pprint.pprint(hackerNews(data, votes))