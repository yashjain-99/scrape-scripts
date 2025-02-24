import json
with open('D:\\TestOne\\College360\\HyperLinks\\all_hyperlinks(replicates).json', 'r') as read_my_json:
    data_json = read_my_json.read()
obj = json.loads(data_json)
# Remove duplicate values in dictionary
# Using dictionary comprehension
temp = {val: key for key, val in obj.items()}
res = {val: key for key, val in temp.items()}

json_object = json.dumps(res, indent=4)
with open('D:\\TestOne\\College360\\HyperLinks\\final_unique.json', "a") as f:
    f.write(json_object)
