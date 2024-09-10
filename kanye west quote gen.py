import random
import requests
from colorama import Fore, init
import json
init(autoreset=True)

with open('quotes.json', 'r') as f:
    data = json.load(f)

print(Fore.RED + random.choice(data))