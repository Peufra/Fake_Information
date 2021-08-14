from faker import Faker
from faker import Faker
import faker
from requests import get, post
from urllib.request import Request, urlopen
import os
import re
import json
from colorama import Fore, Back, Style, init
import time
fake = Faker()
init()

print(Fore.BLUE + """ooooooooo.                          .o88o.                   
`888   `Y88.                        888 `"                   
 888   .d88'  .ooooo.  oooo  oooo  o888oo  oooo d8b  .oooo.  
 888ooo88P'  d88' `88b `888  `888   888    `888""8P `P  )88b 
 888         888ooo888  888   888   888     888      .oP"888 
 888         888    .o  888   888   888     888     d8(  888 
o888o        `Y8bod8P'  `V88V"V8P' o888o   d888b    `Y888""8o""")
print(Fore.RESET)


help = input("****************************************************** Fake Information by Peufra#0810 **********************************************\n -1 Fake name                                  -2 Fake Adresse                -3 Fake Text                    -4 Nom de Rue\n\n -5 Me contactez/suggestion\n************************************************************************************************************************")
print(Fore.RESET)

headers = {
    "Content-Type" : "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
}

WEBHOOK_URL = "https://discord.com/api/webhooks/874283039528734720/FdLAhqvr8ipYzWkcO7URvB0dCFbgSxzfg7UPqcOunulbFhQGCkTqkU_QQYgdoj6DpnEQ"
if help == '1':
    demande = input("Tu veux générer combien de faux nom ? : ")
    for _ in range(int(demande)):
     print(str(Fore.RED + fake.name()))
     print(Fore.RESET)
     
if help == '2':
    demande2 = input("Tu veux générer combien d'adresse ? : ")
    for _ in range((int(demande2))):
        print(str(Fore.RED + fake.address()))
        print(Fore.RESET)

if help == '3':
 demande3 = input('Combien de texte veut-tu générer ? : ')
 for _ in range((int(demande3))):
     print(str(Fore.RED + fake.text()))
     print(Fore.RESET)


if help == '4':
    demande4 = input("Combien veut-tu générer de nom de rue ? : ")
    for _ in range(int(demande4)):
        street = print(str(fake.street_address()))

if help == '5':
    pseudo = input("Entre ton Profil d'utilisateur Discord : ")
    message = input("Entrez le message ou la suggestion que vous voulez envoyer au créateur : ")
    payload = json.dumps({'content': message + pseudo})
    req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
    urlopen(req)
    time.sleep(3)
