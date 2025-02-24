from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json


# https://news.careers360.com/college-university
# pages length

pages_length = 419  # last page number for latest news
hyper_link = 'http://news.careers360.com/college-university?page='

# Init all variables
D1 = dict()
D2 = dict()
D3 = dict()

# Give a batch of colleges
start_point = 1
end_point = 419

Counting = 0
# Looping every college
for link_count in range(pages_length, 0, -1):

    # init variables
    Counting = Counting + 1
    D1 = {}
    D2 = {}

    # Start from given college
    if(Counting >= start_point):
        try:
            url_req = str(str(hyper_link) +
                          str(link_count))
            req = Request(url_req)
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            for article in soup.find_all('div', {'class': 'display-cell rightBlk'}):
                D1 = {}
                article_text = str(article.find(
                    'a').text).replace('\n', '').strip()
                article_hyperlink = str(
                    str('https://news.careers360.com') + str(article.find('a')['href']))
                posted_by, date_posted = str(article.find(
                    'div', {'class': 'arti-Bottom'}).text).split('|')
                posted_by = str(posted_by).replace('\n', '').strip()
                date_posted = str(date_posted).replace('\n', '').strip()
                breadcrumb = 'Home >> College >> ' + article_text
                D1 = {
                    'article_title': article_text,
                    'article_hyperlink': article_hyperlink,
                    'posted_by': posted_by,
                    'date_posted': date_posted,
                    'breadcrumb': breadcrumb
                }
                # print(posted_by, date_posted)
                D2[article_text] = D1
        except Exception as msg:
            print(msg)
            pass

        finally:
            print("Done By ", Counting)
            pass

        D3[link_count] = D2

        # Condition to break a loop
        if(Counting == end_point):
            break

# print(D3)
# Saving a file
# Reading a raw file as a dict object
with open('D:\\TestOne\\College360\\News\\college_news.json', "r") as f:
    data_file = json.load(f)
data_file.update(D3)

json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\News\\college_news.json", "w") as f:
    json.dump(data_file, f)
