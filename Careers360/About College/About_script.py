from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json
import requests
import re

#url = 'https://api.collegeking.in/items/college'

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Load Chrome Driver
PATH = 'D:\TestOne\chromedriver.exe'
s = Service(PATH)
driver = webdriver.Chrome(service=s)

# Initialize variables
store_data = 'NA'
clg_list = list()
D1 = dict()
D2 = dict()
D3 = dict()
H_D1 = dict()
counting = 0
start_point = 1
end_point = 2
# Looping

# Remove unnecessary highlights


def remove_dup(iter_obj):
    highlight_D1 = {}
    if('Ownership' in iter_obj.keys()):
        highlight_D1["ownership"] = iter_obj["Ownership"]
        pass
    if('Estd. Year' in iter_obj.keys()):
        highlight_D1["established_in"] = str(iter_obj["Estd. Year"]).strip()
        pass
    if('Accreditation' in iter_obj.keys()):
        highlight_D1["accredation"] = iter_obj["Accreditation"]
        pass
    if('Campus Size' in iter_obj.keys()):
        highlight_D1["campus_size"] = int(''.join(
            filter(lambda i: i.isdigit(), str(iter_obj["Campus Size"]))))
        pass
    if('Total Student Enrollments' in iter_obj.keys()):
        highlight_D1["total_enrollment"] = int(str(
            iter_obj["Total Student Enrollments"]).strip())
        pass

    # Optional parameter
    if('Total Faculty' in iter_obj.keys()):
        highlight_D1["total_faculty"] = int(str(
            iter_obj["Total Faculty"]).strip())
        pass
    return highlight_D1


# loop throgh every college
for link in obj:
    counting = counting + 1
    D2 = {}
    full_address = ''
    if(counting >= start_point):
        driver.get(str(obj[str(link)]))
        data_desc = ''

        D1 = dict()
        clg_list = []
        # Name Section
        try:
            title_name = driver.find_element(
                By.XPATH, '/html/body/div[2]/div[1]/div/div/div[2]/h1').text
        except:
            title = ''
            print('could not get Title')
            pass
        # Location Section
        '''try:
            locatedin = driver.find_element(
                By.XPATH, '/html/body/div[2]/div[1]/div/div/div[2]/span[1]').text
        except:
            locatedin = ''
            print("Location coud not found")
            pass'''

        # About Section
        try:
            xpath_lists = ['//*[@id="aboutCollege"]/div[1]/h2']
            # '//*[@id="aboutCollege"]/div[2]/div[1]/div/div/div/div/h3[2]'
            # '//*[@id="aboutCollege"]/div[2]/div[1]/div/div/div/div/p[5]'
            about_lists = ['//*[@id="aboutCollege"]/div[2]/div[1]/div/div/div/div/p[2]', '//*[@id="aboutCollege"]/div[2]/div[1]/div/div/div/div/p[3]',
                           '//*[@id="aboutCollege"]/div[2]/div[1]/div/div/div/div/h3[1]', '//*[@id="aboutCollege"]/div[2]/div[1]/div/div/div/div/p[4]']
            driver.find_element(
                By.XPATH, '//*[@id="aboutCollege"]/div[2]/div[2]/a').click()
        except:
            pass
        try:
            for xpath_i in xpath_lists:
                try:
                    store_data = driver.find_element(By.XPATH, xpath_i)
                    if(len(store_data.text) > 0):
                        store_data_list = str(store_data.text).strip()
                        try:
                            for about_list in about_lists:
                                data_obj = driver.find_element(
                                    By.XPATH, about_list)
                                data_desc += data_obj.text
                        except:
                            pass
                except:
                    print("Throw By : ", counting)
                    pass
        except:
            print('No about')
            pass

        # Highlights section
        try:
            xpath_lists = ['//*[@id="quickFacts"]/div[2]/table/tbody/tr/td[1]/div/div[2]', '//*[@id="quickFacts"]/div[2]/table/tbody/tr/td[2]/div/div[2', '//*[@id="quickFacts"]/div[2]/table/tbody/tr/td[3]/div/div[2]',
                           '//*[@id="quickFacts"]/div[2]/table/tbody/tr/td[4]/div/div[2]', '//*[@id="quickFacts"]/div[2]/table/tbody/tr/td[2]/div/div[2]', '//*[@id="quickFacts"]/div[2]/table/tbody/tr/td[5]/div/div[2]', '//*[@id="quickFacts"]/div[2]/table/tbody/tr/td[6]/div/div[2]']
            for xpath_i in xpath_lists:
                try:
                    rank = driver.find_element(By.XPATH, xpath_i)
                    if(len(rank.text) > 0):
                        rank_list = str(rank.text).strip().split('\n')
                        H_D1[rank_list[0]] = rank_list[1]
                        # print(rank_list)
                except:
                    # print(counting)
                    pass

            xpath_lists_1 = ['//*[@id="quickFacts"]/div[2]/div/div/table/tbody/tr/td[1]', '//*[@id="quickFacts"]/div[2]/div/div/table/tbody/tr/td[2]',
                             '//*[@id="quickFacts"]/div[2]/div/div/table/tbody/tr/td[3]', '//*[@id="quickFacts"]/div[2]/div/div/table/tbody/tr/td[4]', '//*[@id="quickFacts"]/div[2]/div/div/table/tbody/tr/td[5]']
            for xpath_i_1 in xpath_lists_1:
                try:
                    establish = driver.find_element(By.XPATH, xpath_i_1)
                    if(len(establish.text) > 0):
                        establish_list = str(establish.text).strip().split(':')
                        H_D1[establish_list[0]] = establish_list[1]
                    # print(establish_list)
                except:
                    # print(counting)
                    pass
        except:
            pass

        # Find full Address
        try:
            full_address = driver.find_element(
                By.XPATH, '//*[@id="genInfo"]/div[2]/div/div[2]/address').text
            # print(full_address)
            if(len(full_address) > 0):
                D1.update({"full_address": str(
                    full_address).removeprefix("Address:")})
            pass
        except:
            #print("address error")
            pass
        # print(H_D1)

        # Pushing the Data
        D1["name"] = title_name
        #D1["locatedin"] = locatedin
        D1["description"] = data_desc
        D1.update(remove_dup(H_D1))
        D3[link] = D1
        print("DOne By", counting)
        if(counting == end_point):
            break


# Reading a raw file as a dict object
with open('D:\\TestOne\\College360\\About Section\\about_clg.json', "r") as f:
    data_file = json.load(f)
data_file.update(D3)
json_object = json.dumps(data_file, indent=4)

# Writing with new dict objects
with open("D:\\TestOne\\College360\\About Section\\about_clg.json", "w") as f:
    json.dump(data_file, f)

# closing chrome
driver.close()
