from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load qna links json
with open('D:\TestOne\College360\QAN\qna_links.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Looping
start_point = 3
end_point = 3

D1 = dict()
Counting = 0

# looping qna links
for link in obj:
    # print(link)
    Counting = Counting + 1
    D2 = {}
    question_links = list()
    # print(obj[str(link)])
    R = 0
    if(Counting >= start_point):
        for i in obj[str(link)]:
            R = R + 1
            try:
                answer_text = ''
                req = Request(i)
                html_page = urlopen(req)
                soup = BeautifulSoup(html_page, "lxml")
                head_question = soup.find('h1').text
                answer_text = soup.find(
                    "div", {'class': 'postQuestDetailBlock'}).text
                try:
                    tags = str(soup.find('div', {'class': 'tags'}).text).replace(
                        '\n', '').strip().split('#')
                    # print(tags)
                    # remove empty elements in a list
                    if(len(tags) > 0):
                        tags.remove("")
                except:
                    print("No tags found")
                    pass
                try:
                    views_count = int(str(soup.find(
                        'div', {'class': 'views tagsRight'}).text).replace('\n', '').strip().removesuffix(" Views"))
                    # print(views_count)
                except:
                    print("No views found")
                    pass
                answer_ = answer_text.replace(
                    '\n', '') if len(answer_text) > 0 else ''
                # print(answer_text)
                # print(views_count)
                D2[head_question] = [answer_, tags, views_count]
                if(R == 5):
                    break
            except:
                print("No Qna Found")
                pass
            finally:
                print('Done by ', Counting)
                '''D1[str(gallary_title.text)] = D2
                print("Done By ", Counting)'''
                pass
        D1[link] = D2

        # print(YOUTUBE_links)
        # break loop if end reached
        if(Counting == end_point):
            break

# output file saving
with open('D:\TestOne\College360\QAN\qna_card_text.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)
json_object = json.dumps(data_file, indent=4)
with open("D:\TestOne\College360\QAN\qna_card_text.json", "w") as f:
    json.dump(data_file, f)
