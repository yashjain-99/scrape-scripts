# parsing to data schema's

import json
# load faq json
with open("College360\\faq\FAQ\\faq_final.json", "r", encoding="utf-8") as f:
    obj = json.loads(f.read())

D3 = []
D2 = dict()

# counter var
c = 0

for clg_id in obj.keys():
    c += 1
    if(len(obj[clg_id]) != 0):
        for question in obj[clg_id].keys():
            D2 = dict()
            D2.update({"college_id": int(clg_id)})
            D2.update({"question": question})
            D2.update({"answer": obj[clg_id][question]})
            D3.append(D2)
    else:
        D2 = dict()
        D2 = {
            "college_id": int(clg_id),
            "question": "",
            "answer": ""
        }
        D3.append(D2)
    if(c == 50):
        break

# print(D3)

with open('College360\\faq\\parsed_faq[50].json', "r") as f:
    data_file = json.load(f)
data_file.extend(D3)
json_object = json.dumps(data_file, indent=4)

# Writing new dict objects
with open('College360\\faq\\parsed_faq[50].json', "w") as f:
    json.dump(data_file, f)
