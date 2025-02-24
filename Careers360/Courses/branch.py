from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import re
import time

clg_link = str('https://www.careers360.com')

# Load json
with open('D:\\TestOne\\College360\\Courses\\all_filters_data.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Load Chrome Driver
PATH = 'D:\TestOne\chromedriver.exe'
s = Service(PATH)
driver = webdriver.Chrome(service=s)

# Init all variables
D1 = dict()
D2 = dict()
D3 = dict()

Counting = 0


# Give a batch of colleges
start_point = 1
end_point = 3

# Looping every college
for id in obj:
    D1 = {}
    D2 = {}

    # init variables
    Counting = Counting + 1
    cource_name_data = []
    D1 = {}

    # Start from given college
    if(Counting >= start_point):
        # url_req = str(str(obj[str(link)]) +
        #               str('/courses'))
        # print(url_req)
        # driver.get(url_req)
        branch_dict = obj[id]['branch']

        try:
            for k, v in zip(branch_dict.keys(), branch_dict.values()):
                # clear D1
                D1 = {}
                # print(k, v)
                url_req = str(v)
                driver.get(url_req)

                # find pages count
                pages_count = driver.find_element(
                    By.XPATH, '/html/body/div[2]/section[1]/div/div[2]/div[1]/div[2]/span').text
                total_c_int = re.findall(r'\d+', str(pages_count))
                total_c_int = int(total_c_int[0])
                print('Courses = ', total_c_int)

                # Page Navigation example link
                # https://www.careers360.com/university/lovely-professional-university-phagwara/courses/be-btech-idpg?page=2

                try:
                    if(total_c_int <= 30):
                        for course_name in driver.find_elements(By.CLASS_NAME, 'heading4'):
                            D1[course_name.find_element(By.TAG_NAME, 'a').text] = course_name.find_element(
                                By.TAG_NAME, 'a').get_attribute('href')
                    if(total_c_int > 30):
                        for page in range(1, int(total_c_int/30)+2):
                            try:
                                url_req_ = str(str(url_req) +
                                               str('?page=' + str(page)))
                                print(url_req_)
                                driver.get(url_req_)
                                for course_name in driver.find_elements(By.CLASS_NAME, 'heading4'):
                                    D1[course_name.find_element(By.TAG_NAME, 'a').text] = course_name.find_element(
                                        By.TAG_NAME, 'a').get_attribute('href')
                            except Exception as Msg:
                                print(Msg)
                                pass

                    D2[k] = D1

                except Exception as Msg:
                    print(Msg)
                    pass
        except:
            pass

        # merging every single filter into a single dict

        # map clg filter
        D3[id] = D2

        # print current clg number
        print('Done By ', Counting)

        # come out of loop if end_point is reached
        if(Counting == end_point):
            break
# Saving a file
# Reading a raw file as a dict object
with open('D:\\TestOne\\College360\\Courses\\all_branch_data.json', "r") as f:
    data_file = json.load(f)
data_file.update(D3)
json_object = json.dumps(data_file, indent=4)

# Writing with new dict objects
with open("D:\\TestOne\\College360\\Courses\\all_branch_data.json", "w") as f:
    json.dump(data_file, f)

# closing chrome
driver.close()
