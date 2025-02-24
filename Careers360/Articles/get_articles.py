import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

D1 = dict()
D2 = dict()
D3 = dict()
L2 = []

# Load Json
with open('articles_hyperlink_dict.json', 'r') as f:
    obj = json.loads(f.read())
# print(obj)

# Load Chrome Driver
PATH = 'D:\TestOne\chromedriver.exe'
s = Service(PATH)
driver = webdriver.Chrome(service=s)

# Give a batch of colleges
start_point = 1
end_point = 3619

Counting = 0
# Looping every college
for get_link in obj:

    # init variables
    Counting = Counting + 1
    D1 = {}
    D2 = {}

    # get link dict
    # print(obj[get_link])

    # Start from given college
    if(Counting >= start_point):
        try:
            url_req = obj[get_link]
            driver.get(url_req)
            # time.sleep(2)
            author_find = driver.find_element(By.CLASS_NAME, 'author')
            posted_by = author_find.find_element(By.TAG_NAME, 'a').text
            L = str(author_find.text).split('on')
            date_posted = str(L[1][0:13]).strip()
            print(date_posted)
            print(posted_by)
            D1 = {
                'article_title': get_link,
                'posted_by': posted_by,
                'date_posted': date_posted,
                'hyperlink': obj[get_link]
            }
        except Exception as msg:
            D1 = {
                'article_title': get_link,
                'posted_by': '',
                'date_posted': '',
                'hyperlink': obj[get_link]
            }
            print(msg)
            pass

        finally:
            print("Done By ", Counting)
            pass

        D3[get_link] = D1
        # Condition to break a loop
        if(Counting == end_point):
            break

# print(D3)
# Saving a file

# Reading a raw file as a dict object
with open('articles_data.json', "r") as f:
    data_file = json.load(f)
data_file.update(D3)

json_object = json.dumps(data_file, indent=4)
with open("articles_data.json", "w") as f:
    json.dump(data_file, f)

# closing driver
driver.close()
