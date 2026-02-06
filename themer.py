#!/usr/bin/env python3

import os
import sys

def banner():
    print("""
╔════════════════════════════╗
║        ThemeR              ║
║   Theme Switch Tool        ║
║   Made by Rajdip ❤️        ║
╚════════════════════════════╝

1. Kali Dark Theme
2. Kali Light Theme
3. Exit
""")

def apply_dark():
    os.system("xfconf-query -c xsettings -p /Net/ThemeName -s 'Kali-Dark'")
    os.system("xfconf-query -c xsettings -p /Net/IconThemeName -s 'Flat-Remix-Blue-Dark'")
    print("[+] Dark theme applied")

def apply_light():
    os.system("xfconf-query -c xsettings -p /Net/ThemeName -s 'Kali-Light'")
    os.system("xfconf-query -c xsettings -p /Net/IconThemeName -s 'Flat-Remix-Blue'")
    print("[+] Light theme applied")

while True:
    banner()
    choice = input("Choose option: ")

    if choice == "1":
        apply_dark()
    elif choice == "2":
        apply_light()
    elif choice == "3":
        print("Exit… Bye 👋")
        sys.exit()
    else:
        print("Invalid choice")
