import random


class color:
    purple = '\033[95m'
    cyan = '\033[96m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    warning = '\033[91m'
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'


class Player:
    def __init__(self, hp, mp, atk, df, magic=[], items=[]):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 15
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_damage(self, i):
        mgd = self.magic[i]['dmg']
        return mgd

    def receive_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            hp = 0
        return self.hp

    def heal(self, he):
        self.hp += he

    def restore(self, re):
        self.mp += re

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost
        return self.mp

    def get_spell_name(self, i):
        return self.magic[i]['name']

    def get_spell_cost(self, i):
        return self.magic[1]['cost']

    def pick_action(self):
        i = 1
        print('\n' + color.cyan + 'ACTIONS:\n' + color.end)
        for item in self.actions:
            print('   ' + str(i) + ':' + item)
            i += 1

    def pick_magic(self):
        i = 1
        print('\n' + color.cyan + 'MAGIC:\n' + color.end)
        for spell in self.magic:
            print('   ' + str(i) + ':' + spell['name'] +
                  '(cost:' + str(spell['cost']) + ')')
            i += 1

    def pick_item(self):
        i = 1
        print('\n' + color.cyan + 'ITEMS:\n' + color.end)
        for item in self.items:
            print('   ' + str(i) + '.' + item.name + ':' +
                  item.description + '(', item.quantity, ')')
            i += 1


class Item:
    def __init__(self, name, type, description, prop, quantity=1):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        self.quantity = quantity
