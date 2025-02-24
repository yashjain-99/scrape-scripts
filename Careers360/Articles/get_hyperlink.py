from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# https://engineering.careers360.com/articles?page=1 check
# https://www.careers360.com/careers/articles?page=1 check
# https://law.careers360.com/articles?page=1         check
# https://university.careers360.com/articles?page=76 check
# https://medicine.careers360.com/articles?page=99   check
# https://finance.careers360.com/articles?page=29    check
# https://bschool.careers360.com/articles?page=323   check
# https://design.careers360.com/articles?page=44     check
# https://www.careers360.com/careers/articles?page=1 check
# https://www.careers360.com/articles?page=2
# pages length
pages_length = 2  # last page number for latest news
hyper_link = 'https://www.careers360.com/articles?page='

# Init all variables
D1 = dict()
D2 = dict()
D3 = dict()

# Give a batch of colleges
start_point = 1
end_point = pages_length

Counting = 0
# Looping every college
for link_count in range(1, pages_length, 1):

    # init variables
    Counting = Counting + 1
    #D1 = {}
    D2 = {}

    # Start from given college
    if(Counting >= start_point):
        try:
            url_req = str(str(hyper_link) + str(link_count))
            req = Request(url_req)
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            for article in soup.find_all('div', {'class': 'artiTitle headingContainer'}):
                #D1 = {}
                # print(article.find('a')['href'])
                # print(article.find('a').text)
                #print(article.find('div', {'class': 'arti-Bottom'}).text)
                article_text = str(article.find(
                    'a').text).replace('\n', '').strip()
                article_hyperlink = str(
                    str('') + str(article.find('a')['href']))
                D1[article_text] = str(
                    str('https://www.careers360.com') + article_hyperlink)
                # print(posted_by, date_posted)
                #D2[article_text] = D1
        except Exception as msg:
            print(msg)
            pass

        finally:
            print("Done By ", Counting)
            pass

        #D3[link_count] = D2

        # Condition to break a loop
        if(Counting == end_point):
            break

# print(D3)
# Saving a file
# Reading a raw file as a dict object
with open('D:\\TestOne\\College360\\Articles\\art_url.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)

json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\Articles\\art_url.json", "w") as f:
    json.dump(data_file, f)
