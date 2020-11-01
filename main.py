from classes.game import Person, bcolors
from classes.magic import Spell
from classes.Inventory import Item
import random

#Spells
#Dark magic
fire = Spell("Fire ball", 20, 135, "dark")
meteor = Spell("Meteor", 60, 420, "dark")
blackhole = Spell("Black Hole", 80, 550, "dark")

#Light magic
lightning = Spell("Lightning", 50, 350, "light")
ice = Spell("Blizzard", 30, 220, "light")
wind = Spell("Wirlwind", 10, 75, "light")

#Heal magic
relife = Spell("Relife", 10, 40, "heal")
cura = Spell("Cura", 20, 120, "heal")

#Items
#Potion/elixar
potion = Item("Potion", "potion", "Heals 50 HP", 50)
Hpotion = Item("Hi-potion", "potion", "Heals 150 HP", 150)
Upotion = Item("Ultra-potion", "potion", "Heals 300 HP", 300)
pheoAsh = Item("PheonixAsh-potion", "potion", "Fully restore HP", 99999)
elixar = Item("Elixar", "elixar", "Fully restore both HP/MP", 99999)

#MP potion
MPpotion = Item("MP potion", "Mpotion", "Restore 50 MP", 50)
HMPpotion = Item("High-MP potion", "Mpotion", "Restore 150 MP", 150)

#Dmg
silverRock = Item("Silver-rock", "attack", "Throw to deal 200 physical DMG", 150)

#Player
Pspells = [cura, fire, ice, meteor]
Pitems = [{'item': potion, 'quantity': 2}, {'item': Hpotion, 'quantity': 1}, 
        {'item': elixar, 'quantity': 1}, {'item': pheoAsh, 'quantity': 1},
        {'item': MPpotion, 'quantity': 2}, {'item': silverRock, 'quantity': 5}]
fAIitems = [{'item': potion, 'quantity': 2}, {'item': Hpotion, 'quantity': 1}, 
        {'item': elixar, 'quantity': 1}, {'item': pheoAsh, 'quantity': 1},
        {'item': MPpotion, 'quantity': 2}, {'item': silverRock, 'quantity': 5}]

#Create players and enemie
player = Person('Player', 550, 80, 90, 40, Pspells, Pitems)
fAI = Person('Valorr', 850, 60, 50, 120, Pspells, fAIitems)
enemy = Person('Monster', 2000, 120, 50, 60, [], [])

def checkCrit(entity, outDmg):
    crit = (entity.atkl + entity.atkh)/1.5
    if outDmg > crit:
        return True
    else:
        return False

print('\n\n')
running = True

