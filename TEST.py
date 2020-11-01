import sys
import random
from classes.Inventory import Item
from classes.game import Person

potion = Item('Potion', 'heal', 'Heal', 50)
Mpotion = Item('Potion', 'heal', 'MHeal', 100)
Hpotion = Item('Potion', 'heal', 'HHeal', 150)
knife = Item('Potion', 'dmg', 'Knife', 200)
itm = [{'item': potion, 'quantity': 5},{'item': Mpotion, 'quantity': 3},{'item': Hpotion, 'quantity': 3},{'item': knife, 'quantity': 2}]
def testColor():
    for i in range(1, 107):
        code = str('\033['+str(i)+'m'+str(i) + '\033[0m')
        sys.stdout.write(code + '  ')

def checkItm():
    i = 1
    for things in itm:
        print(str(things['item'].name))

nPerson = Person('Nic',1000,10,10,10,10,itm)
jPerson = Person('Jac',1000,10,10,10,10,itm)
kPerson = Person('Kuk',1000,10,10,10,10,itm)

randPerson = random.choice([nPerson, jPerson, kPerson])
print(randPerson.name)