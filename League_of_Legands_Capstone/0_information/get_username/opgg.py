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

def travel_world(headers, names, area, highpages, hrange, lowpages, lrange):
    # go throught 4 different main area, and grab userID from opgg
    # set headers to csv file
    headerList = ["userID", "username", "ranking"]
    with open(names+".csv", 'w') as file:
        dw = csv.DictWriter(file, delimiter=',',fieldnames=headerList)
        dw.writeheader()

    # high rank player data
    page = 1
    loading = 0
    while page <= highpages:
        second = sleep_time(0, 0, random.randint(8, 30))
        name = "https://" + area +"op.gg/ranking/ladder/page=" + str(page)
        html=requests.get(name,headers=headers).text
        doc=pq(html)

        for items in get_message(doc("tbody").find("tr").items()):
        	#go throught every tr and find information
            write_csv(items,names)

        print("high rank player loading page number " + str(page))
        page += hrange
    # low rank player data
    while page <= lowpages:
        second = sleep_time(0, 0, random.randint(8, 30))
        name = "https://" + area +"op.gg/ranking/ladder/page=" + str(page)
        html=requests.get(name,headers=headers).text
        doc=pq(html)

        for items in get_message(doc("tbody").find("tr").items()):
        	#go throught every tr and find information
            write_csv(items,names)

        print("lower rank player loading page number " + str(page) + "/ Total " + str(lowpages))
        page += lrange

    print("Data loading completed!")

if __name__ == '__main__':
    # set headers
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400", "Accept-Language":"en-US,en;q=0.9"}
    # stratified sampling

    # Get NA userID
    area = "na."
    highpages = 45
    lowpages = 19720
    hrange = 1
    lrange = 30
    names = "ranking information -- NA"
    travel_world(headers, names, area, highpages , hrange, lowpages, lrange)
    print("NA is completed")

    # Get KR  userID
    area = "www."
    highpages = 55
    lowpages = 48420
    hrange = 1
    lrange = 70
    names = "ranking information -- KR"
    travel_world(headers, names, area, highpages , hrange, lowpages, lrange)
    print("KR is completed")

    # Get EUW userID
    area = "euw."
    highpages = 50
    lowpages = 39100
    hrange = 1
    lrange = 60
    names = "ranking information -- EUW"
    travel_world(headers, names, area, highpages , hrange, lowpages, lrange)
    print("EUW is completed")

    # Get EUE userID
    area = "eune."
    highpages = 40
    lowpages = 19000
    hrange = 1
    lrange = 30
    names = "ranking information -- EUNE"
    travel_world(headers, names, area, highpages , hrange, lowpages, lrange)
    print("EUNE is completed")

    print("userID collect missing has completed")
