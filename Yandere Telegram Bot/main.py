import requests
from pymongo import MongoClient
from time import sleep
from config import Configs

def send_message(message):
    requests.get(f'https://api.telegram.org/bot{Configs.BOT_TOKEN}/sendMessage?chat_id={Configs.CHANNEL_ID}&text={message}')

def send_photo(url, caption):
    return requests.post(f'https://api.telegram.org/bot{Configs.BOT_TOKEN}/sendPhoto?chat_id={Configs.CHANNEL_ID}&photo={url}&caption={caption}').json()

def send_document(url, caption):
    return requests.post(f'https://api.telegram.org/bot{Configs.BOT_TOKEN}/sendDocument?chat_id={Configs.CHANNEL_ID}&document={url}&caption={caption}').json()

def api_response():
    return requests.get("https://yande.re/post.json?limit=100").json()

def main():
    response = api_response()[::-1]
    collection = MongoClient(Configs.MONGO_URI)["db"]["col"]
    if not collection.count_documents({}):
        collection.insert_one({"_id" : 1, "yand_id" : response[-1]["id"]})
        send_photo(response[-1]["sample_url"])
        send_document(response[-1]["file_url"])
    current_id = list(collection.find({"_id" : 1}))[0]["yand_id"]
    if current_id != response[-1]["id"]:
        filtered = list(filter(lambda x: x["id"] > current_id, response))
        for item in filtered:
            # simple hack to escape '#' and spaces.
            tags = '%20'.join(list(map(lambda x: f'%23{x}', item['tags'].split())))
            print(tags)
            r = send_photo(item["sample_url"], tags)
            # checking if the image was sent successfully, if not returning none and keeping track of last successfully sent image.
            if not r["ok"]:
                current_ind = filtered.index(item)
                collection.update_one({"_id" : 1}, {"$set" : {"yand_id" : filtered[current_ind-1]["id"]}})
                return
            send_document(item["file_url"], tags)
            sleep(2)
        collection.update_one({"_id" : 1}, {"$set" : {"yand_id" : filtered[-1]["id"]}})

if __name__ == "__main__":
    main()
