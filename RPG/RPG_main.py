from RPG_fundamentals import Player, Item, color


# Magic
magic = [{'name': 'Fireball', 'cost': 10, 'dmg': 60},
         {'name': 'Blizzard', 'cost': 30, 'dmg': 140},
         {'name': 'Thunder', 'cost': 25, 'dmg': 125}]

# Items
potion = Item('Potion', 'potion', 'Heals 50 HP', 50)
bpotion = Item('Big Potion', 'potion', 'Heals 100 HP', 100)
mpotion = Item('Mana Potion', 'mpotion', 'Restores 30 MP', 30)
bmpotion = Item('Big Mana Potion', 'mpotion', 'Restores 60 MP', 60)

bomb = Item('Bomb', 'throwable', 'Deals 500 points of damage', 500)

# Characters
player = Player(460, 65, 60, 35, magic, [
                potion, bpotion, mpotion, bmpotion, bomb])
enemy = Player(1200, 45, 40, 40)

# Mechanics
running = True
i = 0

print(color.warning + color.bold + "AN ENEMY ATTACKS!" + color.end)

while running:
    player.pick_action()
    choice = input(color.cyan + '\nPick an action' + color.end)

    print(color.cyan + 'You chose ' + choice + color.end)
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.receive_damage(dmg)
        print(color.cyan + 'You attacked for ' + str(dmg) +
              ' points of damage.' + color.end + 'Enemy HP: ' + str(enemy.get_hp()))
    elif index == 1:
        player.pick_magic()
        magic_choice = int(input('Choose a spell: ')) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_cost(magic_choice)

        current_mp = player.get_mp()
        if magic[magic_choice]['cost'] > current_mp:
            print(color.warning + '\nNot enough MP\n' + color.end)
            continue

        if magic_choice == -1:
            continue

        player.reduce_mp(cost)
        enemy.receive_damage(magic_dmg)
        print(color.blue + spell + ' deals ' + str(magic_dmg) +
              ' points of damage.' + color.end + ' Enemy HP: ' + str(enemy.get_hp()))

    elif index == 2:
        player.pick_item()
        item_choice = int(input('Choose an item: ')) - 1

        if player.items[item_choice]['quantity'] == 0:
            print('None left...')
            continue

        if item_choice == -1:
            continue

        if Item.type == 'potion':
            player.heal(Item.prop)
            print()
        elif Item.type == 'mpotion':
            player.restore(Item.prop)
            print()
        elif Item.type == 'throwable':
            enemy.receive_damage(Item.prop)
            print()
        item = player.items[item_choice]['item']
        player.items[item_choice]['quantity'] -= 1

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.receive_damage(enemy_dmg)
    print(color.warning + 'Enemy attacks for ', enemy_dmg,
          ' points of damage.' + color.end + 'Player HP: ', player.get_hp())

    if enemy.get_hp() == 0:
        print(color.green + "Enemy has been defeated!" + color.end)
        running = False

    elif player.get_hp() == 0:
        print(color.warning + color.bold + "YOU ARE DEAD..." + color.end)
        running = False
