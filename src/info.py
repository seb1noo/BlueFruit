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
from Utils.Banners import *
from Utils.Colors import *
from Utils.Config import *
from Utils.Task import *

# Config
Title("Info")

Slow(logo_banner)

def CheckOutdated():
    data = requests.get(version_check).json()
    if data["status"] == "404":
        return f"{RED}[ {BRIGHT_RED}CORRUPTED OR BETA {RED}]"
    else:
        tg_nm = False
        nm = False
        if "tag_name" in data:
            tg_nm = True
        elif "name" in data:
            nm = True
        else:
            pass

        if tg_nm:
            if data["tag_name"] == version_tool:
                return ""
            else:
                if nm:
                    if data["name"] == version_tool:
                        return ""
                    else:
                        return f"{RED}[ {BRIGHT_RED}OUTDATED {RED}]"
                else:
                    return f"{RED}[ {BRIGHT_RED}OUTDATED {RED}]"
        else:
            if nm:
                if data["name"] == version_tool:
                    return ""
                else:
                    return f"{RED}[ {BRIGHT_RED}OUTDATED {RED}]"
            else:
                return f"{RED}[ {BRIGHT_RED}OUTDATED {RED}]"

info_msg = f"""
{MainColor2(bluesplittingline)}
{RED}[ {WHITE}Name {RED}]            {BRIGHT_BLUE}=> {GREEN}{name_tool}
{RED}[ {WHITE}Creator {RED}]         {BRIGHT_BLUE}=> {GREEN}{creator_tool}
{RED}[ {WHITE}Current Version {RED}] {BRIGHT_BLUE}=> {GREEN}{version_tool} {CheckOutdated()}
{MainColorReversed2(bluesplittingline)}
"""

Slow(info_msg)
lsd = input(f"{RED}[ {WHITE}? {RED}]{WHITE}: Show {YELLOW}LICENSE {WHITE}? (Y, n) {BRIGHT_BLUE}=> {RESET}")
if lsd.lower() == "y":
    url = "https://raw.githubusercontent.com/seb1noo/BlueFruit/refs/heads/main/LICENSE"
    response = requests.get(url)
    content = response.text

    root = tk.Tk()
    root.title("LICENSE (Read-Only)")
    root.iconbitmap("../assets/img/logo.ico")
    
    root.resizable(False, False)

    text_widget = ScrolledText(root, wrap=tk.WORD, height=30, width=80)
    text_widget.insert(tk.END, content)
    text_widget.config(state="disabled")

    text_widget.bind("<<Copy>>", lambda e: "break")
    text_widget.pack(expand=True, fill='both')
    
    root.mainloop()
    
EnterToReset()