import requests
from bs4 import BeautifulSoup

query = input("Search game? ").lower().replace(" ", "+")
def main(query):
    url = "https://repack-mechanics.com/?do=search&subaction=search&story=" + query
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    posts = soup.find_all(id = "entryID")
    titles, links = [], []

    for i in range(len(posts)):                                         # displaying available games
        title = posts[i].find(class_ = "title_poster").text
        print(f"{i+1}. {title}")
        titles.append(title)
        links.append(posts[i].find("a")["href"])

    choice = int(input("Enter index of the game to download: "))
    print("-------\nFetching Game Details: ")
    game_url = links[choice-1]
    response = requests.get(game_url)
    soup = BeautifulSoup(response.text, "html.parser")
    game_details = soup.find(class_ = "eText").text
    x = game_details.find("DESCRIPTION:")
    torrent_size = soup.select("div.tor-link span")[0].text
    torrent_link = "https://repack-mechanics.com" + soup.select("div.tor-link a")[0]["href"]
    print(game_details[1:x-2] + f"\nTorret Size: {torrent_size}\n-----")            # displaying details of selected game
    download_torrent(torrent_link)

def download_torrent(torrent_link):                                      # getting .torrent file
    download = input("Do you want to download it? (y/n): ").lower()
    if download == "y":
        response = requests.get(torrent_link)
        file_name = input("Enter name for output file: ") + ".torrent"
        open(file_name, "wb").write(response.content)
        print("Check your local directory for torrent file!")
    else:
        print("Exiting..")

main(query)
