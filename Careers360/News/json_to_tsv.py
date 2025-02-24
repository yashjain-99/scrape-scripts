import csv
import json

# it will generate an excel file

# opening a file
with open('D:\\TestOne\\College360\\News\\latest_news_1.json', 'r', encoding="utf-8") as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)

# writing excel file
with open("D:\\TestOne\\College360\\News\\latest_news_tsv_1.tsv", "w", encoding="utf-8") as f:
    # c = 0
    f.write('article_title	article_hyperlink	posted_by	date_posted	breadcrumb\n')
    for k, v in obj.items():
        for k1, v1 in obj[k].items():
            f.write(
                f'{obj[k][k1]["article_title"]}\t{obj[k][k1]["article_hyperlink"]}\t{obj[k][k1]["posted_by"]}\t{obj[k][k1]["date_posted"]}\t{obj[k][k1]["breadcrumb"]}')
            f.write('\n')
        # c = c + 1
        # if(c == 1):
        #     break
