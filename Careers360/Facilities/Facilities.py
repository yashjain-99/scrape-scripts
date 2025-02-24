from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load colleges url's json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

D1 = dict()
D2 = dict()
Counting = 0

# specifyng range of colleges
start_point = 9001
end_point = 10_000

for link in obj:
    Counting = Counting + 1
    D2 = {}
    if(Counting >= start_point):
        try:
            QUESTION_LIST = []
            req = Request(str(obj[str(link)]) + '/facilities')
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            gallary_title = soup.find("div", {"class": "courseHeading"}).text
            facilities = soup.find("div", {"class": "facilityList"})
            for element in facilities.find_all("li"):
                try:
                    question_data = str(element.text).split('\n')
                    # print(question_data)
                    D2[question_data[0].replace(
                        '\n', '').strip()] = str(question_data[1]).replace('\n', '')
                except:
                    print("Throw")
                    pass
        except:
            print("No Facility Found")
            pass
        finally:
            print('Done by ', Counting)
            pass
        D1[link] = D2
        if(Counting == end_point):
            break

# saving into json
with open('D:\TestOne\College360\Failities\Facilities_final.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)
json_object = json.dumps(data_file, indent=4)
with open("D:\TestOne\College360\Failities\Facilities_final.json", "w") as f:
    json.dump(data_file, f)
