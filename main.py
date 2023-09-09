import time
import os
def start():
  print('loading start assets')
  inventory = {
      "money": 5
  }
  os.system('clear')
  print("Villager News RPG")
  time.sleep(.5)
  print('')
  print('')
  print('type s to start')
  if (input('')) == ('s'):
    os.system('clear')
    print('you are steve')
    time.sleep(2)
    print('you want to beat the ender dragon')
    time.sleep(2)
    print('acheive your goal')
    print('')
    time.sleep(1)
    print('type c to continue')
    if (input('')) == ('c'):
      startlocation()
def startlocation():
  os.system('clear')
  print('Choose a Location (type the number)')
  print('')
  time.sleep(.5)
  print('1. Main Village  (under construction)')
  time.sleep(.1)
  print('2. Testificates Village  (under construction)')
  time.sleep(.1)
  print('2. Witches Lake  (under construction)')
  time.sleep(.1)
  print('4. Fishing Lake  (under construction)')
  print('')
  location = (input(''))
  if location == ('1'):
    mainvillage()
  if location == ('2'):
    os.system('clear')
    print('this area is under construction')
  if location == ('3'):
    os.system('clear')
    print('this area is under construction')
  if location == ('4'):
    os.system('clear')
    print('this area is under construction')
def mainvillage():
  os.system('clear')
  print('Choose a Building (type the number)')
  print('')
  print('1. Jerrys House')
  time.sleep(.1)
  print('2. Homeless Villagers Shack')
  time.sleep(.1)
  print('3. Church')
  time.sleep(.1)
  print('4. Blacksmith')
  time.sleep(.1)
  print('5. Mayors Office/Village Court')
  time.sleep(.1)
  print('6. Villager News HQ')
  print('7. Leave Main Village')
  print('')
  building = (input(''))
  if building == ('1'):
    os.system('clear')
    jerryshouse()
  if building == ('2'):
    homelessvillager()
  if building == ('7'):
    startlocation()
def jerryshouse():
  os.system('clear')
  print('this area it under construction')
def homelessvillager():
  os.system('clear')
  print('Homeless Villager: Hello welcome to my shack.')
  print('what do you want to do (type the number)')
  print('1. Donate 🪙10')
  print('2. say hi')
  print('3. leave')
  print('')
  option = input('')
  if option == '1':
    if inventory[money] >= 10:
      inventory[money] -= 10
      print('thanks for the donation heres a gun')
start()