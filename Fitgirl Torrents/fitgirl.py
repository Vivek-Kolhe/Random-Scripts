import requests
from bs4 import BeautifulSoup
import pyperclip

query = input("Search repack? ").replace(" ", "+")
base_url = "https://fitgirlrepacks.co/search/"

response = requests.get(base_url + query)
soup = BeautifulSoup(response.text, "html.parser")
data = soup.find_all(class_ = "entry-title")
links, magnets = [], []

for i in range(len(data)):
    title = data[i].text
    link = data[i].find("a")["href"]
    print(f"{i+1}. {title}")
    links.append(link)

choice = int(input("Enter index of the repack: "))
print("Fetching repack details..\n-------")
response = requests.get(links[choice-1])
soup = BeautifulSoup(response.text, "html.parser")
content = soup.find(class_ = "entry-content")
repack_details = content.text
temp = repack_details.find("Download Mirrors")
repack_details = repack_details[1:temp-3]
print(repack_details)
ul = content.find("ul")
all_links = ul.find_all("a", href = True)
print("-------\nFetching magnets..")
for i in range(len(all_links)):
    if "magnet" in all_links[i]["href"]:
        magnets.append(all_links[i]["href"])

for i in range(len(magnets)):
    print(f"{i+1}. {magnets[i]}")

ind = int(input("Enter index of the magnet to copy: "))
try:
    pyperclip.copy(magnets[ind-1])
    print("Magnet copied to your clipboard.")
except Exception:
    print("Enter valid index!")