from rutte import data
import requests,time,json

data = data[-6]
print(data)
number = "7828278203"

# for i in data:
#   i[-1]= {k:("+91"+ number if str(v).startswith('+91') else '91'+number if  str(v).startswith('91') else number if v=='7828278203' else v) for k,v in i[-1].items()}
#   r = requests.post(i[0]['url'], headers=i[1],data=json.dumps(i[2], separators=(',', ':')), verify=False)
#   # print(r.text)
#   time.sleep(2.5)
#   print()

# print()
# data[-2]= {k:("+91"+ number if str(v).startswith('+91') else '91'+number if  str(v).startswith('91') else number if v=='7828278203' else v) for k,v in data[-2].items()}
r = requests.post(data[0]['url'], headers=data[1],data=json.dumps(data[2], separators=(',', ':')), verify=False)
print(r.text)
time.sleep(2.5)
print()
