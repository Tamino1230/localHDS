
def safe_input(msg: str = "default", data_type = str):
    while True:
        try:
            user_input = ""
            message = ""
            user_input = input(msg)
            value = data_type(user_input)
            return value #- Only returns if worked
        except: #- Errormessage
            if data_type == int:
                message = "integers"
            elif data_type == float:
                message = "integers and decimal numbers"
            else:
                message = "words"
            print(f"You cannot Input \"{user_input}\" only {message}.")
            continue #- Only allowed inputs

def menue(): #- Menu to print
    avbl = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    print()
    print("| LocalHDS Build")
    print("1) Change Local Domain URL")
    print("2) Add Local Domain overwrite")
    print("3) Remove Local Domain overwrite")
    print("4) List Local Domains")
    print()
    print("| Log Build")
    print("5) Show Log History")
    print("6) Save Log History")
    print()
    print("| Website Build")
    print("7) New Page")
    print("8) Remove Page")
    print("9) Show all Pages")
    print("10) Generate File")
    print("11) Start Last Generated File")

    while True:
        choice = safe_input(f"Enter you choice ({avbl[0]}-{avbl[-1]}): ")
        if not choice in avbl:
            print(f"You can only input ({avbl[0]}-{avbl[-1]}) and not \"{choice}\"")
            continue
        else:
            return choice

def show_all_sites(existing_sites_list: list):
    print()
    print("All Sites:")
    for idx, site in enumerate(existing_sites_list):
        print(f"{idx+1}. {site}")
    print()

def user_add_url_path(existing_sites_list: list):
    while True:
        url_path = safe_input("Add a new url Path <leave it empty for homepage> (cancel): ")
        url_path = "/" + url_path
        if url_path in existing_sites_list:
            print("This site is already used! Choose another one!")
            continue
        if " " in url_path or "." in url_path:
            print("You cannot use \" \" or \".\" !")
        elif url_path.lower() == "/cancel":
            return 0
        existing_sites_list.append(url_path)
        return 0

def user_remove_url_path(existing_sites_list: list):
    show_all_sites(existing_sites_list)
    while True:
        url_path = safe_input("Which site do you want to remove? <leave it empty for homepage> (cancel): ")
        url_path = "/" + url_path
        if not url_path in existing_sites_list:
            print("This site is not in use!")
            continue
        elif url_path.lower() == "/cancel":
            return 0
        existing_sites_list.remove(url_path)
        return 0
