# career counselling https://www.careers360.com/premium/keyword/career-counselling?page=5&ici=premium-home&icn=premium-category-listing_career-counselling
# study help https://www.careers360.com/premium/keyword/study-help?page=5&ici=premium-home&icn=premium-category-listing_study-help
# exam prep https://www.careers360.com/premium/keyword/exam-prep?page=5&ici=premium-home&icn=premium-category-listing_exam-prep
# Parenting https://www.careers360.com/premium/keyword/parenting?page=2&ici=premium-home&icn=premium-category-listing_parenting
# Career insights https://www.careers360.com/premium/keyword/career-insights?page=5&ici=premium-home&icn=premium-category-listing_career-insights
# Mental Health https://www.careers360.com/premium/keyword/mental-health?page=5&ici=premium-home&icn=premium-category-listing_mental-health
# scholarships https://www.careers360.com/premium/keyword/fees-scholarships?page=4&ici=premium-home&icn=premium-category-listing_fees-scholarships
# Jobs https://www.careers360.com/premium/keyword/jobs-internships?page=3&ici=premium-home&icn=premium-category-listing_jobs-internships
# Stuy Abroad https://www.careers360.com/premium/keyword/study-abroad?page=2&ici=premium-home&icn=premium-category-listing_study-abroad
# Sports https://www.careers360.com/premium/keyword/sports-activities?page=2&ici=premium-home&icn=premium-category-listing_sports-activities
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re
import json

# pages length
pages_length = 5  # last page number for latest news
hyper_link = 'https://www.careers360.com/premium/keyword/sports-activities?page='

# Init all variables
D1 = dict()
D2 = dict()
D3 = dict()

# Give a batch of colleges
start_point = 1
end_point = 5

Counting = 0

# Looping every college
for link_count in range(pages_length, 0, -1):

    # init variables
    Counting = Counting + 1
    #D1 = {}
    D2 = {}

    # Start from given college
    if(Counting >= start_point):
        try:
            url_req = str(str(hyper_link) +
                          str(link_count) + str('&ici=premium-home&icn=premium-category-listing_sports-activities'))
            req = Request(url_req)
            html_page = urlopen(req)
            soup = BeautifulSoup(html_page, "lxml")
            for article in soup.find_all('h3', {'class': 'Premium_popular_stories_start_card_sub_heading__X1kMV'}):
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
with open('D:\\TestOne\\College360\\premium\\sports.json', "r") as f:
    data_file = json.load(f)
data_file.update(D1)

json_object = json.dumps(data_file, indent=4)
with open("D:\\TestOne\\College360\\premium\\sports.json", "w") as f:
    json.dump(data_file, f)
