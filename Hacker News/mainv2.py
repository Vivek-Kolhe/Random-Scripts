import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news?p=1")
soup = BeautifulSoup(response.text, "html.parser")
data = soup.select(".storylink")
votes = soup.select(".subtext")
news = []
page = 1

def sortByPoints(x):
    return sorted(x, key = lambda y : y["Points"])[::-1]

def hackerNews(data, votes):
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
while True:
    next_page = input("Next page? (y/n)\n")
    if next_page == "y" or next_page == "Y":
        page += 1
        response = requests.get("https://news.ycombinator.com/news?p=" + str(page))
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.select(".storylink")
        votes = soup.select(".subtext")
        news = []
        pprint.pprint(hackerNews(data, votes))
    elif next_page == "n" or next_page == "N":
        print("Thnaks for using me! Give me a star if you like it!")
        break
    else:
        print("Enter either y or n! ")
