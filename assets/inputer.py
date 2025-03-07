
def safe_input(msg: str = "default", data_type = str):
    while True:
        try:
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
    avbl = ["1", "2", "3", "4", "5", "6"]
    print("1) Change Local Domain URL")
    print("2) Add Local Domain overwrite")
    print("3) Remove Local Domain overwrite")
    print("4) List Local Domains")
    print("5) Log History")
    print("6) Save Log History")

    while True:
        choice = safe_input(f"Enter you choice ({avbl[0]}-{avbl[-1]}): ")
        if not choice in avbl:
            print(f"You can only input ({avbl[0]}-{avbl[-1]}) and not \"{choice}\"")
            continue
        else:
            return choice