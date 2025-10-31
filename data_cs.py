import json,os
data = []
for i in [x for x in os.listdir('bombers') if x[-4:]=="json"]:
    with open(f"bombers/{i}", "r") as file:
        data.append(json.load(file))
