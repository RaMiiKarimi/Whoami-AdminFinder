import requests
from colorama import Fore
from time import sleep
import sys



Green = Fore.GREEN
Red = Fore.RED
White = Fore.LIGHTWHITE_EX
Cyan = Fore.CYAN

Banner = White + "𝐖𝐡𝐢𝐭𝐞𝐑𝐨𝐬𝐞 /" , Cyan + "𝐑𝐚𝐌𝐢𝐢 𝐊𝐚𝐫𝐢𝐦𝐢"

for mybanner in Banner:
    print(mybanner , end='')
    sys.stdout.flush()
    sleep(0.1)
print('')

url = input("Type Your URL :")
print("Whitout Slash /")
admin_panel_names = []


with open('adminpanel.txt') as panels:
    lines = panels.readlines()
    for line in lines:
        admin_panel_names.append(line.strip())

for name in admin_panel_names:
    admin_url = f'{url}/{name}'
    response = requests.get(admin_url)
    if response.status_code == 404:
        print(Red + "Not Found")
    if response.status_code == 200:
        print(Green + "Admin Panel Found: " + admin_url)



