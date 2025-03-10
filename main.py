
#- Local Host-Domain-Switch Program

# import Online
import time
import os
from colorama import Fore

# import Local
from assets.inputer import safe_input, menue, user_add_url_path, user_remove_url_path, show_all_sites
from assets.handler import handler
from assets.domain import addDomain, removeDomain, get_paste, show, list_domains, change_local_domain
from assets.logs import save_log_file, add_log, show_log_history
from assets.generate import generate

# var Config
HOST_PATH = "C:\\Windows\\System32\\drivers\\etc\\hosts"
IP = "127.0.0.1"
DOMAIN = "example.net"
TIME = 0.8
PROGRAM_NAME = ['''
    __                     __   __  ______  _____
   / /   ____  _________ _/ /  / / / / __ \\/ ___/
  / /   / __ \\/ ___/ __ `/ /  / /_/ / / / /\\__ \\ 
 / /___/ /_/ / /__/ /_/ / /  / __  / /_/ /___/ / 
/_____/\\____/\\___/\\__,_/_/  /_/ /_/_____//____/  by Tamino1230                                         
''']


#- main function
def main(HOST_PATH, IP, DOMAIN, PROGRAM_NAME):
    logs = []
    esl = ["/", "/page"]
    
    # print(esl)
    # handler(user_add_url_path(esl), user_add_url_path)
    # print(esl)
    # handler(user_add_url_path(esl), user_add_url_path)
    # print(esl)
    # handler(user_add_url_path(esl), user_add_url_path)
    # print(esl)
    print()
    print(f"{PROGRAM_NAME[0]}")
    LAST_GEN = ""
    while True:
        print(f"\nCurrent:\nDomain: {DOMAIN}\nIP: {IP}\nHost Path: {HOST_PATH}\n")
        value = menue()
        # print(type(value))
        match value:
            case "1":
                os.system('cls')
                old_domain = DOMAIN
                new_domain = change_local_domain(DOMAIN)
                new_domain = str(new_domain)
                DOMAIN = new_domain
                add_log(logs, "Domain Changed", f"From {old_domain} to {new_domain}")
                print(f"Successfully changed Domain from {old_domain} to {new_domain}")
                print("\n")
            case "2":
                os.system('cls')
                code = handler(addDomain(HOST_PATH, IP, DOMAIN), addDomain)
                add_log(logs, "Added Domain", f"{IP} {DOMAIN}")
                if code == 0:
                    print(f"Successfully added Domain: {DOMAIN} with IP: {IP}")
                elif code == -4:
                    print(f"Something went wrong while adding the Domain: {DOMAIN} and IP: {IP}")
                else:
                    print(f"Successfully added Domain: {DOMAIN} with IP: {IP}")
                print("\n")
            case "3":
                os.system('cls')
                code = handler(removeDomain(HOST_PATH, IP, DOMAIN), removeDomain)
                add_log(logs, "Removed Domain", f"{IP} {DOMAIN}")
                if code == 0:
                    print(f"Suceesfully removed Domain: {DOMAIN} with IP: {IP}")
                elif code == -4:
                    print(f"Something went wrong while removing the Domain: {DOMAIN} and IP: {IP}")
                else:
                    print(f"Suceesfully removed Domain: {DOMAIN} with IP: {IP}")
                print("\n")
            case "4":
                os.system('cls')
                handler(list_domains(HOST_PATH), list_domains)
                add_log(logs, "Showed", "Active Local Domains")
                print("\n")
            case "5":
                os.system('cls')
                add_log(logs, "Showed", "Log History")
                show_log_history(logs)
                print("\n")
            case "6":
                os.system('cls')
                add_log(logs, "Saved", "Log History")
                save_log_file(logs, f"assets\\saves\\history_log_saved_{time.time()}.txt")
                print("Saved Log File!")
                print("\n")
            case "7":
                os.system('cls')
                user_add_url_path(esl)
                add_log(logs, "HTML", "Added a new Page")
                print("Succesfully added new Site or cancelt!")
            case "8":
                os.system('cls')
                user_remove_url_path(esl)
                add_log(logs, "HTML", "Removed a Page")
                print("Succesfully removed the Site or cancelt!")
            case "9":
                os.system('cls')
                show_all_sites(esl)
                add_log(logs, "HTML", "Show all Pages")
            case "10":
                os.system('cls')
                if esl == []:
                    print("You dont have enough Path URLS to make a Server!!\n")
                else:
                    server_file_name = f"server_{time.time()}.py"
                    generate(server_file_name, esl)
                    print(f"Successfully Generated Server File!: {server_file_name}")
                    print("Starting Server File..")
                    try:
                        print("Trying to start server with Domains and Path URL's: ")
                        show_all_sites(esl)
                        handler(list_domains(HOST_PATH), list_domains)
                        print(f"Successfully started {server_file_name} File.")
                        os.system(f"python {server_file_name}")
                    except:
                        print(f"An error accured while starting: {server_file_name}. Or Server got closed")
                    finally:
                        LAST_GEN = f"{server_file_name}"
                        add_log(logs, "Server", f"Generated Server: {server_file_name}")
            case "11":
                print("Trying to start last server with Domains and Path URL's: ")
                show_all_sites(esl)
                handler(list_domains(HOST_PATH), list_domains)
                print("")
                if LAST_GEN == "":
                    print("You have not Started a Server before!")
                    continue
                try:
                    os.system(f"python {LAST_GEN}")
                except:
                    print(f"An error accured in {LAST_GEN} or Server got close!d")
                finally:
                    add_log(logs, "Server", f"Started the last used Server: {LAST_GEN}")
            case _:
                print("idk")
                add_log(logs, "idk", "uwu")
        time.sleep(TIME)

if __name__ == "__main__":
    main(HOST_PATH, IP, DOMAIN, PROGRAM_NAME)
