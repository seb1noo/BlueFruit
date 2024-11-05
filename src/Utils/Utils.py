# <============================== BlueFruit ==============================>
# Copyright (c) BlueFruit (https://github.com/seb1noo/BlueFruit)
#
# EN:
#   Do not touch or edit this file in any way, it can corrupt the BlueFruit.
#   If you find any errors, please contact the Owner through discord or the Issues tab on the GitHub Page.
#
# SK:
#   V žiadnom prípade sa tohto súboru nedotýkajte ani ho neupravujte, môže to poškodiť BlueFruit.
#   Ak nájdete nejaké chyby, kontaktujte prosím majiteľa cez Discord alebo záložku "Issues" na stránke GitHub.
# <=======================================================================>

# <============================== WARNING ==============================>
#   This script has taken inspiration from RedTiger Tools (https://github.com/loxy0dev/RedTiger-Tools)
#   - Was edited by LOAD with additional features and to work with BlueFruit!
#   ANY USE OF THIS SCRIPT, WITHOUT PERMISSION IS BANNABLE OFFENSE AND REASON FOR LICENSE PROBLEMS!
# <=======================================================================>

from .Config import *
from .Colors import *
try:
    import ctypes
    import subprocess
    import os
    import readchar
    import time
    import sys
    import datetime
    import sys
    import json
    import requests
    import webbrowser
    import struct
    import threading
    import tkinter as tk
    import random
    from tkinter.scrolledtext import ScrolledText
    import tempfile
    import string
except Exception as e:
    import os
    print(f"[x] | Error Module (Restart Setup): {e}")
    os.system("pause")

# [ ! ] PRIORITY FUNCTIONS
# (these functions are used in utils)
def current_time_day_hour():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def current_time_hour():
    return datetime.datetime.now().strftime('%H:%M:%S')

# USERNAME
try:
    username_pc = os.getlogin()
except:
    username_pc = "username"

# WEBHOOK DATA
username_webhook = "BlueFruit"
avatar_webhook = "https://cdn.discordapp.com/attachments/1267815599669772390/1302289836744638495/logo.jpeg?ex=6727936c&is=672641ec&hm=64f5d17a1282058a9abdb4ad48c8ffb9c2150d603cba36c32c5b30acac52f80e&"
color_webhook = 0x9734f3

# PREFIXES
info_prefix = f"{RED}[ {WHITE}i {RED}]{WHITE}:{RESET}"
warning_prefix = f"{RED}[ {WHITE}! {RED}]{WHITE}:{RESET}"
question_prefix = f"{RED}[ {WHITE}? {RED}]{WHITE}:{RESET}"
error_prefix = f"{RED}[ {WHITE}x {RED}]{WHITE}:{RESET}"
def time_hour_prefix(): return f"{RED}[ {WHITE}{current_time_hour()} {RED}]{WHITE}:{RESET}"
def time_day_hour_prefix(): return f"{RED}[ {WHITE}{current_time_day_hour()} {RED}]{WHITE}:{RESET}"

# DESIGNS
bluesplittingline = f"———————————————————————————————————————————————————————————————————————————————————————————————————————————"

# FUNCTIONS

def ModuleInstall(module):
    """Installs module

    Args:
        module (str): Module name to install
    """
    subprocess.check_call(['pip', 'install', module])

def ModuleUninstall(module):
    """Uninstalls module

    Args:
        module (str): Module name to uninstall
    """
    subprocess.check_call(['pip', 'uninstall', module])
    
def MenuInput():
    """Makes input for main menu of BlueFruit

    Returns:
        input: What has user written in the input
    """
    return input(f"{RED}[ {WHITE}{current_time_hour()}{BLUE}@{WHITE}{username_pc} {RED}] {WHITE}=> {RESET}")

def PrintError(error: str):
    """Prints custom error message to console

    Args:
        error (str): What error it should print.
    """
    print(f"{error_prefix} {BRIGHT_RED}{error}{RESET}")
    
def EnterToReset():
    """Sends message to EnterToReset, that means when user clicks Enter on this message it will restart the program (Returns back to Menu)
    """
    print(f"{question_prefix} Press {YELLOW}ENTER {WHITE}to go back to Menu.{RESET}")
    while True:
        key = readchar.readkey()
        if key in ('\n', '\r'):
            break
    Reset()
    
def ErrorWebhook():
    """Prints invalid webhook message
    """
    PrintError("Invalid Webhook")
    EnterToReset()
    
