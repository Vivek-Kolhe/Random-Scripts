import requests
from pymongo import MongoClient
from time import sleep
from .config import Configs

def send_message(message):
    requests.get(f'https://api.telegram.org/bot{Configs.BOT_TOKEN}/sendMessage?chat_id={Configs.CHANNEL_ID}&text={message}')

def send_photo(url):
    requests.post(f'https://api.telegram.org/bot{Configs.BOT_TOKEN}/sendPhoto?chat_id={Configs.CHANNEL_ID}&photo={url}')

def send_document(url):
    requests.post(f'https://api.telegram.org/bot{Configs.BOT_TOKEN}/sendDocument?chat_id={Configs.CHANNEL_ID}&document={url}')

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
    for item in response:
        if item["id"] != current_id:
            send_photo(item["sample_url"])
            sleep(2)
    if current_id != response[-1]["id"]:
        collection.update_one({"_id" : 1}, {"$set" : {"yand_id" : response[-1]["id"]}})

if __name__ == "__main__":
    main()
