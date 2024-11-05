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

from Utils.Utils import *
from Utils.Colors import *
from Utils.Config import *
from Utils.Banners import *
from Utils.Task import *

Title(f"Discord Nitro Generator")

stored_kick_val = True

def Kick(value: bool = None):
    global stored_kick_val
    if value is None:
        return stored_kick_val
    else:
        stored_kick_val = value
        return stored_kick_val

try:
    Slow(discord_banner)
    Slow(MainColor2(bluesplittingline))
    task.wait(0.03)
    webhook = input(f"{question_prefix} Webhook ? (y/n) {BRIGHT_BLUE}=> {RESET}")
    if webhook.lower() in ['y', "yes", "ye", "es", "yep"]:
        webhook_url = input(f"{question_prefix} Webhook URL {BRIGHT_BLUE}=> {RESET}")
        CheckWebhook(webhook_url)
    
    try:
        threads_number = int(input(f"{question_prefix} Threads Number {BRIGHT_BLUE}=> {RESET}"))
    except:
        PrintError("Please write valid number.")
        EnterToReset()
    
    stop_at_validb = False
    stop_at_valid = input(f"{question_prefix} Stop at first valid ? (y/n) {BRIGHT_BLUE}=> {RESET}")
    if stop_at_valid.lower() in ['y', "yes", "ye", "es", "yep"]:
        stop_at_validb = True
    
    def send_webhook(embed_content):
        payload = {
            'embeds': [{
                    'title': f'Nitro Valid !',
                    'description': f"**Nitro:**\n```{embed_content}```",
                    'color': color_webhook,
                    'footer': {
                    "text": username_webhook,
                    "icon_url": avatar_webhook,
                    }
            }],
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }

        headers = {
            'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    
    number_valid = 0
    number_invalid = 0
    
    def check_nitro():
        global number_valid, number_invalid
        code_nitro = ''.join([random.choice(string.ascii_uppercase + string.digits) for _ in range(16)])
        url_nitro = f'https://discord.gift/{code_nitro}'
        response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code_nitro}?with_application=false&with_subscription_plan=true', timeout=1)
        if response.status_code == 200:
            number_valid += 1
            if webhook.lower() in ['y', "yes", "ye", "es", "yep"]:
                send_webhook(url_nitro)
                
            print(f"{time_hour_prefix()} {BOLD}{GREEN}NITRO VALID!   {RESET}{WHITE}{RED}{number_invalid} {WHITE}invalid found - {GREEN}{number_valid} {WHITE}valid found. {GREEN}Nitro: {BRIGHT_GREEN}{url_nitro}{RESET}")
            if stop_at_validb:
                Kick(False)
        else:
            number_invalid += 1
            print(f"{time_hour_prefix()} {BOLD}{RED}NITRO INVALID! {RESET}{WHITE}{RED}{number_invalid} {WHITE}invalid found - {GREEN}{number_valid} {WHITE}valid found. {RED}Nitro: {BRIGHT_RED}{url_nitro}{RESET}")
        
        Title(f"Discord Nitro Generator - Invalid: {number_invalid} - Valid: {number_valid}")
    
    def request():
        while Kick():
            threads = []
            try:
                for _ in range(int(threads_number)):
                    t = threading.Thread(target=check_nitro)
                    t.start()
                    threads.append(t)
            except:
                PrintError("Threads number parameter is invalid.")
                EnterToReset()
                break

            for thread in threads:
                thread.join()
            
            if not Kick():
                EnterToReset()
                break

    request()
        
except Exception as e:
    PrintError(e)
    EnterToReset()