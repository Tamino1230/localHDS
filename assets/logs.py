
def add_log(liste: list, reason="default mode", msg="default reason"):
    liste.append(f"[{reason.upper()}] {msg};\n")

def save_log_file(liste: list, file_name=""):
    if liste == []:
        print("You dont have any Logs yet!")
    else:
        with open(file_name, "a+") as file:
            for line in liste:
                file.write(line)

def show_log_history(liste: list):
    count = 1
    if liste == []:
        print("You dont have any Logs yet!")
    for line in liste:
        print(f"{count}: {line}")
        count += 1
