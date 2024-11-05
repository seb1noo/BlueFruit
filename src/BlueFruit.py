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

from Utils.Utils import *
from Utils.Config import *
from Utils.Colors import *
from Utils.Banners import *
from Utils.Task import *

Clear()
Title("")
set_console_size(856, 348)

def ResetMenu(ResetWindow: bool = False):
    print(f"{question_prefix} Press {YELLOW}ENTER {WHITE}to go back to Menu.{RESET}")
    while True:
        key = readchar.readkey()
        if key in ('\n', '\r'):
            break
    MainMenuPrint(ResetWindow)
    
def EnterToContinue(ResetWindow: bool = False):
    print(f"{question_prefix} Press {YELLOW}ENTER {WHITE}to continue.{RESET}")
    while True:
        key = readchar.readkey()
        if key in ('\n', '\r'):
            break
    MainMenuPrint(ResetWindow)
    
def EnterToExit():
    print(f"{question_prefix} Press {YELLOW}ENTER {WHITE}to Exit.{RESET}")
    while True:
        key = readchar.readkey()
        if key in ('\n', '\r'):
            break
    sys.exit(None)

def MainMenuPrint(ResetWindow: bool = False):
    Title("Menu")
    Clear()
    if ResetWindow:
        set_console_size(856, 348)
    Slow(MainColor2(f"""
                         ____    _                  _____                  _   _   
                        | __ )  | |  _   _    ___  |  ___|  _ __   _   _  (_) | |_ 
                        |  _ \  | | | | | |  / _ \ | |_    | '__| | | | | | | | __|
                        | |_) | | | | |_| | |  __/ |  _|   | |    | |_| | | | | |_ 
                        |____/  |_|  \__,_|  \___| |_|     |_|     \__,_| |_|  \__|
    """))

    menu = f"""
                                        {GREEN}github.com/seb1noo/BlueFruit
                                    
                                
{RED}[ {WHITE}I {RED}] {BRIGHT_BLUE}=> {WHITE}INFO                                                                {RED}[ {WHITE}R {RED}] {BRIGHT_BLUE} => {WHITE}RESTART 
{RED}[ {WHITE}E {RED}] {BRIGHT_BLUE}=> {WHITE}EXIT                                                                {RED}[ {WHITE}UC {RED}] {BRIGHT_BLUE}=> {WHITE}USER-CREATED TOOLS  
{MainColor2(bluesplittingline)}
{RESET}{RED}[ {WHITE}01 {RED}] {BRIGHT_BLUE}=> {WHITE}BlueFruit Verify         {RESET}{RED}[ {WHITE}04 {RED}] {BRIGHT_BLUE}=> {WHITE}Discord Server Info
{RESET}{RED}[ {WHITE}02 {RED}] {BRIGHT_BLUE}=> {WHITE}Ip Generator             {RESET}{RED}[ {WHITE}05 {RED}] {BRIGHT_BLUE}=> {WHITE}Discord Webhook Spammer        {RESET}{RED}[ {WHITE}! {RED}] {BRIGHT_BLUE}=> {WHITE}More Coming Soon!
{RESET}{RED}[ {WHITE}03 {RED}] {BRIGHT_BLUE}=> {WHITE}Discord Nitro Generator  {RESET}{RED}[ {WHITE}06 {RED}] {BRIGHT_BLUE}=> {WHITE}Discord Webhook Generator
{MainColorReversed2(bluesplittingline)}
{RESET}
"""

    Slow(menu)
    selected_data = MenuInput()
    if not is_clear_string(selected_data):
        PrintError("You need to write option to continue.")
        ResetMenu()
    else:
        if not selected_data.isdigit():
            if selected_data.lower() == "i":
                StartProgram("info.py")
            elif selected_data.lower() == "e":
                Slow("""\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
                    """)
                task.wait(1)
            elif selected_data.lower() == "r":
                Reset()
            elif selected_data.lower() == "u":
                PrintError(f"Invalid Option. Please try again. {YELLOW}Haven't you mean {WHITE}UC{YELLOW}?")
                ResetMenu()
            elif selected_data.lower() == "c":
                PrintError(f"Invalid Option. Please try again. {YELLOW}Haven't you mean {WHITE}UC{YELLOW}?")
                ResetMenu()
            elif selected_data.lower() == "uc":
                PrintError("This option is coming soon! For now its unavailable.")
                ResetMenu()
            else:
                PrintError("Invalid Option. Please try again.")
                ResetMenu()
        else:
            with open("./data/menu_items.json", "r") as f:
                menu_items = json.load(f)
            
            with open("./data/items_coming_soon.json", "r") as f:
                ics = json.load(f)
            
            if selected_data in menu_items:
                StartProgram(menu_items[selected_data])
            else:
                if selected_data in ics:
                    PrintError("This option is coming soon! For now its unavailable.")
                    ResetMenu()
                else:
                    PrintError("Invalid Option.")
                    ResetMenu()

data = requests.get(version_check).json()
if "status" in data and data["status"] == "404":
    Title("Warning")
    PrintError("You are using either corrupted version or version in Beta.")
    EnterToContinue()
else:
    tg_nm = False
    nm = False
    if "tag_name" in data:
        tg_nm = True
    elif "name" in data:
        nm = True
    else:
        PrintError("You are using either corrupted version or version in Beta.")
        EnterToContinue()

    if tg_nm:
        if data["tag_name"] == version_tool:
            MainMenuPrint()
        else:
            if nm:
                if data["name"] == version_tool:
                    MainMenuPrint()
                else:
                    Title("Warning")
                    PrintError("You have outdated version of the BlueFruit. Please update to continue using.")
                    EnterToExit()
            else:
                Title("Warning")
                PrintError("You are using either corrupted version or version in Beta.")
                EnterToContinue()
    else:
        if nm:
            if data["name"] == version_tool:
                MainMenuPrint()
            else:
                Title("Warning")
                PrintError("You have outdated version of the BlueFruit. Please update to continue using.")
                EnterToExit()
        else:
            Title("Warning")
            PrintError("You are using either corrupted version or version in Beta.")
            EnterToContinue()