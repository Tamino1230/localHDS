
#- Local Host-Domain-Switch Program

# import Online
import time
import os

# import Local
from assets.inputer import safe_input, menue
from assets.handler import handler
from assets.domain import addDomain, removeDomain, get_paste, show, list_domains, change_local_domain

# var Config
HOST_PATH = "C:\\Windows\\System32\\drivers\\etc\\hosts"
IP = "127.0.0.1"
DOMAIN = "example.net"
TIME = 2

PROGRAM_NAME = ['''
    __                     __   __  ______  _____
   / /   ____  _________ _/ /  / / / / __ \\/ ___/
  / /   / __ \\/ ___/ __ `/ /  / /_/ / / / /\\__ \\ 
 / /___/ /_/ / /__/ /_/ / /  / __  / /_/ /___/ / 
/_____/\\____/\\___/\\__,_/_/  /_/ /_/_____//____/  by Tamino1230
                                                 
''']


#- main function
def main(HOST_PATH, IP, DOMAIN):
    for name in PROGRAM_NAME:
        print(name)
    while True:
        value = menue()
        print(type(value))
        match value:
            case "1":
                new_domain = change_local_domain(DOMAIN)
                print(DOMAIN)
                DOMAIN = new_domain
                print(DOMAIN)
            case "2":
                handler(addDomain(HOST_PATH, IP, DOMAIN), addDomain)
            case "3":
                handler(removeDomain(HOST_PATH, IP, DOMAIN), removeDomain)
            case "4":
                handler(list_domains(HOST_PATH), list_domains)
            case "5":
                print("Function 5")
            case _:
                print("idk")
        time.sleep(TIME)
        os.system('cls')

if __name__ == "__main__":
    main(HOST_PATH, IP, DOMAIN)