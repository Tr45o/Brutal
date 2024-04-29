import os
import time
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_red(text):
    print("\033[91m {}\033[00m".format(text)) 

def print_green(text):
    print("\033[92m {}\033[00m".format(text)) 
    
def print_orange(text):
    print("\033[93m {}\033[00m".format(text)) 

def generate_random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

clear()
    
tr45o_ascii = """
   ____  ____   __   ___  _____ 
  (_  _)(  _ \ /. | | __)(  _  )
    )(   )   /(_  _)|__ \ )(_)( 
   (__) (_)\_)  (_) (___/(_____)
  Telegram : https://t.me/Tr45o
  GitHub   : https://GitHub.com/Tr45o
"""

tr45o_lines = tr45o_ascii.split('\n')

for line in tr45o_lines:
    print_red(line)
    time.sleep(0.1)

time.sleep(2)
clear() 

tr45o_ascii = """
   ____             _         
  |  _ \           | |        
  | |_) |_ __ _   _| |_ _   _ 
  |  _ <| '__| | | | __| | | |
  | |_) | |  | |_| | |_| |_| |
  |____/|_|   \__,_|\__|\__, |
                        __/ |
                       |___/ 
  Telegram : https://t.me/Tr45o
  GitHub   : https://GitHub.com/Tr45o
"""

tr45o_lines = tr45o_ascii.split('\n')

for line in tr45o_lines:
    print_green(line)
    time.sleep(0.1)
    
    
username = input("\033[93m[**] Instagram Username : ")
print("[**] Fetching details of victim\n[**] https://instagram.com/" + username)
time.sleep(2)
print("[**] Ready to Login")

password_attempts = 10000

random_passwords = []

for _ in range(password_attempts):
    random_password = generate_random_password(random.randint(5, 10))
    random_passwords.append(random_password)

for password in random_passwords:
    time.sleep(2)
    print("[**] Trying to login with password:", password)