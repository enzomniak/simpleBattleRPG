import random
class bcolors:
    LIGHTBLUE = '\033[96m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    GRAY = '\033[90m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLACK = '\u001b[30;1m'
    #For darker change \u001b[4x;1m to \u001b[4xm
    Bg_BLACK = '\u001b[40;1m'
    Bg_RED = '\u001b[41;1m'
    Bg_GREEN = '\u001b[42m'
    Bg_YELLOW = '\u001b[43;1m'
    Bg_BLUE = '\u001b[44;1m'
    Bg_MAGENTA = '\u001b[45;1m'
    Bg_WHITE = '\u001b[47;1m'
    Bg_ENDC = '\u001b[0m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, item):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 20
        self.atkh = atk + 20
        self.df = df
        self.magic = magic
        self.item = item
        self.action = ["Attck", "Magics", "Items"]
        self.name = name

    def generate_itemDmg(self, itemDmg):
        low = itemDmg - 20
        high = itemDmg + 20
        return random.randrange(low, high)

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def take_dmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def healMP(self, dmg):
        self.mp += dmg
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        
    def get_hp(self):
        return self.hp

    def get_maxHp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxMp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.Bg_BLUE + "====== |Actions| ======" + bcolors.Bg_ENDC + bcolors.ENDC)
        for item in self.action:
            print("   " + str(i) + ".) " + item)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.Bg_WHITE + "====== *Magics* ======" + bcolors.Bg_ENDC + bcolors.ENDC)
        for spell in self.magic:
            print("   " + str(i) + ".) " + str(spell.name) + " cost: " + bcolors.HEADER + str(spell.cost) +bcolors.ENDC)
            i += 1

    def choose_item(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.Bg_WHITE + "====== |Items| ======" + bcolors.Bg_ENDC + bcolors.ENDC)
        for itm in self.item:
            print("   " + str(i) + ".) " + str(itm['item'].name) + ": " + bcolors.Bg_BLACK + bcolors.OKGREEN + str(itm['item'].description)+ ' (x' +str(itm['quantity']) + ')'+ bcolors.Bg_ENDC +bcolors.ENDC)
            i += 1

    def reduce_item(self, index):
        self.item[index]['quantity'] -= 1

    def get_stats(self):
        #HP bar
        hit_point_bar = ""
        hit_point_ticks = (self.hp/self.maxhp) * 100/4
        while hit_point_ticks > 0:
            hit_point_bar += "█"
            hit_point_ticks -= 1
        while len(hit_point_bar) < 25:
            hit_point_bar += " "
        whiteSpaceHP = ""
        if len(str(self.hp)) < len(str(self.maxhp)):
            whiteSpaceHP += " "
        #MP bar
        mp_bar = ""
        mp_ticks = (self.mp/self.maxmp) * 100/10
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "
        whiteSpaceMP = ""
        if len(str(self.mp)) < len(str(self.maxmp)):
            whiteSpaceMP += " "

        print("                      _________________________              __________")
        print(bcolors.BOLD + self.name +":    "+bcolors.ENDC+ whiteSpaceHP + "HP:"+str(self.hp)+"/"+str(self.maxhp)+ 
            "|"+ bcolors.OKGREEN + hit_point_bar+bcolors.ENDC+"|"+
            "    "+"MP:"+whiteSpaceMP+str(self.mp)+"/"+str(self.maxmp)+"|"+bcolors.OKBLUE+mp_bar+bcolors.ENDC+"|")

    def get_stats_en(self):
        #HP bar
        hit_point_bar = ""
        hit_point_ticks = (self.hp/self.maxhp) * 100/2
        while hit_point_ticks > 0:
            hit_point_bar += "█"
            hit_point_ticks -= 1
        while len(hit_point_bar) < 50:
            hit_point_bar += " "
        whiteSpaceHP = ""
        if len(str(self.hp)) < len(str(self.maxhp)):
            whiteSpaceHP += " "
        #MP bar
        mp_bar = ""
        mp_ticks = (self.mp/self.maxmp) * 100/10
        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "
        whiteSpaceMP = ""
        if len(str(self.mp)) < len(str(self.maxmp)):
            whiteSpaceMP += " "

        print("                         __________________________________________________                __________")
        print(bcolors.BOLD + self.name +":    "+bcolors.ENDC+ whiteSpaceHP +"HP:"+str(self.hp)+"/"+str(self.maxhp)+ 
            "|"+ bcolors.FAIL + hit_point_bar+bcolors.ENDC+"|"+
            "    "+"MP:"+whiteSpaceMP+str(self.mp)+"/"+str(self.maxmp)+"|"+bcolors.GRAY+mp_bar+bcolors.ENDC+"|")