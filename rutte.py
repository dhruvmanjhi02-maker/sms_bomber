import json,os
data = []
for i in [x for x in os.listdir() if x[-4:]=="json"]:
    with open(i, "r") as file:
        data.append(json.load(file))




