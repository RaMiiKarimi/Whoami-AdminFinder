import requests
from colorama import Fore
from time import sleep
import sys



Green = Fore.GREEN
Red = Fore.RED
White = Fore.LIGHTWHITE_EX
Cyan = Fore.CYAN

Banner = Cyan + "𝐖𝐡𝐢𝐭𝐞𝐑𝐨𝐬𝐞 / 𝐑𝐚𝐌𝐢𝐢 𝐊𝐚𝐫𝐢𝐦𝐢"

for mybanner in Banner:
    print(mybanner , end='')
    sys.stdout.flush()
    sleep(0.1)
print('')

print("𝗣𝗮𝘀𝘁𝗲 𝗟𝗶𝗻𝗸 𝗪𝗶𝘁𝗵𝗼𝘂𝘁 𝗦𝗹𝗮𝘀𝗵")

url = input("Type Your URL :")
admin_panel_names = [] 






with open('adminpanel.txt') as panels:
    lines = panels.readlines()
    for line in lines:
        admin_panel_names.append(line.strip())


for name in admin_panel_names:
    admin_url = f'{url}/{name}'
    response = requests.get(admin_url)
    if response.status_code == 200:
        print(Green + "𝗔𝗱𝗺𝗶𝗻 𝗣𝗮𝗻𝗲𝗹 𝗙𝗼𝘂𝗻𝗱: " + admin_url)
    if response.status_code == 401:
        print(Red +"𝗬𝗼𝘂𝗿 𝗜𝗣 𝗠𝗮𝘆 𝗕𝗲 𝗕𝗹𝗼𝗰𝗸𝗲𝗱")
    if response.status_code == 429:
        print(Red +"𝗬𝗼𝘂𝗿 𝗜𝗣 𝗠𝗮𝘆 𝗕𝗲 𝗕𝗹𝗼𝗰𝗸𝗲𝗱")



