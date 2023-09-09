import os
os.system('clear')
print('loading start assets')
inventory = {
    "money": 5
}
os.system('clear')
print('ready you have $' + str(inventory['money']))
inventory['money'] = input('how much money do you want        $')
print("you now have     $" + str(inventory['money']))