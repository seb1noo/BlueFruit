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
import time

Title("Verify Program")

Slow(logo_banner)
Slow(f"""
{info_prefix} {WHITE}This test will check if BlueFruit is correctly installed or not. If not, it will throw error \nand you need to reinstall BlueFruit. But if its not major problem, this program can also fix it.
{warning_prefix} {RED}WARNING! {RESET}{BRIGHT_RED}This test is not finished and checks only license, version and creator. Also its not \noptimized so it can take performance.""")
f_data = input(f"{question_prefix} {BRIGHT_RED}Do you still want to continue? {WHITE}(y/n) {BRIGHT_BLUE}=> {RESET}")
if not f_data.lower() in ['y', "yes", "ye", "es", "yep"]:
    EnterToReset()
else:
    Clear()
    print(f"{time_hour_prefix()} {BRIGHT_RED}In here will be displayed logs what is the program doing.")
    task.wait(1)
    print(f"{time_hour_prefix()} {GREEN}Starting...")
    start_time = time.time()
    task.wait(3)
    print(f"{time_hour_prefix()} Checking version...")
    data = requests.get(version_check)
    continue_1 = False
    tests_passed_1 = 0
    tests_done_1 = 0
    if data.status_code != 200:
        data = data.json()
        if data["status"] == "404":
            print(f"{time_hour_prefix()} {BRIGHT_RED}Corrupted or BETA Version detected!")
            tests_done_1 += 1
            tests_passed_1 += 0
            continue_1 = True
        else:
            tg_nm = False
            nm = False
            if "tag_name" in data:
                tg_nm = True
            elif "name" in data:
                nm = True
            else:
                print(f"{time_hour_prefix()} {BRIGHT_RED}Corrupted or BETA Version detected!")
                tests_done_1 += 1
                tests_passed_1 += 0
                continue_1 = True

            if tg_nm and not continue_1:
                if data["tag_name"] == version_tool:
                    print(f"{time_hour_prefix()} {GREEN}Version is stable and up-to-date.")
                    tests_done_1 += 1
                    tests_passed_1 += 1
                    continue_1 = True
                else:
                    if nm and not continue_1:
                        if data["name"] == version_tool:
                            print(f"{time_hour_prefix()} {GREEN}Version is stable and up-to-date.")
                            tests_done_1 += 1
                            tests_passed_1 += 1
                            continue_1 = True
                        else:
                            print(f"{time_hour_prefix()} {BRIGHT_RED}Version is outdated and unstable!")
                            tests_done_1 += 1
                            tests_passed_1 += 0
                            continue_1 = True
                    else:
                        if not continue_1:
                            print(f"{time_hour_prefix()} {BRIGHT_RED}Corrupted or BETA Version detected!")
                            tests_done_1 += 1
                            tests_passed_1 += 1
                            continue_1 = True
            else:
                if nm and not continue_1:
                    if data["name"] == version_tool:
                        print(f"{time_hour_prefix()} {GREEN}Version is stable and up-to-date.")
                        tests_done_1 += 1
                        tests_passed_1 += 1
                        continue_1 = True
                    else:
                        print(f"{time_hour_prefix()} {BRIGHT_RED}Version is outdated and unstable!")
                        tests_done_1 += 1
                        tests_passed_1 += 0
                        continue_1 = True
                else:
                    if not continue_1:
                        print(f"{time_hour_prefix()} {BRIGHT_RED}Corrupted or BETA Version detected!")
                        tests_done_1 += 1
                        tests_passed_1 += 0
                        continue_1 = True
    print(f"{time_hour_prefix()} {GREEN}Version check has been done in {YELLOW}{tests_done_1} tests{GREEN}, out of what {YELLOW}{tests_passed_1} tests {GREEN}passed.")
    print(f"{time_hour_prefix()} Checking license and creator...")
    tests_done_2 = 0
    tests_passed_2 = 0
    task.wait(3)
    tests_done_2 += 1
    print(f"{time_hour_prefix()} {BRIGHT_RED}License not found, but openable!") 
    tests_passed_2 += 0
    task.wait(0.03)
    tests_done_2 += 1
    if creator_tool.lower() == "load (seb1noo)" or creator_tool.lower() == "load" or creator_tool.lower() == "seb1noo" or creator_tool.lower() == "(seb1noo)":
        print(f"{time_hour_prefix()} {GREEN}Creator is valid and verified!")
        tests_passed_2 += 1
    else:
        print(f"{time_hour_prefix()} {BRIGHT_RED}Creator is not valid!")
        tests_passed_2 += 0
    
    print(f"{time_hour_prefix()} {GREEN}License and creator check has been done in {YELLOW}{tests_done_2} tests{GREEN}, out of what {YELLOW}{tests_passed_2} tests {GREEN}passed.")
    print(f"{time_hour_prefix()} Checking Utils...")
    task.wait(3)
    print(f"{time_hour_prefix()} {BRIGHT_RED}Skipping Util Test - Module for testing Utils was not found!") 
    task.wait(0.03)
    print(f"{time_hour_prefix()} Finishing tests...")
    task.wait(5)
    
    total_time = int(time.time() - start_time)
    minutes, seconds = divmod(total_time, 60)
    
    if minutes > 0:
        time_passed = f"{minutes}m {seconds}s"
    else:
        time_passed = f"{seconds}s"
    
    print(f"{time_hour_prefix()} {GREEN}Test finished! {YELLOW}{tests_done_1 + tests_done_2} tests{GREEN} were done, out of what {YELLOW}{tests_passed_1 + tests_passed_2} tests {GREEN}passed.")
    print(f"{time_hour_prefix()} {GREEN}Total time passed: {YELLOW}{time_passed}")
    
    EnterToReset()