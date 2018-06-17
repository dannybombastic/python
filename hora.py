import datetime
import time
import os

i = 0
while True:
    

    os.system("cls")
    dt = datetime.datetime.now()
    print("{}:{}:{}".format(dt.hour,dt.minute,dt.second))

    time.sleep(1)
    if i == 50 :
        print(i)
        break
    else:
        i += i + 1