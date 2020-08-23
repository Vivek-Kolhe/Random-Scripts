import requests
from random import randrange
from bs4 import BeautifulSoup

choice = input("Want me to fetch:\n1. A random movie\n2. A random tv series\n")
if choice == "1":
    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
elif choice == "2":
    url = "https://www.imdb.com/chart/toptv?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=cb6cf75a-1a51-49d1-af63-8202cfc3fb01&pf_rd_r=GJH80BS3XMSJVNB4689J&pf_rd_s=right-4&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_ql_6"

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("Fetching a random title for you to watch..\n------")
    titles, years, ratings, starring = [], [], [], []

    for title in soup.select("td.titleColumn a"):
        titles.append(title.text)
    for year in soup.select("td.titleColumn span.secondaryInfo"):
        years.append(year.text[1:5])
    for stars in soup.select("td.titleColumn a"):
        starring.append(stars["title"])
    for rate in soup.find_all(class_ = "ratingColumn imdbRating"):
        ratings.append(rate.text.strip())

    while True:
        i = randrange(250)
        print(f"Title: {titles[i]}\nYear: {years[i]}\nRating: {ratings[i]}\nStarring: {starring[i]}")
        user_input = input("Want me to fetch another title (y/n)? ").lower()
        if user_input != "y":
            print("Exiting..")
            break
except Exception:
    print("Invalid choice. Exiting..")