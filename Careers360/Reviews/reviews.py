from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# Load json
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# Variables
D1 = dict()
D2 = dict()
D3 = dict()
L1 = []
RD1 = list()
RD2 = dict()
posted = list()
title_list = list()
Counting = 0

# Looping
start_point = 1478
end_point = 1478
for link in obj:

    # Initialization
    Counting = Counting + 1
    D1 = {}
    title_list = []
    posted = []
    RD1 = []

    if(Counting >= start_point):
        try:
            # reviews?page=2
            # Find number of pages
            try:
                req = Request(str(obj[str(link)]) + '/reviews')
                html_page = urlopen(req)
                soup = BeautifulSoup(html_page, "lxml")
                total_c = soup.find('span', {'class': 'reviewTot'}).text
                total_c_int = re.findall(r'\d+', str(total_c))
                print('Reviews = ', total_c_int,
                      'Pages = ', int(total_c_int[0])/30)
            except:
                pass
            page_c = 0
            for i in range(1, int(int(total_c_int[0])/30)+2):
                page_c = page_c + 1
                #req = Request(str(obj[str(link)]) + '/reviews?page=' + str(i))
                html_page = urlopen(req)
                soup = BeautifulSoup(html_page, "lxml")

                # Heading title
                for title_text in soup.find_all("h4", {"class": "blockHeading"}):
                    title_list.append(title_text.text)
                # print(title_list)

                # posted Date
                for posted_on in soup.find_all('div', {'class': 'stName'}):
                    # Posted on 01 Mar' 22
                    try:
                        posted_edit = str(posted_on)
                        if(posted_edit.find('Posted on') != -1):
                            post_pre = posted_edit.find('Posted on')
                            post_suf = posted_edit.find('</span>')
                            posted.append(posted_edit[post_pre+9:post_suf])
                    except Exception as msgt:
                        print(msgt)
                        pass

                #Feature and description
                i_title = 0
                for card_items in soup.find_all('div', {'class': 'ratingOuter'}):
                    card_item = str(card_items.text).split('\n')
                    card_item.remove('')
                    while("" in card_item):
                        card_item.remove("")
                    while("\t\t\t\t\t\t\t\t\t\t\t\t\t" in card_item):
                        card_item.remove("\t\t\t\t\t\t\t\t\t\t\t\t\t")
                    '''while("Infrastructure" in card_item):
                        card_item.remove("Infrastructure")'''
                    card_item.pop()
                    card_item.pop()
                    card_item.pop()
                    card_item.pop()
                    card_item.pop()
                    D1[title_list[i_title]] = {'description': card_item}
                    i_title = i_title + 1
                    # print(D1)
                    # Rating
                    try:
                        cnt = 0
                        RD2 = {}
                        for card_rating in card_items.find_all('div', {'class': 'userRating'}):
                            # print(card_rating)
                            cnt = cnt + 1
                            temp = re.findall(r'\d+', str(card_rating))
                            # print(temp)
                            res = list(map(int, temp))
                            if(cnt == 1):
                                RD2['Infrastructure'] = res[0]
                            if(cnt == 2):
                                RD2['Placements'] = res[0]
                            if(cnt == 3):
                                RD2['Academics'] = res[0]
                            if(cnt == 4):
                                RD2['Value for Money'] = res[0]
                            if(cnt == 5):
                                RD2['Campus Life'] = res[0]
                                cnt = 0
                                RD1.append(RD2)
                                RD2 = {}

                    except Exception as msg:
                        print(msg)
                        pass
                print("Page ", page_c)
        except:
            print("No reviews Found")
            pass
        finally:
            print('Done by ', Counting)
            '''D1[str(gallary_title.text)] = D2
            print("Done By ", Counting)'''
            pass
        # Adding Dict values section
        # print(len(title_list), len(posted), len(RD1), len(D2))
        print(len(D1), len(RD1))
        # print(RD1)
        for k, l in zip(D1, range(0, len(RD1))):
            D1[k].update(RD1[l])
        for k, l in zip(D1, range(0, len(posted))):
            D1[k].update({'date_posted': str(posted[l]).strip()})
        D3[link] = D1
    if(Counting == end_point):
        break
# print(D3)

# Writing into a file
with open('D:\\TestOne\\College360\\Reviews\\reviews.json', "r") as f:
    data_file = json.load(f)
data_file.update(D3)
json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\Reviews\\reviews.json", "w") as f:
    json.dump(data_file, f)
