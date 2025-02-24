from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import json
import re

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Load Chrome Driver
PATH = 'D:\TestOne\chromedriver.exe'
s = Service(PATH)
driver = webdriver.Chrome(service=s)

# Init all variables
D1 = dict()
D2 = dict()

NO_RESULT = ''
Counting = 0


# Give a batch of colleges
start_point = 6
end_point = 25

# Looping every college
for link in obj:
    streams_dict = {}
    degree_dict = {}
    branch_dict = {}
    study_mode_dict = {}
    course_level_dict = {}

    # init variables
    Counting = Counting + 1
    cource_name_data = []
    D1 = {}

    # Start from given college
    if(Counting >= start_point):
        url_req = str(str(obj[str(link)]) +
                      str('/courses'))
        print(url_req)
        driver.get(url_req)

        # Find Every filter
        for filters in driver.find_elements(By.CLASS_NAME, 'filterBlk'):
            try:

                temp_list = str(filters.text).split('\n')

                # Get Stream data
                try:
                    if((temp_list[0] == 'STREAM') and not(temp_list[-1].endswith('More'))):
                        streams_src = str(driver.find_element(
                            By.XPATH, '//*[@id="courseOffered"]/div[2]/div/div/div[2]').get_attribute('innerHTML'))
                        soup = BeautifulSoup(streams_src, 'html.parser')
                        for label_stream in soup.find_all('a'):
                            # streams_dict.append(str(label_stream.text).strip())
                            # print(label_stream['href'])
                            streams_dict[label_stream.text] = str(
                                label_stream['href'])
                except:
                    pass

                # Get Degree data
                try:
                    if((temp_list[0] == 'DEGREE') and not(temp_list[-1].endswith('More'))):
                        streams_src = str(driver.find_element(
                            By.XPATH, '//*[@id="courseOffered"]/div[2]/div/div/div[1]').get_attribute('innerHTML'))
                        soup = BeautifulSoup(streams_src, 'html.parser')
                        for label_degree in soup.find_all('a'):
                            # streams_dict.append(str(label_stream.text).strip())
                            # print(label_degree['href'])
                            degree_dict[label_degree.text] = str(
                                label_degree['href'])
                except:
                    pass

                # Get Branch Data
                try:
                    if((temp_list[0] == 'BRANCH') and not(temp_list[-1].endswith('More'))):
                        branch_src = str(filters.get_attribute('innerHTML'))
                        soup = BeautifulSoup(branch_src, 'html.parser')
                        for branch_name, branch_value in zip(soup.find_all('label'), soup.find_all('input')):
                            y_value = branch_value['value']
                            branch_dict[str(branch_name.text).strip()
                                        ] = str(str(obj[str(link)]) + str('/courses?branch=' + str(y_value)))
                except:
                    pass

                # Get Study Mode data
                try:
                    if(temp_list[0] == 'STUDY MODE'):
                        for i in temp_list[1:]:
                            study_mode_dict[i] = str(str(obj[str(link)]) + str(str('/courses/') + str(i).lower().replace(
                                ' ', '-') + str('-courses-mode')))
                except:
                    pass

                # Get Course level data
                try:
                    if(temp_list[0] == 'COURSE LEVEL'):
                        for i in temp_list[1:]:
                            if (i == 'UG'):
                                course_level_dict[i] = str(
                                    str(obj[str(link)]) + str('/courses?level=1'))
                            if (i == 'PG'):
                                course_level_dict[i] = str(
                                    str(obj[str(link)]) + str('/courses?level=2'))
                            if (i == 'Doctoral'):
                                course_level_dict[i] = str(
                                    str(obj[str(link)]) + str('/courses?level=3'))
                            if (i == 'Diploma'):
                                course_level_dict[i] = str(
                                    str(obj[str(link)]) + str('/courses?level=4'))
                except:
                    pass
            except:
                print('No such element')
                pass

        # Get pop up full streams data
        try:
            if(len(streams_dict) == 0):
                streams_src = str(driver.find_element(
                    By.ID, 'browse_by_stream').get_attribute('innerHTML'))
                # print(streams_src)
                soup = BeautifulSoup(streams_src, 'html.parser')
                for label_stream in soup.find_all('a'):
                    # streams_dict.append(str(label_stream.text).strip())
                    # print(label_stream['href'])
                    streams_dict[label_stream.text] = str(
                        label_stream['href'])
        except:
            pass

        # Get pop up full degree data
        try:
            if(len(degree_dict) == 0):
                degree_src = str(driver.find_element(
                    By.ID, 'browse_by_degree').get_attribute('innerHTML'))
                soup = BeautifulSoup(degree_src, 'html.parser')
                for a_degree in soup.find_all('a'):
                    # print(a_degree['href'])
                    degree_dict[a_degree.text] = str(
                        a_degree['href'])
        except:
            pass

        # Get pop up full branch data
        try:
            if(len(branch_dict) == 0):
                branch_src = str(driver.find_element(
                    By.ID, 'moreFilterBranch').get_attribute('innerHTML'))
                soup = BeautifulSoup(branch_src, 'html.parser')
                for branch_name, branch_value in zip(soup.find_all('label'), soup.find_all('input')):
                    y_value = branch_value['value']
                    branch_dict[str(branch_name.text).strip()
                                ] = str(str(obj[str(link)]) + str('/courses?branch=' + str(y_value)))
        except:
            pass

        # print all dict
        # print(degree_dict)
        # print(streams_dict)
        # print(branch_dict)
        # print(study_mode_dict)
        # print(course_level_dict)

        # merging every single filter into a single dict
        D1 = {
            "degree": degree_dict,
            "stream": streams_dict,
            "branch": branch_dict,
            "study_mode": study_mode_dict,
            "course_level": course_level_dict
        }

        # map clg filter
        D2[link] = D1

        # print current clg number
        print('Done By ', Counting)

        # come out of loop if end_point is reached
        if(Counting == end_point):
            break

# Saving a file
# Reading a raw file as a dict object
with open('D:\\TestOne\\College360\\Courses\\all_filters_data.json', "r") as f:
    data_file = json.load(f)
data_file.update(D2)
json_object = json.dumps(data_file, indent=4)

# Writing with new dict objects
with open("D:\\TestOne\\College360\\Courses\\all_filters_data.json", "w") as f:
    json.dump(data_file, f)

# closing chrome
driver.close()