while running:
    party = [player,fAI]
    for member in party:
        member.get_stats()
    print('_____________________________________________________________________________________________________')
    enemy.get_stats_en()
    for member in party:
        #print(bcolors.FAIL + 'Enemy HP: '+ str(enemy.get_hp()) + '/' + str(enemy.get_maxHp()) + ' Enemy MP: ' + str(enemy.get_mp()) + bcolors.ENDC)
        #print(bcolors.OKGREEN + 'Player HP: '+ str(player.get_hp()) + '/' + str(player.get_maxHp()) + ' Player MP: ' + str(player.get_mp()) + bcolors.ENDC)
        print(bcolors.BOLD + member.name + bcolors.ENDC + "'s turn")
        member.choose_action()
        choice = input('Choose your action: ')

        if choice == 'q':
            print(bcolors.Bg_RED + '==========Quiting==========' + bcolors.Bg_ENDC)
            running = False
            break
        elif choice == '1':
            atkDmg = member.generate_dmg()
            if checkCrit(member, atkDmg) == True:
                print("-- "+member.name+" ATTACK " + bcolors.WARNING + 'CRITICAL HIT! ' + bcolors.WARNING + str(atkDmg) + " Damage!" + bcolors.ENDC)
            else:
                print("-- "+member.name+" ATTACK " + bcolors.FAIL + str(atkDmg) + " Damage!" + bcolors.ENDC)
            enemy.take_dmg(atkDmg)
            print("Enemy has: " + bcolors.Bg_RED + str(enemy.get_hp())+" HP left" + bcolors.Bg_ENDC)
        elif choice == '2':
            member.choose_magic()
            print ('Type ' + bcolors.WARNING + '"b"' + bcolors.ENDC + ' to go back' )
            print(member.name+' have ' + bcolors.HEADER + str(member.get_mp()) + ' MP' + bcolors.ENDC + ' left')
            selMagic = input("Select magic: ")
            if selMagic == 'b' or selMagic == '':
                continue
            
            spell = member.magic[int(selMagic) - 1]
            magicDmg = spell.dmg
            if spell.cost > member.get_mp():
                print("You don't have enough MP")
                continue
            elif spell.type == "heal":
                member.reduce_mp(spell.cost)
                print("-- "+member.name+" CAST " + str(spell.name) + bcolors.OKGREEN + " +" + str(magicDmg) + " HP!" + bcolors.ENDC)
                member.heal(spell.dmg)
                print(member.name+" HP = " + bcolors.OKGREEN + str(member.get_hp()) + "/" + str(member.get_maxHp()) + bcolors.ENDC)
            elif spell.type == "dark":
                member.reduce_mp(spell.cost)
                print("-- "+member.name+" CAST " + str(spell.name) + " " + bcolors.FAIL + str(magicDmg) + " Damage!" + bcolors.ENDC)
                enemy.take_dmg(magicDmg)
                print("Enemy has: " + bcolors.Bg_RED + str(enemy.get_hp())+" HP left" + bcolors.Bg_ENDC)
            elif spell.type == "light":
                member.reduce_mp(spell.cost)
                print("-- "+member.name+" CAST " + str(spell.name) + " " + bcolors.FAIL + str(magicDmg) + " Damage!" + bcolors.ENDC)
                enemy.take_dmg(magicDmg)
                print("Enemy has: " + bcolors.Bg_RED + str(enemy.get_hp())+" HP left" + bcolors.Bg_ENDC)

        elif choice == '3':
            member.choose_item()
            print ('Type ' + bcolors.WARNING + '"b"' + bcolors.ENDC + ' to go back' )
            selItem = input("Choose an item: ")
            if selItem == 'b' or selItem == '':
                continue
            #Check item quantity
            amtItem = member.item[int(selItem) - 1]['quantity']
            if amtItem <= 0:
                print(bcolors.WARNING + '+++++++ |Out of item| +++++++' + bcolors.ENDC)
                continue
            #Use item and reduce the amounnt
            item = member.item[int(selItem) - 1]['item']
            member.reduce_item(int(selItem) - 1)
            #member.item[int(selItem) - 1]['quantity'] -= 1
            if item.type == 'potion':
                member.heal(item.prop)
                print(member.name+" used " + bcolors.LIGHTBLUE + str(item.name) + '!' + bcolors.ENDC)
                print(member.name+" HP: " + bcolors.OKGREEN + str(member.get_hp()) + "/" + str(member.get_maxHp()) + '^' + bcolors.ENDC)
            elif item.type == 'Mpotion':
                member.healMP(item.prop)
                print(member.name+" used " + bcolors.LIGHTBLUE + str(item.name) + '!' + bcolors.ENDC)
                print(member.name+" MP: " + bcolors.OKGREEN + str(member.get_mp()) + "/" + str(member.get_maxMp()) + '^' + bcolors.ENDC)
            elif item.type == 'elixar':
                member.hp = member.maxhp
                member.mp = member.maxmp
                print(member.name+" used " + bcolors.LIGHTBLUE + str(item.name) + '!' + bcolors.ENDC)
                print(member.name+" HP: " + bcolors.OKGREEN + str(member.get_hp()) + "/" + str(member.get_maxHp()) + '^' + bcolors.ENDC)
                print(member.name+" MP: " + bcolors.OKGREEN + str(member.get_mp()) + "/" + str(member.get_maxMp()) + '^' + bcolors.ENDC)
            elif item.type == 'attack':
                itemDmg = member.generate_itemDmg(item.prop)
                enemy.take_dmg(itemDmg)
                print(member.name+" used " + bcolors.FAIL + str(item.name) +' '+ str(itemDmg) +' DMG!' + bcolors.ENDC)
                print("Enemy has: " + bcolors.Bg_RED + str(enemy.get_hp())+" HP left" + bcolors.Bg_ENDC)

        if enemy.get_hp() <= 0:
            print(bcolors.WARNING + bcolors.BOLD + "\nYou've slain the enemy!" + bcolors.ENDC)
            running = False
            break
        else:
            print('\n'+bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)
            enemy_dmg = enemy.generate_dmg()
            randMember = random.choice([player, fAI])
            randMember.take_dmg(enemy_dmg)
            #CHECK CRIT
            if checkCrit(enemy, enemy_dmg) == True:
                print("-- Enemy ATTACK "+bcolors.OKGREEN+randMember.name+ bcolors.WARNING + ' CRITICAL HIT! ' + bcolors.WARNING + str(enemy_dmg) + " Damage!" + bcolors.ENDC)
            else:
                print("-- Enemy ATTACK " + bcolors.OKGREEN + randMember.name+bcolors.FAIL + " " + str(enemy_dmg) + " Damage!" + bcolors.ENDC)
            #PLAYER TAKE DMG
            print(randMember.name+" has: " + bcolors.Bg_BLUE + str(randMember.get_hp()) + " HP Left!" + bcolors.Bg_ENDC)
            if randMember.get_hp() <= 0:
                print(bcolors.FAIL + bcolors.BOLD + "\n ~~~~~ "+randMember.name+" died ~~~~~" + bcolors.ENDC)
                running = False
                break

            '''for member in party:
                if member.hp == 0:
                    print(bcolors.WARNING + '--------- |You Lost| ---------' bcolors.ENDC)
                    running = False'''