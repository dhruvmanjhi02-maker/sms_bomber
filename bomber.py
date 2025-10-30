from data_cs import data
import requests,time,json,warnings
from logo import banner, attack
import threading

warnings.filterwarnings("ignore")

banner()


def bomber():
    for i in data:
        # r = requests.post(i[0]['url'], headers=i[1],data=json.dumps(i[2], separators=(',', ':')), verify=False)
        # print(r.status_code)
        # time.sleep(2.5)
        print()

t1 = threading.Thread(target=attack)
t2 = threading.Thread(target=bomber)

t1.start()
t2.start()

t1.join()
t2.join()


