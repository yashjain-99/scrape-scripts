from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

question_links = list()
D1 = dict()

# Give a batch of colleges range
start_point = 111
end_point = 200

# counter variable just to track within range
Counting = 0

for link in obj:
    Counting = Counting + 1
    if(Counting >= start_point):
        try:
            print(link, Counting)
            req = Request(str(obj[str(link)]))
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            answer_text = soup.find("div", {'class': 'thumb'})
            # print(answer_text.find('img', src=True)['src'])
            # D1[link] = D2
            # print(YOUTUBE_links)
            D1[link] = answer_text.find('img', src=True)['src']
        except Exception as msg:
            print(msg, Counting)
            pass
        # if the range is reached then loop will be terminated
        if(Counting == end_point):
            break

# Reading a raw file as a dict object
with open('D:\TestOne\College360\Logos\logos.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)

# updatng D1 and saving as a file --> logos_test.json
json_object = json.dumps(data_file, indent=4)
with open("D:\TestOne\College360\Logos\logos.json", "w") as f:
    json.dump(data_file, f)
