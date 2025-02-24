import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json
# Init all variables

D1 = dict()
D2 = dict()
D3 = dict()
L2 = []

# Load Json
with open('D:\\TestOne\\College360\\premium\\temp_data.json', 'r') as f:
    obj = json.loads(f.read())
# print(obj)

# Load Chrome Driver
PATH = 'D:\TestOne\chromedriver.exe'
s = Service(PATH)
driver = webdriver.Chrome(service=s)


# Give a batch of colleges
start_point = 1
end_point = 70

Counting = 0
# Looping every college
for get_link in obj:

    # init variables
    Counting = Counting + 1
    D1 = {}
    D2 = {}

    # Start from given college
    if(Counting >= start_point):
        try:
            url_req = obj[get_link]
            driver.get(url_req)
            time.sleep(2)
            L = str(driver.find_element(
                By.CLASS_NAME, 'Premium_article_summary_author_details__lyl3s').text).split('\n')
            L2 = [tag_text.text for tag_text in driver.find_elements(
                By.CLASS_NAME, 'Premium_tags_ul_list__Y_Se3')]
            posted_by = L[1]
            date_posted = L[2]

            # save every news record
            D1 = {
                'posted_by': posted_by,
                'date_posted': date_posted,
                'tags': L2,
                'hyperlink': driver.current_url
            }
        except Exception as msg:
            print(msg)
            pass

        finally:
            print("Done By ", Counting)
            pass

        D3[get_link] = D1

        # Condition to break a loop
        if(Counting == end_point):
            break

# Saving a file
# Reading a raw file as a dict object
with open('D:\\TestOne\\College360\\premium\\articles_miss_data.json', "r") as f:
    data_file = json.load(f)
data_file.update(D3)

json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\premium\\articles_miss_data.json", "w") as f:
    json.dump(data_file, f)

# closing driver
driver.close()
