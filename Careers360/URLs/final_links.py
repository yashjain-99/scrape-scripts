# Script Documentation
# script to extract hyperlinks of each category from careers360
# categories are IT, Medical, Pharma, Engineering etc..
# https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-india
# https://bschool.careers360.com/colleges/list-of-mba-colleges-in-india
# search in career360

# importing required libraries
import math
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# initializing variables

# specify here number of courses
number_of_colleges = 5352

HTTP_links = list()
c = 0
start_page = 1
end_page = math.ceil(number_of_colleges//30)

# looping
for page in range(start_page, end_page):

    # increment page by +1
    c = c + 1
    try:
        URL_ = " "
        URL_ = "https://it.careers360.com/colleges/list-of-bca-mca-colleges-in-india?sort=popularity&page=" + \
            str(page)
        #URL_ = "https://design.careers360.com/colleges/ranking"
        req = Request(URL_)
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        mydivs = soup.find_all("h2", {"class": "blockHeading"})
        #mydivs = soup.find_all("div", {"class": "titleDate"})
        # print(mydivs)
    except:
        pass

    try:
        text_data = ''
        for element in mydivs:
            text_data = str(element)
            hyper_links = re.search(
                r'<h2 class="blockHeading"><a href="(.*?)">', text_data).group(1)
            # print(hyper_links)
            if(hyper_links != ''):
                HTTP_links.append(hyper_links)
            else:
                pass
    except:
        print("except passed")
        pass
    print("Done By ", c)

# print(len(HTTP_links))

json_data_dict = dict()

# specify id for keys
key_i_i = 19839
for key_i in range(0, len(HTTP_links)):
    json_data_dict[str(key_i_i)] = HTTP_links[key_i]
    key_i_i = key_i_i + 1
# print(json_data_dict)


# store it in a json file
json_object = json.dumps(json_data_dict, indent=4)
with open('D:\\TestOne\\College360\\HyperLinks\\hyper_links_it.json', "a") as f:
    f.write(json_object)
