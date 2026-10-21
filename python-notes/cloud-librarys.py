import os
#print(os.system("df -h")) #linux or mac
#print(os.system('systeminfo'))
# print(os.system('sysinfo'))
# print(os.system('date'))

def check(command):
    print(os.system(command))
check("systeminfo")
check("free -m")
check("date")