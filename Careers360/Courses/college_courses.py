from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Init all variables
D1 = dict()
D2 = dict()
D3 = dict()
detailed_data = list()
cource_name_data = list()
NO_RESULT = ''
Counting = 0
hyper_links = []
courses_count = []
ad_process_details = []
merge_ad_process_details = []
admission_process = ''
eligibility = ''

# Give a batch of colleges
start_point = 1
end_point = 2

# Looping every college
for link in obj:

    # init variables
    Counting = Counting + 1
    D1 = {}
    D2 = {}
    cource_name_data = []
    detailed_data = []
    ad_process_details = []
    merge_ad_process_details = []

    # Start from given college
    if(Counting >= start_point):
        try:
            url_req = str(str(obj[str(link)]) +
                          str('/courses'))
            req = Request(url_req)
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            pages_count = soup.find('span', {'class': 'showResults'}).text
            total_c_int = re.findall(r'\d+', str(pages_count))
            print('Courses = ', total_c_int)
            pass
        except:
            pass
        try:
            for page in range(1, int(int(total_c_int[0])/30)+2):
                print(
                    str(str(obj[str(link)]) + str('/courses' + '?page=' + str(page))))
                url_req = str(str(obj[str(link)]) +
                              str('/courses/' + '?page=' + str(page)))
                req = Request(url_req)
                html_page = urlopen(req)
                soup = BeautifulSoup(html_page, "lxml")
                clg_details_count = 0
                for element_1 in soup.find_all("h2", {"class": "heading4"}):
                    try:
                        get_hyper = element_1

                        # Get course Admission Process and Eligibility Criteria
                        try:
                            clg_details_count += 1
                            get_hyper_link = re.search(
                                r'<a href="(.*?)">', str(get_hyper)).group(1)
                            # hyper_links.append(str('https://www.careers360.com/') + get_hyper_link)
                            html_page_1 = urlopen(
                                Request(str('https://www.careers360.com') + get_hyper_link))
                            # print(get_hyper_link)
                            soup_1 = BeautifulSoup(html_page_1, 'lxml')
                            try:
                                admission_process = soup_1.find(
                                    'div', {'id': 'adProcess'}).text
                            except:
                                pass
                            # print(admission_process)
                            try:
                                eligibility = soup_1.find(
                                    'div', {'id': 'eligibility'}).text
                            except:
                                pass
                            # print(eligibility)
                            ad_process_details.append(
                                {'admission_process': admission_process, 'eligibility': eligibility})
                            print(clg_details_count)
                        except Exception as Msge:
                            print(Msge)
                            pass

                        # Get course name
                        cource_data = str(element_1.text).split('\n')
                        # courses_count.append(cource_data)
                        for i in range(0, len(cource_data)):
                            cource_data[i] = cource_data[i].strip('\t')
                        while('' in cource_data):
                            cource_data.remove('')
                        # print(cource_data)
                        cource_name_data.append(str(''.join(cource_data)))
                    except:
                        print("Throw: No course found")
                        pass
                    finally:
                        pass

                # Get Fee, Seats, Duration and Accepted Exams
                    #D2[question_data[0]] = question_data[1]
                for element in soup.find_all("ul", {"class": "baseUl"}):
                    try:
                        question_data = str(element.text).split('\n')
                        for i in range(0, len(question_data)):
                            question_data[i] = question_data[i].strip('\t')
                        while('' in question_data):
                            question_data.remove('')
                        # print(question_data)
                        if(len(question_data) > 0):
                            for i in range(0, len(question_data)):
                                L = str(question_data[i]).split(':')
                                D2[L[0]] = L[1].strip()
                            detailed_data.append(D2)
                            D2 = {}
                    except:
                        print("Throw: No course data found")
                        pass
                    finally:
                        # print(question_data)
                        # print(D2)
                        pass

            # Merging all the parameters
            for k in range(0, len(ad_process_details)):
                detailed_data[k].update(ad_process_details[k])
            for k in range(0, len(cource_name_data)):
                D1[cource_name_data[k]] = detailed_data[k]
            # Adding

            D3[link] = D1
            # print(cource_name_data)
            # print(detailed_data)
        except:
            print("No course Found..!")
            pass
        finally:
            #D1[str(gallary_title.text)] = D2
            print("Done By ", Counting)
            pass

        # Condition to break a loop
        if(Counting == end_point):
            break

# print(detailed_data)
print(len(hyper_links), len(courses_count))

# Saving a file
# Reading a raw file as a dict object
with open('D:\TestOne\College360\Courses\courses.json', "r") as f:
    data_file = json.load(f)
data_file.update(D3)

json_object = json.dumps(data_file, indent=4)
with open("D:\TestOne\College360\Courses\courses.json", "w") as f:
    json.dump(data_file, f)
