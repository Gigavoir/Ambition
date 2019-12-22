import random
from colorama import init, Fore, Back, Style
init(autoreset=True)

#Character classes
class Warrior:
  def __init__(self, p, t):
    self.player = p 
    self.team = t
    self.mana = 10
    self.health = 0
    self.armor = 16
  def attack(self, players, chars, names):
    tar = -1
    print("[P"+str(self.player+1)+"] Select a target for "+Fore.RED+"Attack"+Style.RESET_ALL+": ")
    for x in range(players):
      if x != self.player:
        print("("+str(x+1)+") "+str(names[x]))
    while tar < 0 or tar > players:
      tar = int(input("Target: "))
      tar = tar-1
      if tar < 0 or tar > players-1:
        print("That's not a valid target.")
        tar = -1
      elif tar != self.player:
        print("Attacked "+str(names[tar])+".")
      else:
        print("You can't target yourself with this.")
        tar = -1
  def charge(self, players, chars, names):
    self.mana = self.mana-10
    print("Casted "+Fore.YELLOW+"Charge"+Style.RESET_ALL+".")
  def taunt(self, players, chars, names):
    tar = -1
    print("[P"+str(self.player+1)+"] Select a target for "+Fore.BLUE+"Taunt"+Style.RESET_ALL+": ")
    for x in range(players):
      if x != self.player:
        print("("+str(x+1)+") "+str(names[x]))
    while tar < 0 or tar > players:
      tar = int(input("Target: "))
      tar = tar-1
      if tar < 0 or tar > players-1:
        print("That's not a valid target.")
        tar = -1
      elif tar != self.player:
        print("Taunted "+str(names[tar])+".")
      else:
        print("You can't target yourself with this.")
        tar = -1
    self.mana = self.mana-15

class Mage:
  def __init__(self, p, t):
    self.player = p
    self.team = t
    self.health = 50
    self.mana = 0
    self.armor = 10
  def attack(self, players, chars, names):
    tar = -1
    print("[P"+str(self.player+1)+"] Select a target for "+Fore.RED+"Attack"+Style.RESET_ALL+": ")
    for x in range(players):
      if x != self.player:
        print("("+str(x+1)+") "+str(names[x]))
    while tar < 0 or tar > players:
      tar = int(input("Target: "))
      tar = tar-1
      if tar < 0 or tar > players-1:
        print("That's not a valid target.")
        tar = -1
      elif tar != self.player:
        print("Attacked "+str(names[tar])+".")
      else:
        print("You can't target yourself with this.")
        tar = -1
  def frostbolt(self, players, chars, names):
    tar = -1
    print("[P"+str(self.player+1)+"] Select a target for "+Fore.RED+"Frostbolt"+Style.RESET_ALL+": ")
    for x in range(players):
      if x != self.player:
        print("("+str(x+1)+") "+str(names[x]))
    while tar < 0 or tar > players:
      tar = int(input("Target: "))
      tar = tar-1
      if tar < 0 or tar > players-1:
        print("That's not a valid target.")
        tar = -1
      elif tar != self.player:
        print("Attacked "+str(names[tar])+" with "+Fore.RED+"Frostbolt"+Style.RESET_ALL+".")
      else:
        print("You can't target yourself with this.")
        tar = -1
    self.mana = self.mana - 20
  def fireball(self, players, chars, names):
    self.mana = self.mana-45
    print("Casted "+Fore.RED+"Fireball"+Style.RESET_ALL+".")


#Number of players
def numPlayers():
  s = 0
  while s < 2 or s > 6:
    s = int(input("Enter a number of players between 2 and 6: "))
    if s < 2 or s > 6:
      print("Error. Please enter a number between 2 and 6.")
    else:
      print("Game will be played with "+str(s)+" players.")
      return(s)

#If more than 2 players are selected will prompt for teams
def teamsEnabled():
  s = 0
  b = False
  if players > 2:
    while b == False:
      s = str(input("Enable teams? Y/N: "))
      if s == "Y" or s == "y":
        print("Teams enabled.")
        b = True
        return(True)
      elif s == "N" or s == "n":

        print("Teams disabled.")
        b = True
        return(False)
      else:
        print("Error. Please enter Y or N.")

#Name selection
def nameSelect(y):
  s = 0
  a = False
  names = []
  for x in range(y):
    a = False
    while a == False:
      s = str(input("Enter name for Player "+str(x+1)+": "))
      s = s.capitalize()
      if s in names:
        print("Name already taken. Enter a new name.")
      else:
        names.append(s)
        a = True
  return(names)
    

#Character selection
def charSelect(y, n):
  print("Roles: "+Fore.BLUE+"Tank"+Style.RESET_ALL+", "+Fore.GREEN+"Healer"+Style.RESET_ALL+", "+Fore.RED+"Damage")
  print("Available classes:\n(1) "+Fore.BLUE+"Warrior\n"+Style.RESET_ALL+"(2)"+Fore.RED+" Mage\n"+Style.RESET_ALL+"(3)"+Fore.RED+" Rogue\n"+Style.RESET_ALL+"(4)"+Fore.GREEN+" Cleric\n"+Style.RESET_ALL+"(5)"+Fore.RED+" Ranger")
  chars = []
  for x in range(y):
    s = 0
    while s < 1 or s > 5:
      s = int(input("Select class for "+str(n[x])+": "))
      if s == 1:
        chars.append(Warrior(x, -1))
        print("Selected Warrior.")
      elif s == 2:
        chars.append(Mage(x, -1))
        print("Selected Mage.")
      elif s == 3:
        chars.append(Rogue(x, -1))
        print("Selected Rogue")
      elif s == 4:
        chars.append(Cleric(x, -1))
        print("Selected Cleric.")
      elif s == 5:
        chars.append(Ranger(x, -1))
        print("Selected Ranger.")
      else:
        print("Invalid selection.")
    #print(x)
  return(chars)


#Team selection
def teamSelect(y, c):
  s = 0
  t = []
  print("Team (1) = "+Fore.RED+"Red Team\n"+Style.RESET_ALL+"Team (2) = "+Fore.BLUE+"Blue Team")
  for x in range(y):
    s = int(input("Select team for P"+str(x+1)+" ("+str(c[x])+"): "))
    #if s == 1:



#Display setup info
print(Fore.YELLOW+"-=[AMBITION AUTOMATED v1.0]=-")
players = numPlayers()
if players > 2:
  teams = teamsEnabled()
else:
  teams = False
names = nameSelect(players)
chars = charSelect(players, names)
if teams == True:
  playerTeams = teamSelect(players, chars)
print("Number of players: "+str(players))
print("Teams: "+str(teams))

chars[0].attack(players, chars, names)
chars[1].charge(players, chars, names)
chars[2].taunt(players, chars, names)
chars[3].frostbolt(players, chars, names)
chars[4].fireball(players, chars, names)

if teams == False:
  print("Character selections:\n"+str(chars))
elif teams == True:
  print("Character and team selections:\n"+str(teamRed)+"\n"+str(teamBlue))
else:
  print("Something went very wrong. Consider restarting the program.")



