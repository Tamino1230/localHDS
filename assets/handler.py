
# import Local
from assets.domain import show

#- Checks for spezific returns Handels
def handler(value, function):
    match value:
        case 0: #- No Error Accured
            return
        case -1: #- General Error
            print(f"Handler: An Error accured in \"{function.__name__}\"")
        case -2: #- If User didnt start the program with Administrator
            print(f"Handler: Permission denied. Run the script as an Administrator! Because of \"{function.__name__}\"")
            show("Permission denied!", "Run the script as an Administrator!", "error")
            exit()
        case -3:
            print("Handler: File not found.")
            show("Not Found", "The inputed file was not Found", "warn")
        case -4:
            print("Handler: Blacklisted URL.")
            show("Blacklisted", "You inputed a Blacklisted URL!", "warn")
        case _: #- Other cases /  errorcodes
            if isinstance(value, str): #- If value is a String it returns
                return
            elif isinstance(value, int): #- If its an Unknown Errorcode 
                print(f"Handler: Unknown Error Accured Errorcode: \"{value}\"! Because of \"{function.__name__}\"")
                show("Unknown Error", f"An Unknown Error Accured")
                return
            return