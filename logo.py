#!/usr/bin/env python3
import os
import time
import random

# === COLORS ===
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
M = "\033[95m"
C = "\033[96m"
W = "\033[0m"
BOLD = "\033[1m"
P = "\033[35m"

# === FULL FILLED BOLD LOGO ===
SMS_BOMBER_ASCII = f"""
{BOLD}{Y}███████ ███    ███ ███████     ██████   ██████  ███    ███ ██████  ███████ ██████  
██      ████  ████ ██          ██   ██ ██    ██ ████  ████ ██   ██ ██      ██   ██ 
███████ ██ ████ ██ ███████     ██████  ██    ██ ██ ████ ██ ██████  █████   ██████  
     ██ ██  ██  ██      ██     ██   ██ ██    ██ ██  ██  ██ ██   ██ ██      ██   ██ 
███████ ██      ██ ███████     ██████   ██████  ██      ██ ██████  ███████ ██   ██ {W}
                                                                                                                                                                                                                                                                                       
"""

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print(SMS_BOMBER_ASCII)
    print(f"{Y}{'═' * 70}{W}")
    print(f"{Y}                ⚡ Author: HACKER_X | Mode: ULTRA FLOOD ⚡{W}")
    print(f"{Y}{'═' * 70}{W}\n")


def attack():
    try:    
        for i in range(1, 20):
            for j in range(1,20):
                if j == 19:
                    os.system('cls')
                    print(f"{R}[{Y}Attacking 🧨{R}]:"," " * j + "[💥]")
                    print()
                    print(f"{Y}Press 'Ctrl+C' to quit.")
                    time.sleep(1)
                else:
                    os.system('cls')
                    print(f"{R}[{Y}Attacking 🧨{R}]:"," " * j + "[💣]")
                    print()
                    print(f"{Y}Press 'Ctrl+C' to quit.")
                    time.sleep(0.1)
    except KeyboardInterrupt:
        os.system("cls")
        print(f'{P}Toot Exit! Thanks for Using.')
attack()
    
