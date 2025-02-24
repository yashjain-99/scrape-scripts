from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import json

# Load json
with open('final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Load Chrome Driver
PATH = 'chromedriver.exe'
s = Service(PATH)
driver = webdriver.Chrome(service=s)

D1 = dict()
D2 = dict()
counting = 0


# for specifying explicit range
start_point = 103
end_point = 200

# Looping
for link in obj:
    counting = counting + 1
    full_address = ''
    if(counting >= start_point):
        driver.get(str(obj[str(link)]))
        try:
            elem = driver.find_element(
                By.XPATH, '/html/body/div[2]/div[1]/div/div/div[2]/span[1]').text
            print(elem, counting)
            D1[link] = str(elem).split(',')[0]
            D2[link] = str(elem).split(',')
        except Exception as error_msg:
            print(counting)
            pass
        if(counting == end_point):
            break

    # time.sleep(2)
    # D2[str(obj[str(link)])] = D1
    # print(D1)

# save city location json
with open('city_Location.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)
json_object = json.dumps(data_file, indent=4)
with open("city_Location.json", "w") as f:
    json.dump(data_file, f)

# save city with state
with open('city_with_state.json', "r") as f:
    data_file_1 = json.load(f)
data_file_1.update(D2)
json_object_1 = json.dumps(data_file_1, indent=4)
with open("city_with_state.json", "w") as f:
    json.dump(data_file_1, f)
