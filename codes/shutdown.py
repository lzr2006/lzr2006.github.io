import os
from time import sleep
for i in range(1,100000000000):
    os.system("shutdown -s -t 30")
    sleep(1.5)
    os.system("shutdown -a")
    sleep(1.5)
