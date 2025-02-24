from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

D1 = dict()
D2 = dict()
Counting = 0

# specify range of colleges
start_point = 3
end_point = 4

# loop from obj
for link in obj:
    Counting = Counting + 1
    D2 = {}
    if(Counting >= start_point):
        try:
            QUESTION_LIST = []
            req = Request(str(obj[str(link)]))
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            gallary_title = soup.find("h1")
            for element in soup.find_all("div", {"class": "qnaBlk"}):
                try:
                    question_data = str(element.text).split('\n')
                    while('' in question_data):
                        question_data.remove('')
                    # print(question_data)
                except:
                    print("Throw")
                    pass
                finally:
                    D2[str(question_data[0]).removeprefix('Question: ')] = str(
                        question_data[1]).removeprefix('Answer: ')
        except:
            print("No FAQ Found")
            pass
        finally:

            # add every college faq
            D1[link] = D2
            print("Done By ", Counting)
            pass

        # break loop if end college is reached
        if(Counting == end_point):
            break

# saving a file
with open('D:\\TestOne\\College360\\faq\\faq_final.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)

json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\faq\\faq_final.json", "w") as f:
    json.dump(data_file, f)
