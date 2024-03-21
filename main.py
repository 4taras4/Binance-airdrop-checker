import os
import json
from termcolor import cprint

with open("results.json", "r") as file:
    JSON = json.load(file)

with open("wallets.txt", "r") as f:
    WALLETS = [row.strip().lower() for row in f]
    
if __name__ == "__main__":
    eligble_wallets = []
    
    for data in JSON["l1"]:
        address = str(data.lower())
        if address in WALLETS:
            cprint(f"l1 elligable: {address}", 'green')
            eligble_wallets.append(address)

    for data in JSON["l2"]:
        address = str(data.lower())
        if address in WALLETS:
            cprint(f"l2 elligable: {address}", 'green')
            eligble_wallets.append(address)

    cprint(f'{len(eligble_wallets)} eligble wallets\n', 'white')
    with open("eligble_wallets.json", "w+") as file:
        json.dump(eligble_wallets, file, indent=4, ensure_ascii=False)