import csv
import json

# opening a file
with open('D:\\TestOne\\College360\\Articles\\articles_data.json', 'r', encoding="utf-8") as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)


with open("D:\\TestOne\\College360\\Articles\\temp.tsv", "w", encoding="utf-8") as f:
    # c = 0
    f.write('article_title\tposted_by\tdate_posted\thyperlink\n')
    for k in obj.keys():
        f.write(
            f'{obj[k]["article_title"]}\t \
                {obj[k]["posted_by"]}\t \
                {obj[k]["date_posted"]}\t \
                {obj[k]["hyperlink"]}\n')

    # c = c + 1
    # if(c == 1):
    #     break
