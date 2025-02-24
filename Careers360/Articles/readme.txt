Articles Blog

get_hyperlinks.py ( get all the hyperlinks of blog )

Input : 2 inputs: (pages, url)

pages_length = 2  # last page number for latest news
hyper_link = 'https://www.careers360.com/articles?page='

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

it will create urls "url.json" json file which contains all the urls of blog

get_articles.py ( scrapes the data )

parameters

article_title
posted_by
date_posted
hyperlink

Input : give extracted "url.json" as input

Output :it will generate articles_data.json 

all the json files
🔗 https://drive.google.com/drive/folders/1NHLUjtT5Bi8H3cCckB-x4rOuve5Nu_hp?usp=sharing
Extracted Excel file

🔗 https://docs.google.com/spreadsheets/d/1pKk-XRrNYNIzE5IsbNXnRH1hs1gOEECG/edit?usp=sharing&ouid=110284172906022819450&rtpof=true&sd=true
