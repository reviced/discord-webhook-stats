import requests
import colorama
import asyncio
import time
import threading
import os
import ctypes
from colorama import Fore, Style
from threading import Thread
from sys import stdout
from requests import Session
from time import strftime, gmtime

sent = 0
session = Session()
b = Style.BRIGHT
os = os.system
os('cls')



print(f"""

{b+Fore.GREEN}


██████╗ ███████╗██╗   ██╗██╗ ██████╗███████╗██████╗ 
██╔══██╗██╔════╝██║   ██║██║██╔════╝██╔════╝██╔══██╗
██████╔╝█████╗  ██║   ██║██║██║     █████╗  ██║  ██║
██╔══██╗██╔══╝  ╚██╗ ██╔╝██║██║     ██╔══╝  ██║  ██║
██║  ██║███████╗ ╚████╔╝ ██║╚██████╗███████╗██████╔╝
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝ ╚═════╝╚══════╝╚═════╝ 

                                                             
{b+Fore.BLUE} > {Fore.RESET}Webhook Stats 
{b+Fore.BLUE} > {Fore.RESET}Creator: isaiah#6969
""")

print(f"[{Fore.GREEN}>{Fore.RESET}] Webhook link ")
webhook = input("#root~reviced~ ")
r = requests.get(webhook).json()
print(f"""

{b+Fore.GREEN}
 
    Webhook Name  : {r["name"]}
    Webhook Token : {r["token"]}
    Webhook ID    : {r["token"]}
    Guild ID      : {r["guild_id"]}
    Channel ID    : {r["channel_id"]}')
""")
