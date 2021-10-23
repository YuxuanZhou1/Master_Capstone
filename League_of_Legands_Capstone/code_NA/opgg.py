import requests
from pyquery import PyQuery as pq
import csv
import re
import time
import random

def sleep_time(hour, min, sec):
    return hour * 3600 + min * 60 + sec

def get_message(five_mes):
    rank_list = []
    for items in five_mes:
        # Get userID from opgg
        userID = items.find("td.ranking-table__cell--rank").text()
        # Get username from opgg
        username = items.find("span").text()[:-4]
        # Get user rank from opgg
        rank = items.find("td.ranking-table__cell--tier").text()

        # get information
        yield{
        "userID":userID,
        "username":username,
        "ranking":rank,
        }

def write_csv(data,names):
    # set name as filename
    with open(names+".csv", "a", encoding="utf-8-sig", newline='') as file:
        fieldnames = ["userID", "username", "ranking"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)

if __name__ == '__main__':
    # set headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400", "Accept-Language":"en-US,en;q=0.9"}
    names = ("ranking information")

    page = 1

    while page != 30:
        second = sleep_time(0, 0, random.randint(8, 30))
        name = "https://na.op.gg/ranking/ladder/page=" + str(page)
        html=requests.get(name,headers=headers).text
        doc=pq(html)

        for items in get_message(doc("tbody").find("tr").items()):
        	#go throught every tr and find information
            write_csv(items,names)

        loading = page%4

        print("loading page number " + str(page) + " " + "." *loading)
        page += 1

    print("Data loading completed !")
