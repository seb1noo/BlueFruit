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

Title("Discord Server Info")

def EnterToContinue():
    print(f"{question_prefix} Press {YELLOW}ENTER {WHITE}to continue.{RESET}")
    while True:
        key = readchar.readkey()
        if key in ('\n', '\r'):
            break

try:
    Slow(discord_banner)
    Slow(MainColor2(bluesplittingline))
    invite = input(f"{question_prefix} Server invite {BRIGHT_BLUE}=> {RESET}")
    
    try:
        invite_code = invite.split("/")[-1]
    except:
        invite_code = invite
    
    response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")
    Slow(MainColor2(bluesplittingline))
    
    if response.status_code == 200:
        api = response.json()

        type_value = api.get('type', "None")
        code_value = api.get('code', "None")
        inviter_info = api.get('inviter', {})
        inviter_id = inviter_info.get('id', "None")
        inviter_username = inviter_info.get('username', "None")
        inviter_avatar = inviter_info.get('avatar', "None")
        inviter_discriminator = inviter_info.get('discriminator', "None")
        inviter_public_flags = inviter_info.get('public_flags', "None")
        inviter_flags = inviter_info.get('flags', "None")
        inviter_banner = inviter_info.get('banner', "None")
        inviter_accent_color = inviter_info.get('accent_color', "None")
        inviter_global_name = inviter_info.get('global_name', "None")
        inviter_banner_color = inviter_info.get('banner_color', "None")
        expires_at = api.get('expires_at', "None")
        flags = api.get('flags', "None")
        server_info = api.get('guild', {})
        server_id = server_info.get('id', "None")
        server_name = server_info.get('name', "None")
        server_icon = server_info.get('icon', "None")
        server_features = server_info.get('features', "None")
        if server_features != "None":
            server_features = ' / '.join(server_features)
        server_verification_level = server_info.get('verification_level', "None")
        server_nsfw_level = server_info.get('nsfw_level', "None")
        server_description = server_info.get('description', "None")
        server_nsfw = server_info.get('nsfw', "None")
        server_premium_subscription_count = server_info.get('premium_subscription_count', "None")
        channel_info = api.get('channel', {})
        channel_id = channel_info.get('id', "None")
        channel_type = channel_info.get('type', "None")
        channel_name = channel_info.get('name', "None")
    else:
        PrintError("Invalid discord server invite url")
        EnterToReset()
    
    Slow(f"""
{BRIGHT_BLUE}Invitation Information:
{RED}+ {GREEN}Invitation                        {BRIGHT_BLUE}=> {WHITE}{invite}
{RED}+ {GREEN}Type                              {BRIGHT_BLUE}=> {WHITE}{type_value}
{RED}+ {GREEN}Code                              {BRIGHT_BLUE}=> {WHITE}{code_value}
{RED}+ {GREEN}Expires                           {BRIGHT_BLUE}=> {WHITE}{expires_at}
{RED}+ {GREEN}Server ID                         {BRIGHT_BLUE}=> {WHITE}{server_id}
{RED}+ {GREEN}Server Name                       {BRIGHT_BLUE}=> {WHITE}{server_name}
{RED}+ {GREEN}Channel ID                        {BRIGHT_BLUE}=> {WHITE}{channel_id}
{RED}+ {GREEN}Channel Name                      {BRIGHT_BLUE}=> {WHITE}{channel_name}
{RED}+ {GREEN}Channel Type                      {BRIGHT_BLUE}=> {WHITE}{channel_type}
{RED}+ {GREEN}Server Description                {BRIGHT_BLUE}=> {WHITE}{server_description}
{RED}+ {GREEN}Server Icon                       {BRIGHT_BLUE}=> {WHITE}{server_icon}
{RED}+ {GREEN}Server Features                   {BRIGHT_BLUE}=> {WHITE}{server_features}
{RED}+ {GREEN}Server NSFW Level                 {BRIGHT_BLUE}=> {WHITE}{server_nsfw_level}
{RED}+ {GREEN}Server NSFW                       {BRIGHT_BLUE}=> {WHITE}{server_nsfw}
{RED}+ {GREEN}Flags                             {BRIGHT_BLUE}=> {WHITE}{flags}
{RED}+ {GREEN}Server Verification Level         {BRIGHT_BLUE}=> {WHITE}{server_verification_level}
{RED}+ {GREEN}Server Premium Subscription Count {BRIGHT_BLUE}=> {WHITE}{server_premium_subscription_count}
         """)

    if inviter_info:
        EnterToContinue()
        Slow(f"""
{BRIGHT_BLUE}Inviter Info:
{RED}+ {GREEN}ID                  {BRIGHT_BLUE}=> {WHITE}{inviter_id}
{RED}+ {GREEN}Username            {BRIGHT_BLUE}=> {WHITE}{inviter_username}
{RED}+ {GREEN}Global Name         {BRIGHT_BLUE}=> {WHITE}{inviter_global_name}
{RED}+ {GREEN}Avatar              {BRIGHT_BLUE}=> {WHITE}{inviter_avatar}
{RED}+ {GREEN}Tag (Discriminator) {BRIGHT_BLUE}=> {WHITE}#{inviter_discriminator}
{RED}+ {GREEN}Public Flags        {BRIGHT_BLUE}=> {WHITE}{inviter_public_flags}
{RED}+ {GREEN}Flags               {BRIGHT_BLUE}=> {WHITE}{inviter_flags}
{RED}+ {GREEN}Banner              {BRIGHT_BLUE}=> {WHITE}{inviter_banner}
{RED}+ {GREEN}Accent Color        {BRIGHT_BLUE}=> {WHITE}{inviter_accent_color}
{RED}+ {GREEN}Banner Color        {BRIGHT_BLUE}=> {WHITE}{inviter_banner_color}
            """)
    
    EnterToReset()
    
except Exception as e:
    PrintError(e)
    EnterToReset()