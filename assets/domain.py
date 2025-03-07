
# import Online
import tkinter as tk
from tkinter import messagebox
import requests

# import Local
from assets.inputer import safe_input

#- Gets the raw content from a Website
def get_paste(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        content = response.text
        return content
    except requests.exceptions.RequestException as e:
        return -1

#- Shows a WindowsMessagebox
def show(info="default_info", text="default_text", show="info"):
    show = show.lower()
    modes = ["info", "error", "warn"]
    if not show in modes:
        print(f"Send out Popup for \"Wrong Argument: info\"")
    else:
        print(f"Send out Popup for \"{show}\"")
    if show == modes[0]:
        messagebox.showinfo(info, text)
    elif show == modes[1]:
        messagebox.showerror(info, text)
    elif show == modes[2]:
        messagebox.showwarning(info, text)
    else:
        messagebox.showinfo(info, text)

#- Removes a domain
def removeDomain(filepath, ip_address, forward_domain):
    try:
        with open(filepath, "r") as file:
            lines = file.readlines()
        
        target = f"{ip_address} {forward_domain.strip()}"
        new_lines = [line for line in lines if target not in line.strip()]
        
        with open(filepath, "w") as file:
            file.writelines(new_lines)
        return 0
    except PermissionError:
        print("Permission denied. Run the script as an administrator.")
        return -2
    except Exception as e:
        print(f"An unknown error occurred: {e}")
        return 1

#- Adds a domain
def addDomain(filepath, ip_address, forward_domain):
    try:
        with open(filepath, 'a') as file:
            file.write(f"{ip_address} {forward_domain}\n")
        print(f"{forward_domain} added.")
        return 0
    except PermissionError:
        print("Permission denied. Run the script as an administrator.")
        return -2
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
    
def list_domains(filepath):
    try:
        new = []
        with open(filepath, "r") as file:
            data = file.readlines()
        for line in data:
            line = line.strip()  
            if line and not line.startswith("#"):
                # print("found line", line)
                new.append(line)
            else:
                 #print(f"Ignored line: {line}")
                 pass
        if not new: 
            print("No Local IP's and Domains were found!")
        else:
            print("Local IP and Domains:")
            for count, domain in enumerate(new, start=1):
                print(f"{count}.) {domain}")
        return 0
    except FileNotFoundError:
        print(f"File not found. \"{filepath}\".")
        return -3
    except PermissionError:
        print("Permission denied. Run the script as an administrator.")
        return -2
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

def change_local_domain(old_domain):
    blacklisted = ["discord.com"]
    while True:
        value = safe_input("Input new Domain <example.net> (cancel): ")
        if value in blacklisted:
            return -4
        elif value.lower() == "cancel":
            print("Canceling")
            value = old_domain
        elif not "." in value or " " in value:
            print("This is not a real Domain! <example.net>")
            continue
        return value.lower()