def Title(title):
    """Changes title of the console to the custom one

    Args:
        title (str): What title it should be
    """
    if sys.platform.startswith("win"):
        if title and title.strip():
            ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool} | {title}")
        else:
            ctypes.windll.kernel32.SetConsoleTitleW(f"{name_tool} {version_tool}")
    elif sys.platform.startswith("linux"):
        if title and title.strip():
            sys.stdout.write(f"\x1b]2;{name_tool} {version_tool} | {title}\x07")
        else:
            sys.stdout.write(f"\x1b]2;{name_tool} {version_tool}\x07")

def Reset():
    """Restarts the script
    """
    if sys.platform.startswith("win"):
        subprocess.Popen(['python', './BlueFruit.py'], shell=True)
        sys.exit()
    elif sys.platform.startswith("linux"):
        subprocess.Popen(['python3', './BlueFruit.py'], shell=True)
        sys.exit()
        
def Clear():
    """Clears console
    """
    if sys.platform.startswith("win"):
        os.system("cls")
    elif sys.platform.startswith("linux"):
        os.system("clear")
        
def Slow(texte):
    """Makes smooth animation for applying line after line

    Args:
        texte (str): Text it should animate
    """
    delay = 0.03
    lines = texte.split('\n')
    for line in lines:
        print(line)
        time.sleep(delay)
        
def set_console_size(width, height):
    """Sets console size to the selected ones

    Args:
        width (int): Width of the console window
        height (int): Height of the console window
    """
    if sys.platform.startswith("win"):
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleScreenBufferSize(handle, width | (height << 16))
        
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        GWL_STYLE = -16
        WS_MAXIMIZEBOX = 0x00010000
        WS_THICKFRAME = 0x00040000

        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

        style &= ~(WS_MAXIMIZEBOX | WS_THICKFRAME)

        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, style)
        os.system(f"mode con: cols={width // 8} lines={height // 12}")

    elif sys.platform.startswith("linux"):
        os.system(f"printf '\033[8;{height};{width}t'")
        
def is_clear_string(input_string):
    """Checks if its string

    Args:
        input_string (str): The string

    Returns:
        bool: If the string is clear
    """
    return bool(input_string.strip())

def StartProgram(program):
    """Starts program for BlueFruit

    Args:
        program (str): Program to start
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    program_path = os.path.join(base_dir, program)

    if sys.platform.startswith("win"):
        file = ['python', program_path]
        subprocess.run(file, shell=True)

    elif sys.platform.startswith("linux"):
        file = ['python3', program_path]
        subprocess.run(file, shell=True)
        
def MainColor2(text):
    """Makes smooth gradient colors for string

    Args:
        text (str): String to apply gradient color to

    Returns:
        str: Colored string
    """
    start_color = (5, 10, 169)  
    end_color = (118, 136, 255)

    num_steps = 9

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    
    colors += list(reversed(colors[:-1]))  
    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            color = colors[color_index]
            result.append(text_color(*color) + char + "\033[0m")
        
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)

def MainColorReversed2(text):
    """Makes smooth gradient colors for string, but reversed from function MainColor2

    Args:
        text (str): String to apply gradient color to

    Returns:
        str: Colored string
    """
    end_color = (5, 10, 169)  
    start_color = (118, 136, 255)

    num_steps = 9

    colors = []
    for i in range(num_steps):
        r = start_color[0] + (end_color[0] - start_color[0]) * i // (num_steps - 1)
        g = start_color[1] + (end_color[1] - start_color[1]) * i // (num_steps - 1)
        b = start_color[2] + (end_color[2] - start_color[2]) * i // (num_steps - 1)
        colors.append((r, g, b))
    
    colors += list(reversed(colors[:-1]))  
    
    def text_color(r, g, b):
        return f"\033[38;2;{r};{g};{b}m"
       
    lines = text.split('\n')
    num_colors = len(colors)
    
    result = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            color_index = (i + j) % num_colors
            color = colors[color_index]
            result.append(text_color(*color) + char + "\033[0m")
        
        if i < len(lines) - 1:
            result.append('\n')
    
    return ''.join(result)

def CheckWebhook(webhook):
    """Checks if webhook url is valid

    Args:
        webhook (str): Webhook URL
    """
    if webhook.lower().startswith("https://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://canary.discord.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("https://discordapp.com/api/webhooks"):
        pass
    elif webhook.lower().startswith("http://discordapp.com/api/webhooks"):
        pass
    else:
        ErrorWebhook()