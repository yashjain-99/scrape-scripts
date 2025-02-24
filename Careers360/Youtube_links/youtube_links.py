from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json
from collections import OrderedDict

# Give a batch of colleges
start_point = 3
end_point = 100

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

D1 = dict()
Counting = 0

# looping
for link in obj:
    Counting = Counting + 1
    D2 = {}
    YOUTUBE_links = list()
    if(Counting >= start_point):
        try:
            QUESTION_LIST = []
            req = Request(str(obj[str(link)]))
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            gallary_title = soup.find("h1").text
            regex = re.compile('.*owl-video.*')
            for video_link in soup.find_all("a", {"class": regex}, href=True):
                if(str(video_link['href']).strip('"').startswith('http')):
                    YOUTUBE_links.append(str(video_link['href']).strip('"'))
        except:
            print("No video Found")
            pass
        finally:
            print('Done by ', Counting)
            '''D1[str(gallary_title.text)] = D2
            print("Done By ", Counting)'''
            pass

        # add every college youtube url's List
        D1[link] = list(OrderedDict.fromkeys(YOUTUBE_links))

        # print(YOUTUBE_links)
        # if the range is reached then loop will be terminated
        if(Counting == end_point):
            break

# Reading a raw file as a dict object
with open('D:\\TestOne\\College360\\Video\\Youtube_links.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)

# updatng D1 and saving as a file --> Youtube_links.json
json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\Video\\Youtube_links.json", "w") as f:
    json.dump(data_file, f)
