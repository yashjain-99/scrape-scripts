from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Looping
start_point = 3
end_point = 3

D1 = dict()
Counting = 0
for link in obj:
    Counting = Counting + 1
    D2 = {}
    question_links = list()
    if(Counting >= start_point):
        req = Request(str(obj[str(link)]) +
                      '/all-questions?sort_by=Popularity')
        html_page = urlopen(req)
        soup = BeautifulSoup(html_page, "lxml")
        #gallary_title = soup.find("h1").text
        #regex = re.compile('.*owl-video.*')
        pages_str = soup.find("div", {"class": "showResult"})
        no_pages = ""
        for m in str(pages_str):
            if(m.isdigit()):
                no_pages = no_pages + m
        print("Number of pages : ", no_pages)
        try:
            if(int(no_pages) == ""):
                no_pages = 10
        except:
            no_pages = 10
            pass
        for i in range(0, (int(no_pages)//10)):
            try:
                QUESTION_LIST = []
                req = Request(str(obj[str(link)]) +
                              '/all-questions?sort_by=Popularity&page='+str(i))
                html_page = urlopen(req)
                soup = BeautifulSoup(html_page, "lxml")
                #gallary_title = soup.find("h1").text
                #regex = re.compile('.*owl-video.*')
                #pages_str = soup.find("div", {"class": "showResult"})

                for video_link in soup.find_all("div", {"class": 'cardBlk noAnswer'}):
                    print(
                        'https:'+str(video_link.find('a', href=True)['href']))
                    question_links.append(
                        'https:'+str(video_link.find('a', href=True)['href']))
                if(i == 20):
                    break
            except:
                print("No qna Found")
                pass
            finally:
                #print('Done by ', Counting)
                '''D1[str(gallary_title.text)] = D2
                print("Done By ", Counting)'''
                pass
        print('Done by ', Counting)
        D1[link] = question_links
        # print(YOUTUBE_links)
        if(Counting == end_point):
            break

# save all the college qna links
with open('D:\TestOne\College360\QAN\qna_links.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)
json_object = json.dumps(data_file, indent=4)
with open("D:\TestOne\College360\QAN\qna_links.json", "w") as f:
    json.dump(data_file, f)
