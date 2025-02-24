from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# init attributes
D1 = dict()
HTTP_links = list()
Counting = 0

# range of colleges
start_point = 1
end_point = 100

# looping through dict
for link in obj:

    Counting = Counting + 1

    # Start from given college
    if(Counting >= start_point):
        try:
            HTTP_links = []
            req = Request(str(obj[str(link)]))
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            mydivs = soup.find_all(
                "div", {"class": "galleryGrid gallerySlider"})
            gallary_title = soup.find("h1")
            # print(gallary_title.text)
            img_lists = str(mydivs).split('<img')
            # print(img_lists)
            text_data = ''
            for element in img_lists:
                try:
                    text_data = str(element)
                    hyper_links = re.search(r'src="(.*?)"', text_data).group(1)
                    # print(hyper_links)
                    if(hyper_links != ''):
                        HTTP_links.append(hyper_links)
                    else:
                        continue
                except Exception as msg:
                    print("Throw")
                    pass
        except:
            print("No image Found")
            pass
        finally:
            D1[link] = HTTP_links
            print("Done By ", Counting)
            pass

        # Condition to break a loop
        if(Counting == end_point):
            break

# Saving links
with open('D:\\TestOne\\College360\\Gallary\\gallary_final.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)

json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\Gallary\\gallary_final.json", "w") as f:
    json.dump(data_file, f)
