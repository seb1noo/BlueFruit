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
from Utils.Banners import *
from Utils.Colors import *
from Utils.Config import *
from Utils.Task import *
   
Title("Ip Generator")

Slow(map_banner)
Slow(MainColor2(bluesplittingline))

stored_kick_val = True

def Kick(value: bool = None):
    global stored_kick_val
    if value is None:
        return stored_kick_val
    else:
        stored_kick_val = value
        return stored_kick_val

try:
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
            'embeds': [embed_content],
            'username': username_webhook,
            'avatar_url': avatar_webhook
        }

        headers = {
            'Content-Type': 'application/json'
        }

        requests.post(webhook_url, data=json.dumps(payload), headers=headers)

    number_valid = 0
    number_invalid = 0
    def ip_check():
        global number_valid, number_invalid
        number_1 = random.randint(1, 255)
        number_2 = random.randint(1, 255)
        number_3 = random.randint(1, 255)
        number_4 = random.randint(1, 255)
        ip = f"{number_1}.{number_2}.{number_3}.{number_4}"

        try:
            if sys.platform.startswith("win"):
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, text=True, timeout=0.1)
            elif sys.platform.startswith("linux"):
                result = subprocess.run(['ping', '-c', '1', '-W', '1', ip], capture_output=True, text=True, timeout=0.1)

            if result.returncode == 0:
                number_valid += 1
                if webhook.lower() in ['y', "yes", "ye", "es", "yep"]:
                    embed_content = {
                        'title': 'Ip Valid !',
                        'description': f"**Ip:**\n```{ip}```",
                        'color': color_webhook,
                        'footer': {
                            "text": username_webhook,
                            "icon_url": avatar_webhook,
                        }
                    }
                    send_webhook(embed_content)
                    print(f"{time_hour_prefix()} {BOLD}{GREEN}IP VALID!   {RESET}{WHITE}{RED}{number_invalid} {WHITE}invalid found - {GREEN}{number_valid} {WHITE}valid found. {GREEN}Ip: {BRIGHT_GREEN}{ip}{RESET}")
                    if stop_at_validb:
                        Kick(False)
                else:
                    print(f"{time_hour_prefix()} {BOLD}{GREEN}IP VALID!   {RESET}{WHITE}{RED}{number_invalid} {WHITE}invalid found - {GREEN}{number_valid} {WHITE}valid found. {GREEN}Ip: {BRIGHT_GREEN}{ip}{RESET}")
                    if stop_at_validb:
                        Kick(False)
                
            else:
                number_invalid += 1
                print(f"{time_hour_prefix()} {BOLD}{RED}IP INVALID! {RESET}{WHITE}{RED}{number_invalid} {WHITE}invalid found - {GREEN}{number_valid} {WHITE}valid found. {RED}Ip: {BRIGHT_RED}{ip}{RESET}")
        except:
            number_invalid += 1
            print(f"{time_hour_prefix()} {BOLD}{RED}IP INVALID! {RESET}{WHITE}{RED}{number_invalid} {WHITE}invalid found - {GREEN}{number_valid} {WHITE}valid found. {RED}Ip: {BRIGHT_RED}{ip}{RESET}")
        Title(f"Ip Generator - Invalid: {number_invalid} - Valid: {number_valid}")

    def request():
        while Kick():
            threads = []
            try:
                for _ in range(int(threads_number)):
                    t = threading.Thread(target=ip_check)
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