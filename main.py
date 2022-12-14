import requests, time, json, os
from colorama import Fore

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')

url_server = []
header_old = {"Authorization": token, "Content-Type": 'application/json'}
header_invitation = {"Authorization": token, "Content-Type": 'application/json', "max_age": "0", "max_uses": "0", "temporary": "false"}

payload = {}
def guild_show():
  x = 0 # number guild 
  

  while True: # guild checking 
    try:
      guild_id = requests_info_guild[x]['id']
      print(f"[{Fore.GREEN}+{Fore.WHITE}]guild      : {guild_id}\t{requests_info_guild[x]['name']}")


      vanity = vanity_url_detect(guild_id) # func check vanity


      requests_for_channel_checker = requests.get(f'https://discord.com/api/v8/guilds/{guild_id}/channels', headers=header_old).json() # info channel check type 

      i = 0 # number channel 
      while True: # channel  checking
        if vanity == None:
           pass
        else:
          url_server.append(f"discord.gg/{vanity}")
          print(f"[{Fore.GREEN}+{Fore.WHITE}]invitation : {url_server[x]}")
          print("\n")
          x = x + 1
          time.sleep(1) # slow mod optional
          break
        
        try: 
          if requests_for_channel_checker[i]['type'] == 0: 
            good_channel = requests_for_channel_checker[i]['id']
            requests_info_invitation = requests.post(f"https://discord.com/api/v9/channels/{good_channel}/invites", headers=header_invitation, json=payload).json()
            if requests_info_invitation['code'] == 50013:
              i = i + 1
        
            else: # code gen success
              url_server.append(f"discord.gg/{requests_info_invitation['code']}")
              print(f"[{Fore.GREEN}+{Fore.WHITE}]channel    : {good_channel}\t{requests_for_channel_checker[i]['name']}")
              print(f"[{Fore.GREEN}+{Fore.WHITE}]invitation : {url_server[x]}")
              print("\n")
              x = x + 1
              time.sleep(1) # slow mod optional
              break
          else:
            i = i + 1 

        except Exception:
          print("error")
          x = x + 1 
          break


    except:
      print(f"\n[{Fore.YELLOW}~{Fore.WHITE}]Step 1 Success!")
      break
def vanity_url_detect(guild_id):
  requests_info_guild_vanity = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=header_old).json()
  return requests_info_guild_vanity['vanity_url_code']


def list_success_server():
    os.system('cls')
    f = open("backup.txt", "a")
    v = 0
    for _ in requests_info_guild:
      if url_server[v] == "30016": # soon update
        url = "???"

      else:
        url = "??????"
        print(f"guild  : {requests_info_guild[v]['name']}  : {url}")
        v = v + 1
        try:
            f.write(f"{url_server[v]}\n")
        except:
            pass
    f.close()
    
def list_relationships():
  f = open("backup.txt", "a")
  api4 = f"users/@me/relationships"
  requests_relationships = requests.get(f'https://discord.com/api/v9/{api4}', headers=header_old).json()
  for fr13nd in requests_relationships:
    print(f"{fr13nd['user']['username']}#{fr13nd['user']['discriminator']}\t ID : {fr13nd['user']['id']}")
    f.write(f"{fr13nd['user']['username']}#{fr13nd['user']['discriminator']}\t ID : {fr13nd['user']['id']}\n")
  f.close()

requests_info_guild = requests.get(f'https://discord.com/api/v8/users/@me/guilds', headers=header_old).json()
guild_show()
list_relationships()
list_success_server() 
