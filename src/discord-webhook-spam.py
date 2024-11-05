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
from Utils.Colors import *
from Utils.Config import *
from Utils.Banners import *
from Utils.Task import *

Title("Discord Webhook Spammer")

def EnterToContinue():
    print(f"{warning_prefix} {BRIGHT_RED}This program is unstoppable when you set there infinite times to spam. To close this program you \nwill need to close the whole BlueFruit. \n{question_prefix} {WHITE}Press {YELLOW}ENTER {WHITE}to continue.{RESET}")
    while True:
        key = readchar.readkey()
        if key in ('\n', '\r'):
            break

try:
    Slow(discord_banner)
    Slow(MainColor2(bluesplittingline))
    webhook = input(f"{question_prefix} Webhook {BRIGHT_BLUE}=> {RESET}")
    CheckWebhook(webhook)
    
    message = input(f"{question_prefix} Message {BRIGHT_BLUE}=> {RESET}")
    times_num = input(f"{question_prefix} How many times (0 for infinite) {BRIGHT_BLUE}=> {RESET}")
    if not times_num.isdigit():
        PrintError("Needs to be a number!")
        EnterToReset()
    
    EnterToContinue()
    Clear()
    if int(times_num) == 0:
        json_msg = {"content": message}
        while True:
            atmpt = requests.post(webhook, json=json_msg)
            if atmpt.ok:
                print(f"{time_hour_prefix()} {GREEN}Successfully sent!")
            else:
                print(f"{time_hour_prefix()} {BRIGHT_RED}Something went wrong.")
    else:
        json_msg = {"content": message}
        for _ in range(int(times_num)):
            atmpt = requests.post(webhook, json=json_msg)
            if atmpt.ok:
                print(f"{time_hour_prefix()} {GREEN}Successfully sent!")
            else:
                print(f"{time_hour_prefix()} {BRIGHT_RED}Something went wrong.")
    
    print(f"{time_hour_prefix()} {BRIGHT_GREEN}FINISHED!")
    EnterToReset()
    
    
except Exception as e:
    PrintError(e)
    EnterToReset()