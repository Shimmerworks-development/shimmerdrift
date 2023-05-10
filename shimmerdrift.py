import time
import random
import math



#GAME VERSION#######
version = "0.0.1"  #
####################


spell_tutorial = False
melee_tutorial = False
inv=[]
spellbook = []
task=''
location=''

shards = 0


def start_quest(quest):
    global task
    if quest in tasks:
        task = tasks[quest].name
        gap(1)
        print(f"* +< NEW QUEST [{tasks[task].description}] >+ *")
        gap(1)
    else:
        print("XX -> quest not found <- XX")

def complete_quest():
    global task
    gap(1)
    print(f"* +< QUEST COMPLETED [{tasks[task].description}] >+ *")
    gap(1)
    task=''


def gain_shards(amount):
    global shards
    if race=="dwarf":
        amount=round(amount*1.25)
    shards+=amount
    gap(1)
    print(f"++ -> You gained {amount} shards <- ++")
    gap(1)

def buy(item, cost):
    global shards
    if shards >= cost:
        gap(1)
        print("------------------------")
        print(f"** -> You paid {cost} shards for {item} <- **")
        rpint(f'** -> You have {shards} shards remaining <- **')
        shards-=cost
        gain_item(item, 1)
        print("------------------------")
        gap(1)
    else:
        gap(1)
        print("XX -> Not enough shards <- XX")
        gap(1)
    

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
tasks = {
    "arena": Task("arena", "Travel to the great arena and speak to Aphax"),
    "gear": Task("gear", "Travel to the town square and purchase some gear from the weaponsmith"),
    "archive": Task("archive", "Travel to the Grand Archive and research the Cataclysm"),
}

def gap(size):
    for x in range(size):
        print('')

def wait():
    input('⇥ ')

classes = {
    "warrior": {"ATK": 1, "HP": 9, "DESC":"Trained in combat, you are skilled with a blade and tough in the face of battle", "ABILITY":"+20% Damage when using a melee weapon"},
    "mage": {"ATK": 0, "HP": 8, "DESC":"Disciplined in the ways of sorcery, your intelligent use of magic strikes fear into the hearts of your enemies", "ABILITY":"-20% Mana cost for spells"},
    "rogue": {"ATK": 2, "HP": 5, "DESC":"Your agility and cunning allows you to take out your foes with fierce consistency", "ABILITY":""},
    "paladin": {"ATK": 1, "HP": 10, "DESC":"A warrior of the light, you are skilled in both combat and magic, and are a force to be reckoned with", "ABILITY":""},
    "cleric": {"ATK": 0, "HP": 12, "DESC":"A healer of great power, capable of cleansing devastating wounds and restoring life to the fallen", "ABILITY":""},
}

races = {
    "human": {"ATK": 2, "HP": 28, "DESC":"The mundane Human, great learners capable of great things when they put their minds and hearts to it", "ABILITY":"+50% More experience"},
    "elf": {"ATK": 1, "HP": 22, "DESC":"The Nimble Elf, Theyre powers lie in both the magical and physical", "ABILITY":"+60% Damage dealt by spells"},
    "dwarf": {"ATK": 2, "HP": 30, "DESC":"The humble Dwarf, beings of great strength who live in the darkest depths of the realm", "ABILITY":"+25% More shards"},
    "halfling": {"ATK": 0, "HP": 26, "DESC":"The miniscule and nimble Halfling, they are skilled in the art of stealth and make adept pickpockets", "ABILITY":"Higher chance of escaping from a fight, gains a small amount of experience when escaping"},
    "dragonborn": {"ATK": 1, "HP": 24, "DESC":"The mighty Dragonborn, children of the great dragons of the realm, they are created with a great spark of draconic power", "ABILITY":"Critical hits 100% of the time"},

}

starting_gear = {
    "warrior": ["common shortsword", "potion of healing", "common iron armor"],
    "mage": ["common mage staff", "common silver robes", 'spellbook', 'potion of mana'],
    "rogue": ["uncommon dagger", "common leather armor"],
    "paladin": ["common hammer", "spellbook", "common pearl robes"],
    "cleric": ["common dagger","potion of healing", "common pearl robes", "spellbook"],
}

class Spell:
    def __init__(self, name, description, stats, mana_cost):
        self.name = name
        self.description = description
        self.stats = stats
        self.mana_cost = mana_cost

    def display(self):
        return f"[{spells[self].name}: {spells[self].description}] [Damage: {spells[self].stats['ATK']}] [Mana Cost: {spells[self].mana_cost}]"

spells = {
    "ice shard": Spell("Ice Shard", "Shoots a high velocity shard of ice at your enemy", {"ATK": 1}, 0),
    "lightning bolt": Spell("Lightning Bolt", "Releases a devastating bolt of lightning towards your enemy", {"ATK": 3}, 3),
    "fireball": Spell("Fireball", "Fires an array of blazing fireballs at your enemy causing great damage", {"ATK": 5}, 6),
    "healing hands": Spell("Healing Hands", "A healing spell, allows you to regain a small amount of your life", {"HP": 5}, 2),
    "cleansing shot": Spell("Cleansing Shot", "Shoots pure bullet of power at an enemy", {"ATK": 2}, 0),
    "light blast": Spell("Light Blast", "Creates a bright flash of purest light in all directions damaging all it hits", {"ATK": 3}, 3),
}

attack_spells = {
    "ice shard": Spell("Ice Shard", "Shoots a high velocity shard of ice at your enemy", {"ATK": 1}, 0),
    "lightning bolt": Spell("Lightning Bolt", "Releases a devastating bolt of lightning towards your enemy", {"ATK": 3}, 3),
    "fireball": Spell("Fireball", "Fires an array of blazing fireballs at your enemy causing great damage", {"ATK": 5}, 6),
    "cleansing shot": Spell("Cleansing Shot", "Shoots pure bullet of power at an enemy", {"ATK": 2}, 0),
    "light blast": Spell("Light Blast", "Creates a bright flash of purest light in all directions damaging all it hits", {"ATK": 3}, 3),
}

utility_spells = {
    "healing hands": Spell("Healing Hands", "A healing spell, allows you to regain a small amount of your life", {}, 2),
}

starting_spells = {
    "mage": ["ice shard", "lightning bolt", "fireball"],
    "cleric": ["healing hands", "cleansing shot", "light blast"],
    "paladin": ["lighning bolt", "cleansing shot", "light blast"]
}

starting_weapon = {
    "warrior": "common shortsword",
    "mage": "common mage staff",
    "rogue": "uncommon dagger",
    "paladin": "common hammer",
    "cleric": "common dagger",
}

starting_armor = {
    "warrior": "common iron armor",
    "mage": "common silver robes",
    "rogue": "common leather armor",
    "paladin": "common pearl robes",
    "cleric": "common pearl robes",

}

class Weapon:
    def __init__(self, name, description, stats, use):
        self.name = name
        self.description = description
        self.stats = stats
        self.use = use

    def display(self):
        print(f"[Weapon - {self.name}: {self.description} Attack: +{self.stats['ATK']}]")

weapons = {
    "common shortsword": Weapon("Common Shortsword", "A relativley short blade, but it's sharpness and weight make it a somewhat deadly weapon", {"ATK": 4}, "none"),
    "common dagger": Weapon("Common Dagger", "A miniscule blade, deals little to no damage, but a precise strike may deliver a killing blow", {"ATK": 3}, "none"),
    "common mage staff": Weapon("Common Mage Staff", "A long wooden stick with a blue jewel at it's head, it's magical properties make it a powerful tool and weapon alike", {"ATK": 3}, "none"),
    "common hammer": Weapon("Common Hammer", "A large hammer, it's weight makes it hard to wield, but it's destructive strike makes it a deadly weapon", {"ATK": 4}, "none"),
    "uncommon dagger": Weapon("Uncommon Dagger", "A miniscule blade, deals little to no damage, but a precise strike may deliver a killing blow", {"ATK": 5}, "none"),
}

class Armor:
    def __init__(self, name, description, stats, use):
        self.name = name
        self.description = description
        self.stats = stats
        self.use = use

    def display(self):
        print(f"[Armor - {self.name}: {self.description} Defense: +{self.stats['DEF']}]")

armors = {
    "common silver robes": Armor("Common Silver Robes", "A set of robes made from the finest silver, they are light and flexible, but offer little protection", {"DEF": 1}, "none"),
    "common pearl robes": Armor("Common Pearl Robes", "A set of robes made from the whitest silk, offers extremley ranged movement, provides extremely little protection", {"DEF": 1}, "none"),
    "common iron armor": Armor("Common Iron ", "A heavy iron set, it's weight makes it hard to move in, but it's sturdy construction makes it hard to break", {"DEF": 3}, "none"),
    "common leather armor": Armor("Common Leather Armor", "A set of leather armor, it's light weight makes it easy to move in, but it's weak construction makes it easy to break", {"DEF": 2}, "none"),
    }

class Item:
    def __init__(self, name, description, stats, use):
        self.name = name
        self.description = description
        self.stats = stats
        self.use = use

    def display(self):
        print(f"[Item - {self.name}: {self.description}]")

items = {
    "spellbook": Item("Spellbook", "A book containing the secrets of the arcane arts, it's pages are filled with spells that can be used to aid you in battle", {}, "none"),
    "potion of healing": Item("Potion of Healing", "A small vial filled with a mysterious liquid, it's healing properties can restore your health", {"HP": 5},"heal5"),
    "potion of mana": Item("Potion of Mana", "A small vial filled with a mysterious liquid, it's magical properties can restore your mana", {"MANA": 5},'mana5'),
    "mysterious jewel": Item("Mysterious Jewel", "A small blue crystal bestowed upon you by the mysterious being, it can be used at any time", {}, "jewel"),

    "common shortsword": Weapon("Common Shortsword", "A relativley short blade, but it's sharpness and weight make it a somewhat deadly weapon", {"ATK": 4}, "none"),
    "common dagger": Weapon("Common Dagger", "A miniscule blade, deals little to no damage, but a precise strike may deliver a killing blow", {"ATK": 3}, "none"),
    "common mage staff": Weapon("Common Mage Staff", "A long wooden stick with a blue jewel at it's head, it's magical properties make it a powerful tool and weapon alike", {"ATK": 3}, "none"),
    "common hammer": Weapon("Common Hammer", "A large hammer, it's weight makes it hard to wield, but it's destructive strike makes it a deadly weapon", {"ATK": 4}, "none"),
    "uncommon dagger": Weapon("Uncommon Dagger", "A miniscule blade, deals little to no damage, but a precise strike may deliver a killing blow", {"ATK": 5}, "none"),

    "common silver robes": Armor("Common Silver Robes", "A set of robes made from the finest silver, they are light and flexible, but offer little protection", {"DEF": 1}, "none"),
    "common pearl robes": Armor("Common Pearl Robes", "A set of robes made from the whitest silk, offers extremley ranged movement, provides extremely little protection", {"DEF": 1}, "none"),
    "common iron armor": Armor("Common Iron ", "A heavy iron set, it's weight makes it hard to move in, but it's sturdy construction makes it hard to break", {"DEF": 3}, "none"),
    "common leather armor": Armor("Common Leather Armor", "A set of leather armor, it's light weight makes it easy to move in, but it's weak construction makes it easy to break", {"DEF": 2}, "none"),
}

key_items = {
    "mysterious jewel": Item("Mysterious Jewel", "A small blue crystal bestowed upon you by the mysterious being, it can be used at any time", {}, "jewel"),
}

def use(item):
    global hp, mana, max_hp, max_mana, inv
    if item in inv:
        if item in items:
            if items[item].use == "heal5":
                hp += 5
                print("You gulp down the vial of liquid, you feel your vitality return to you")
                gap(1)
                print('^^ -> HP +5 <- ^^')
                if hp > max_hp:
                    hp = max_hp
                print(f"<- [ HP: {hp}/{max_hp} ] ->")
                gap(1)
                inv.remove(item)
            elif items[item].use == "mana5":
                mana += 5
                print("You gulp down the vial of liquid, you feel the mana flowing through your veins")
                gap(1)
                print('^^ -> MANA +5 <- ^^')
                if mana > max_mana:
                    mana = max_mana
                print(f"<- [ MANA: {mana}/{max_mana} ] ->")
                gap(1)
                inv.remove(item)
            elif items[item].use == "jewel":
                print("You hold the jewel in your hand, and it radiates with a curious energy you can quite put your finger on")
                gap(1)
            
            elif items[item].use == "none":
                print("XX -> that item cannot be used <- XX")
        
class Location:
    def __init__(self, name, description, characters, enemies):
        self.name = name
        self.description = description
        self.characters = characters
        self.enemies = enemies

locations = {
  "The Summoning Fractal": Location("The Summoning Fractal", "The main attraction in the great city of Solacia, Every thousand years it produces a great avatar to protect the realm.", ["Rodor"], []),
  "The Great Arena": Location("The Great Arena", "Another landmark of solacia, a place for great warriors to train their skills in battle, the arena provides an accesible area for consistently battling against enemies.", ["Aphax"], ['Ooze', 'Goblin', "Magma Goblin"]),
  "The Grand Archive": Location("The Grand Archive", "An expansive network of documents reciting eons of fortune and tragedy.", ["Unnamed Historian"], ["Bookworm"]),
  "Town Square": Location("Town Square", "The centerpoint of Solacia, a bustling hub of activity, the town square is the perfect place to rest and spend shards.", ["Theodore"], []),
}

def display_location(location):
    gap(4)
    print("------------------------------------")
    print(f"Location: {locations[location].name}")
    print(f"{locations[location].description}")
    if locations[location].characters != []:
        print("Characters:")
        for character in locations[location].characters:
            print(f"-> {character}")
    if locations[location].enemies != []:
        print("Possible Enemies:")
        for enemy in locations[location].enemies:
            print(f"-> {enemy}")
    print("------------------------------------")
    gap(4)

class Enemy:
    def __init__(self, name, description, stats, amsg, level):
        self.name = name
        self.description = description
        self.stats = stats
        self.amsg = amsg
        self.level = level


    def display(self):
        print(f"[Enemy - {self.name}: {self.description}]")

enemies = {
    "Bookworm": Enemy("Bookworm", "", {"ATK": 0, "HP": 1}, 'The Bookworm feebly attempts to nibble on your finger', 1),
    "Ooze": Enemy("Ooze", "A small green, and slimy creature, incredibly easy to destroy", {"ATK": 1, "HP": 7}, 'The Ooze lunges at you with a slimy psuedopod', 1),
    "Goblin": Enemy("Goblin", "A small red, and ugly creature", {"ATK": 3, "HP": 16}, 'The Goblin jumps forwards at you, taking a stab with a rusted dagger', 2),
    "Magma Goblin": Enemy("Magma Goblin", "A small red, and ugly creature, it's skin is covered in magma, and it's eyes are filled with fire", {"ATK": 4, "HP": 21, "DEF": 1}, 'The Magma Goblin leaps forward and takes a slash at you with a blackened claw', 3),
    "Orc": Enemy("Orc", "A giant beast of magnificent proportions, beware it's deadly club swing", {"ATK": 5, "HP": 34}, 'The Orc swings his mighty club toward you', 4),
    "Giant Spider": Enemy("Giant Spider", "A ravenous arachnid, it's terrifying fangs are nearly always deadly", {"ATK": 6, "HP": 48}, 'The Giant Spider launches itself at you, its fangs dripping with venom', 5),
    "Dragon": Enemy("Dragon", "A massive beast of fire and fury, stay well away from it's deadly breath", {"ATK": 12, "HP": 160}, 'The Dragon swoops through the air at you, leaving a deadly stream of fire in its wake', 9),
}

class Boss:
    def __init__(self, name, description, stats, amsg):
        self.name = name
        self.description = description
        self.stats = stats
        self.amsg = amsg

def gain_item(item_name, quantity):
    if item_name in items:
        inv.append(item_name)

        if quantity > 1:
            print(f"++ -> gained {item_name} x{quantity}<- ++")
        else:
            if item_name in key_items:
                print(f"++ -> gained key item: {item_name} <- ++")
            else:
                print(f"++ -> gained {item_name} <- ++")
    else:
        print(f"XX -> {item_name} is not a valid item <- XX")

def level_up():
    global lvl, xp, max_hp, max_mana, hp, mana, weapon, armor, spell_choice, xp_tolvlup
    while xp >= xp_tolvlup:
        current_level = lvl
        lvl+=1
        new_level = lvl
        xp-=xp_tolvlup
        xp_tolvlup=round(xp_tolvlup*1.15)
        max_hp = round(max_hp*1.2)
        if "spellbook" in inv:
            max_mana = round(max_mana*1.2)
        gap(1)
        print(f"^^ -> LEVEL UP! <- ^^")
        print(f"{current_level} -> {new_level}")
        gap(1)

spell_choice=''

def fight(enemy_name):
    global hp, weapon, armor, spell_choice, mana, xp, xp_tolvlup, lvl, max_hp, max_mana, allow_escape, inv, spellbook, spell_tutorial, melee_tutorial, spell_tutorial_explain
    if enemy_name in enemies:
        enemy = enemies[enemy_name]
        enemy.display()
        starting_e_hp=enemy.stats["HP"]
        enemy_hp = enemy.stats["HP"]
        allow_escape = True
        while enemy_hp > 0:
            print("            [FIGHT INFO]")
            gap(2)
            print("ENEMY:")
            print(f"    -[ HP: {enemy_hp}/{starting_e_hp} ]-")
            gap(2)
            print("YOU")
            gap(2)
            if 'spellbook' in inv:
                print(f"    -[ mana: {mana}/{max_mana} ]-")
            print(f"    -[ HP: {hp}/{max_hp} ]-")
            print(f"    -[ DEF: {armors[armor].stats['DEF']} ]-")
            gap(1)
            print(f"    -[ weapon: {weapon} ]-")
            print(f"    -[ armor: {armor} ]-")
            gap(4)
            print("            [FIGHT OPTIONS]")
            print("    -[ melee attack  (Q)        ]-")
            if 'spellbook' in inv:
               print("    -[ magic attack  (W)        ]-")
            if allow_escape: 
                print("    -[ attempt to run away  (E) ]-")
            print("    -[ use item  (R)            ]-")
            gap(2)
            f_option = ''
            if 'spellbook' in inv:
                while f_option not in ["q", "w", "e", "r"]:
                    f_option = input("fight choice > ").lower()
            else:
                while f_option not in ["q", "e", "r"]:
                    f_option = input("fight choice > ").lower()




            if f_option == "q":
                if spell_tutorial == True:
                    print("[Aphax] > You already know how to attack with your weapon, try using a spell instead.")
                    gap(2)
                    wait()
                    gap(2)
                else:
                    gap(4)
                    print(f"!! -> you attack the {enemy_name} with your {weapon} <- !!")

                    if race == "dragonborn":
                        damage = random.randint(round(base_atk + weapons[weapon].stats["ATK"]*1.5), round(base_atk + weapons[weapon].stats["ATK"]*1.7))
                    else:
                        damage = random.randint(base_atk + weapons[weapon].stats["ATK"], round(base_atk + weapons[weapon].stats["ATK"]*1.7))
                    
                    wait()
                    if damage >= round(base_atk + weapons[weapon].stats["ATK"]*1.5):
                        print("!! -> CRITICAL HIT <- !!")
                    if class_u == "warrior":
                        damage = round(damage*1.2)
                    enemy_hp -= damage
                    print(f"!! -> dealt {damage} damage to the {enemy_name} <- !!")
                    if enemy_hp <= 0:
                        print(f"!! -> the {enemy_name} has been defeated <- !!")
                        gap(2)
                        xp_gain = random.randint(enemy.level*3, round(enemy.level*8.5))
                        if race == "human":
                            xp_gain = round(xp_gain*1.5)
                        print(f"!! -> gained {xp_gain} experience <- !!")
                        xp += xp_gain
                        level_up()
                        progress = (xp / xp_tolvlup) * 100
                        filled_segments = int(progress / 100 * 40)
                        empty_segments = 40 - filled_segments
                        progress_bar = '[ ' + '▣' * filled_segments + '□' * empty_segments + ' ]'
                        print(f"current level: {lvl}")
                        print(f"EXP: {xp} / {xp_tolvlup}")
                        print(progress_bar)
                        wait()
                        break
                    
                    print(f"!! -> {enemy.amsg} <- !!")
                    damage = random.randint(enemy.stats["ATK"], round(enemy.stats["ATK"]*1.7))
                    if damage >= round(enemy.stats["ATK"]*1.5):
                        print("!! -> CRITICAL HIT <- !!")
                    hp -= damage
                    print(f"!! -> the {enemy_name} dealt {damage} damage to you <- !!")
                    if hp <= 0:
                        print(f"!! -> you have been defeated by the {enemy_name} <- !!")
                        print("☠︎︎☠︎︎ -> GAME OVER <- ☠︎︎☠︎︎")
                        quit()
                    wait()
                    gap(4)
            



            elif f_option == "w":
                if melee_tutorial == True:
                    gap(4)
                    print('[Aphax] > Not yet! You must first learn how to fight with your weapon')
                    gap(4)
                    wait()
                    gap(6)
                else:

                    if 'spellbook' in inv:
                        if spell_tutorial_explain == True:
                            gap(1)
                            print("[Aphax] > When in a battle such this as you can cast spells to damage your enemies.")
                            wait()
                            print("[Aphax] > Each spell has a mana cost, if you cant meet that cost you are unable to cast it.")
                            time.sleep(1)
                            print("[Aphax] > However if you can, the spell will be cast and that much mana will be drained.")
                            wait()
                            print("[Aphax] > If you wish to restore your mana to its maximum, you may rest when no longer in a battle.")
                            time.sleep(1)
                            print("[Aphax] > You can also use mana potions to restore mana while fighting, however they are limited.")
                            gap(2)
                            time.sleep(1)
                            print("[Aphax] > Now, lets try casting a spell!")
                            spell_tutorial_explain = False
                        gap(4)
                        print(f"             ꩜꩜ -> choose a spell to cast <- ꩜꩜")
                        
                        



                        gap(1)
                        for spell in spellbook:
                            if spell in attack_spells:
                                print(f"    ⋆˖⁺‧₊ {Spell.display(spell)} ₊‧⁺˖⋆")
                        gap(1)
                        spell_choice = input("spell choice > ").lower()
                        while spell_choice not in spellbook:
                            spell_choice = input("spell choice > ").lower()
                        if spell_choice in spellbook:
                            if spell_choice in attack_spells:
                                if spells[spell_choice].mana_cost <= mana:
                                    spell = spell_choice
                                    mana_to_use = spells[spell].mana_cost
                                    if class_u == "mage":
                                        mana_to_use = round(mana_to_use*0.8)
                                        
                                    mana -= mana_to_use
                                    print(f"꩜꩜ -> spent {mana_to_use} mana <- ꩜꩜")
                                    print(f"꩜꩜ -> mana remaining: {mana} <- ꩜꩜")
                                    print(f"!! -> you cast {spells[spell].name} at the {enemy_name} <- !!")
                                    wait()
                                    damage = random.randint(base_atk + spells[spell].stats["ATK"], round(base_atk + spells[spell].stats["ATK"]*1.7))
                                    if damage >= round(base_atk + spells[spell].stats["ATK"]*1.5):
                                        print("!! -> CRITICAL HIT <- !!")
                                    if race == "elf":
                                        damage = round(damage*1.6)
                                    enemy_hp -= damage
                                    print(f"!! -> dealt {damage} damage to the {enemy_name} <- !!")
                                    if enemy_hp <= 0:
                                        print(f"!! -> the {enemy_name} has been defeated <- !!")
                                        gap(2)
                                        xp_gain = random.randint(enemy.level*3, round(enemy.level*8.5))
                                        if race == "human":
                                            xp_gain = round(xp_gain*1.5)
                                        print(f"!! -> gained {xp_gain} experience <- !!")
                                        xp += xp_gain
                                        level_up()
                                        progress = (xp / xp_tolvlup) * 100
                                        filled_segments = int(progress / 100 * 40)
                                        empty_segments = 40 - filled_segments
                                        progress_bar = '[ ' + '▣' * filled_segments + '□' * empty_segments + ' ]'
                                        print(f"current level: {lvl}")
                                        print(f"EXP: {xp} / {xp_tolvlup}")
                                        print(progress_bar)
                                        wait()
                                        break
                                    wait()
                                    print(f"!! -> {enemy.amsg} <- !!")
                                    damage = random.randint(enemy.stats["ATK"], round(enemy.stats["ATK"]*1.7))
                                    if damage >= round(enemy.stats["ATK"]*1.5):
                                        print("!! -> CRITICAL HIT <- !!")
                                    hp -= damage
                                    print(f"!! -> the {enemy_name} dealt {damage} damage to you <- !!")
                                    if hp <= 0:
                                        print(f"!! -> you have been defeated by the {enemy_name} <- !!")
                                        gap(1)
                                        print("☠︎︎☠︎︎ -> GAME OVER <- ☠︎︎☠︎︎")
                                        quit()
                                    gap(4)
                                else:
                                    print("꩜꩜ -> you do not have enough mana to cast that spell <- ꩜꩜")
                                    gap(4)
            elif f_option == "e":
                if melee_tutorial == True:
                    gap(4)
                    print('[Aphax] > Not yet! You must first learn how to fight with your weapon')
                    gap(4)
                    wait()
                    gap(6)
                
                else:
                    if spell_tutorial == True:
                        gap(4)
                        print('[Aphax] > Not yet! You must first learn how to cast spells.')
                        gap(4)
                        wait()
                        gap(6)
                    else:
                        if allow_escape:
                            print("!! -> you attempt to run away <- !!")
                            time.sleep(1)
                            a=random.randint(1, enemy.level+1)
                            if race == "halfling":
                                escape_range = [1,2,3,4]
                            else:
                                escape_range = [1]
                            if a not in escape_range: 
                                print("!! -> you failed to escape <- !!")
                                allow_escape = False
                                time.sleep(1)
                                print(f"!! -> {enemy.amsg} <- !!")
                                damage = random.randint(enemy.stats["ATK"], round(enemy.stats["ATK"]*1.7))
                                if damage >= round(enemy.stats["ATK"]*1.5):
                                    print("!! -> CRITICAL HIT <- !!")
                                hp -= damage
                                print(f"!! -> the {enemy_name} dealt {damage} damage to you <- !!")
                                if hp <= 0:
                                    print(f"!! -> you have been defeated by the {enemy_name} <- !!")
                                    print("☠︎︎☠︎︎ -> GAME OVER <- ☠︎︎☠︎︎")
                                    quit()
                                gap(4)
                            else:
                                print("!! -> you successfully escaped <- !!")
                                if race == "halfling":
                                    gap(1)
                                    xp_gain = random.randint(enemy.level, round(enemy.level*2))
                                    print(f"!! -> gained {xp_gain} experience <- !!")
                                    xp += xp_gain
                                    level_up()
                                    progress = (xp / xp_tolvlup) * 100
                                    filled_segments = int(progress / 100 * 40)
                                    empty_segments = 40 - filled_segments
                                    progress_bar = '[ ' + '▣' * filled_segments + '□' * empty_segments + ' ]'
                                    print(f"current level: {lvl}")
                                    3
                                    print(f"EXP: {xp} / {xp_tolvlup}")
                                    print(progress_bar)
                                    gap(1)
                                    wait()

                                gap(4)
                                break
                        else:
                            print("!! -> you cannot escape now <- !!")
                            gap(4)
            elif f_option == "r":
                if melee_tutorial == True:
                    gap(4)
                    print('[Aphax] > Not yet! You must first learn how to fight with your weapon')
                    gap(4)
                    wait()
                    gap(6)
                else:
                    if spell_tutorial == True:
                        gap(4)
                        print('[Aphax] > Not yet! You must first learn how to cast spells.')
                        wait()
                        gap(6)
                    else:
                        gap(4)
                        print(" - Inventory - ")
                        for item in inv:
                            print(f"{item}")
                        print(" -           - ")
                        gap(1)
                        item_choice=''
                        while item_choice not in items:
                            item_choice = input("item choice > ").lower()
                        use(item_choice)
            


                        
            

                




    else:
        print(f"Error: {enemy_name} is not a valid enemy.")
    
class Character:
    def __init__(self, name, description, stats):
        self.name = name
        self.description = description
        self.stats = stats

    def meet(self):
        print(f"[Character discovered! - {self.name}: {self.description}, ATK: {self.stats['ATK']}, HP: {self.stats['HP']}]")

characters = {
    "Rodor": Character("Rodor", "Guardian of the Summoning Fractal, he is a powerful warrior who has sworn to protect the fractal at any cost.", {"ATK": 56, "HP": 620}),
    "Aphax": Character("Aphax", "Keeper of the great arena.", {"ATK": 42, "HP": 528}),
    "Unnamed Historian": Character("Unnamed Historian", "A visitor of the Grand Archive, they may hold valuable knowledge of days long forgotten...", {"ATK": 2, "HP": 17}),
    "Theodore": Character("Theodore", "A tourist from the city of Atria, he is here to see the fractal for himself.", {"ATK": 0, "HP": 23}),
}

def cont(query, options):
    options_str = "/".join(options)
    gap(1)
    cont_input = input(f"{query} [{options_str}] >")
    while cont_input.lower() not in options:
        gap(1)
        cont_input = input(f"{query} [{options_str}] >")
    return cont_input

def choose_race():
    global race_choice, chosen_race
    print("Pick a race for your avatar to call its own")
    gap(1)
    for i, r in enumerate(races):
      gap(1)
      print("--------------------------------")
      print(r)
      gap(1)
      print(races[r]['DESC'])
      gap(1)
      print(f"[ ATK > +{races[r]['ATK']} ] [ HP > +{races[r]['HP']} ]")
      print(f"[ ABILITY - {races[r]['ABILITY']} ]")
      print("--------------------------------")
      gap(1)
      wait()
    while race_choice.lower() not in races:
      race_choice = input("race >").lower()
    print(f'are you sure you want to pick {race_choice}? [y/n]')
    confirm=''
    while confirm not in ['y','n']:
      confirm=input("y/n >").lower()
    if confirm == "n":
        gap(6)
        race_choice = ""
        choose_race()
    else:
        gap(1)
        chosen_race = race_choice
    
def choose_class():
    global class_choice, chosen_class
    print("Pick a class from which your avatar will learn its skills")
    gap(1)
    for i, c in enumerate(classes):
        gap(1)
        print("--------------------------------")
        print(c)
        gap(1)
        print(classes[c]['DESC'])
        gap(1)
        print(f"[ ATK > +{classes[c]['ATK']} ] [ HP > +{classes[c]['HP']} ]")
        print("--------------------------------")
        gap(1)
        wait()
    while class_choice.lower() not in classes:
      class_choice = input("class >").lower()
    print(f'are you sure you want to pick {class_choice} [y/n]')
    confirm=''
    while confirm not in ['y','n']:
      confirm=input("y/n >").lower()
    if confirm == "n":
        gap(6)
        class_choice = ""
        choose_class()
    else:
        gap(1)
        chosen_class = class_choice
        print(f'class chosen > {chosen_class}')

def rest(length):
    global mana, max_mana, hp, max_hp
    print('ᶻ 𝗓 𐰁  resting  𐰁 𝗓 ᶻ')
    time_left=length
    for x in range (length):
        time.sleep(1)
        time_left-=1
        print(f'{time_left} seconds left')
    gap(4)


    print('rest complete')
    if 'spellbook' in inv:
        mana+=max_mana-mana
    hp+=max_hp-hp
    gap(1)
    print('------------------------------------')
    if 'spellbook' in inv:
        print(f'ᶻ 𝗓 𐰁 mana restored to [{mana}/{max_mana}]  𐰁 𝗓 ᶻ')
    print(f'ᶻ 𝗓 𐰁 hp restored to [{hp}/{max_hp}]  𐰁 𝗓 ᶻ')
    print('------------------------------------')
    gap(1)

def continual_options():
    global action, inv, armor, weapon, j
    print('------------------------------------')
    print('           =+ ACTIONS +=')
    gap(1)
    print('> rest [rest]')
    print('> check your self [check]')
    print('> switch armor/weapon [equip]')
    print('> use item [use]')
    #if "omnimap" in inv:
        #print('> use omnimap [omni]')
    #else:
        #print('> use map [map]')
    print('> journey [↪]')
    gap(1)
    print('------------------------------------')
    gap(1)
    action=input('action >').lower()
    while action not in ['rest','check','equip','use','omni','map','', ' ']:
        action=input('action >').lower()
    if action == 'rest':
        rest(15)
    elif action == 'check':
        check()
    elif action == 'equip':
        gap(2)
        print(" - Inventory - ")
        for item in inv:
            print(f"{item}")
        print(" -           - ")
        gap(2)
        item_to_equip = input("item >").lower()
        while item_to_equip not in inv:
            while item_to_equip not in armors:
                while item_to_equip not in weapons:
                    item_to_equip = input("item >").lower()
        equip(item_to_equip)
    elif action == 'use':
        gap(2)
        print(" - Inventory - ")
        for item in inv:
            print(f"{item}")
        print(" -           - ")
        gap(2)
        item_to_use = input("item >").lower()
        while item_to_use not in inv:
            while item_to_use not in items:
                item_to_use = input("item >").lower()
        use(item_to_use)
    #elif action == 'omni':
        #omnimap()
    #elif action == 'map':
        #map()
    elif action == '' or action == ' ':
        j= 1

def check():
    gap(4)
    print(" - Inventory - ")
    for item in inv:
        print(f"{item}")
    print(" -           - ")
    wait()
    gap(1)
    if "spellbook" in inv:
        print(" - spellbook - ")
        for spell in spellbook:
            print(f"{spell}")
        print(" -           - ")
        gap(1)
        wait()
    print(" - stats - ")
    print(f"health: {hp}/{max_hp}")
    if "spellbook" in inv:
        print(f"mana: {mana}/{max_mana}")
    print(f"total attack: {base_atk+weapons[weapon].stats['ATK']}")
    print(f"defence: {armors[armor].stats['DEF']}")
    print(" -       - ")
    wait()
    gap(1)
    print(" - Equipped - ")
    print(f"weapon: {weapon}")
    print(f"armor: {armor}")
    print(" -          - ")
    wait()
    gap(3)
    print(" - Status - ")
    print(f"quest: {tasks[task].description}")
    print(f"shards: {shards}")
    print(f"level: {lvl}")
    progress = (xp / xp_tolvlup) * 100
    filled_segments = int(progress / 100 * 40)
    empty_segments = 40 - filled_segments
    progress_bar = '[ ' + '▣' * filled_segments + '□' * empty_segments + ' ]'
    print(f"EXP: {xp} / {xp_tolvlup}")
    print(progress_bar)
    print(" -        - ")
    wait()
    gap(4)

def encounter(power, size):
    global lvl
    on_lvl_enemies=[]
    possible_enemies=[]
    things_to_fight=[]
    for enemy in enemies:
        if enemies[enemy].level <= power:
            on_lvl_enemies.append(enemy)
    for enemy in on_lvl_enemies:
        if enemy in locations[location].enemies:
            possible_enemies.append(enemy)
    p_size = random.randint(size, round(size*1.8))
    for x in range(p_size):
        thing_to_fight=random.choice(possible_enemies)
        things_to_fight.append(thing_to_fight)
    gap(1)
    print('------------------------------------')
    gap(1)
    print('!! -> enemy encounter <- !!')
    gap(1)
    print(f'Size: {p_size}')
    print(f'Power: {power}')
    gap(1)
    for enemy in things_to_fight:
        print(f"> {enemy}")
    
    gap(1)
    print('------------------------------------')
    wait()
    gap(4)
    for enemy in things_to_fight:
        gap(6)
        fight(enemy)
    gap(1)
    print('------------------------------------')
    print('✧✧ -> defeated encounter<- ✧✧')
    print('------------------------------------')
    gap(3)

def equip(item):
    global armor, weapon, inv, weapons, armors
    if item in inv:
        if item in weapons:
            if weapon != item:
                weapon = item
                print(f"equipped {item} as weapon")
                gap(1)
        if item in armor:
            if armor != item:
                armor = item
                print(f"equipped {item} as armour")
                gap(1)

def learn_spell(spell):
    if spell in spells:
        if spell not in spellbook:
            spellbook.append(spell)
            gap(1)
            print(f". *･｡✧⁺ committed {spell} to spellbook✧⁺｡･* .")
            gap(1)
        else:
            gap(1)
            print(f"you already know {spell}")
            gap(1)

def journey():
    global j, task, xp, xp_tolvlup, lvl, hp, mana, base_atk, max_hp, max_mana, armor, weapon, inv, spellbook, spells, weapons, armors
    j=0
    while j != 1:
        continual_options()
    j=0



race_choice = ""
class_choice = ""



                                                                       ############ GAME START ############


print (f"                                                          welcome to shimmerdrift v{version}                     ")
gap(6)
syntax=input("view syntax? (reccomended for new players) [y/↪] >").lower()
if syntax == 'y':
    print("↪ = enter")
    print("y = yes")
    print("n = no")
gap(6)

print('[Mysterious Being] > Hello there, I have been expecting you.')
time.sleep(1)
gap(1)
print('[Mysterious Being] > Come.')
time.sleep(1)
choice=cont('go with mysterious being', ['y','n'])
while choice == 'n':
    gap(1)
    print('[Mysterious Being] > Come.')
    choice=cont('go with mysterious being', ['y','n'])
if choice == 'y':
    gap(1)
    print('[Mysterious Being] > I am glad you have decided to join me')
    time.sleep(1)
print('[Mysterious Being] > The realm is in a state of grave peril, and I fear you may be the only one who can help it')
time.sleep(1)
print('[Mysterious Being] > But first, I do not yet know your name?')
gap(1)
name_confirm = ''
while name_confirm != 'y':
    player_name = input("name >")
    name_confirm = cont('is this correct? ' + player_name, ['y','n'])
    if name_confirm == 'n':
        gap(1)
        print('[Mysterious Being] > Very well, try again.')
        gap(1)
gap(1)
print(f'[Mysterious Being] > {player_name}, is it? A fine name indeed.')
time.sleep(1)
print('[Mysterious Being] > Now, I must hold you just a moment longer, your final tasks before descending to the great land of Adria will be to choose the specialties of your avatar.')
time.sleep(1)
print('[Mysterious Being] > What race will you choose, I wonder.')
time.sleep(1)
gap(1)
choose_race()
gap(1)
print(f'[Mysterious Being] > Ah, the {chosen_race}, a noble choice.')
time.sleep(1)
print('[Mysterious Being] > Now, what class will it be.')
gap(1)
choose_class()
gap(1)
print(f'[Mysterious Being] > The {chosen_class}, a powerful skill set indeed.')
time.sleep(2)
gap(1)
print('[Mysterious Being] > I am afraid it is time for you to depart, a great darkness is approaching, and I fear it will soon be too late to stop it.')
print('[Mysterious Being] > Here, take this jewel, it has no purpose as of yet, but it may prove useful in the future.')
time.sleep(1)
gap(1)
gain_item('mysterious jewel', 1)
gap(1)
wait()
print('[Mysterious Being] > Farewell, and good luck.')
time.sleep(1)
gap(6)


########## Game Setup ##########
race=chosen_race
class_u=chosen_class

starting_gear = starting_gear[chosen_class]
for item in starting_gear:
    inv.append(item)
lvl=1
xp=0
xp_tolvlup=45
if 'spellbook' in inv:
    max_mana=12
    mana=3
hp = classes[chosen_class]['HP'] + races[chosen_race]['HP']
max_hp=hp
base_atk = classes[chosen_class]['ATK'] + races[chosen_race]['ATK']
weapon=starting_weapon[chosen_class]
armor=starting_armor[chosen_class]

if "spellbook" in inv:
    for spell in starting_spells[chosen_class]:
        spellbook.append(spell)
################################



gap(6)
print("------------------------------------")
print(" - starting stats - ")
print(f"HP: {hp}/{max_hp}")
print(f"base attack: {base_atk}")
if 'spellbook' in inv:
    print(f"mana: {mana}/{max_mana}")
print(" -                - ")
print("------------------------------------")
wait()
gap(4)
print("------------------------------------")
print(" - starting items - ")
for item in inv:
    print(f"{item}")
print(" -                - ")
print("------------------------------------")
wait()
gap(4)
if "spellbook" in inv:
    print("------------------------------------")
    print(" - starting spells - ")
    for spell in spellbook:
        print(f"{spell}")
    print(" -                 - ")
    print("------------------------------------")
    wait()
    gap(4)
print("------------------------------------")
print(" - starting weapon - ")
print(f"{weapon}")
print(" -                 - ")
print("------------------------------------")
wait()
gap(4)
print("------------------------------------")
print(" - starting armor - ")
print(f"{armor}")
print(" -                - ")
print("------------------------------------")
time.sleep(1)
gap(6)
print('PRESS ENTER TO DESCEND INTO THE REALM')
descend = input("↧↧↧ >")
gap(3)
print('Descending...')
gap(3)
time.sleep(3)
print(f" - Welcome to the world of Adria, {player_name} - {chosen_race} {chosen_class} - ")
gap(3)
time.sleep(1)
location="The Summoning Fractal"
display_location(location)
time.sleep(1)
gap(3)
print('You burst forth from the fractal shining with brilliant blue sparks, you find yourself in a town square filled with excitement and valour, you see a figure walking towards you from the side of the fractal, his face is worn and scarred but his eyes sparkle with warmth')
gap(3)
wait()
gap(3)
characters["Rodor"].meet()
gap(3)
print('[Rodor] > Why hello there, I am Rodor, it is my duty to welcome all new arrivals to the realm of Adria, I believe Aphax is wating for you at the arena in the centre of town, I will take you there now.')
gap(3)
time.sleep(1)
start_quest("arena")
gap(3)
wait()
gap(3)
journey()
gap(3)
location="The Great Arena"
display_location(location)
gap(1)
complete_quest()
gap(2)
wait()
gap(1)
print("You arrive at the Great Arena, it is a sight to behold. The grand structure is made of a dark gray stone and its ominous shadow stretches across the entire town square. You see a slim figure standing next to the entrance, he is wearing a leather vest and a belt over his ragged clothes")
wait()
gap(1)
print('[Aphax] > Welcome to the Great Arena, I am Aphax, the arena master, I am here to help you get started in your journey and teach you the basics of combat.')
time.sleep(1)
print('[Aphax] > Lets step inside. We will begin by attempting to battle an Ooze.')
wait()
gap(1)
print('[Aphax] > Oozes are weak creatures, but are extremely common so you will encounter them often.')
time.sleep(1)
print('[Aphax] > Are you ready to begin?')
f_ooze=cont('battle Ooze', ['y','n'])
while f_ooze != 'y':
    print('[Aphax] > I see, I will be here if you change your mind.')
    wait()
    f_ooze=cont('battle Ooze', ['y','n'])
if f_ooze == 'y':
    print('[Aphax] > Very well, let us begin.')
    wait()
    gap(1)
    melee_tutorial=True
    print("[Aphax] > Begin by choosing the 'melee attack' option.")
    gap(4)
    wait()
    fight('Ooze')
    melee_tutorial=False
    gap(1)

print('[Aphax] > Congratulations on defeating your foe.')
time.sleep(1)
print('[Aphax] > Im sure you have noticed that you have gained some experience points, once you gain a certain amount you will level up, this will increase many of your stats.')
wait()
if "spellbook" in inv:
    spell_tutorial=True
    spell_tutorial_explain=True
    print('[Aphax] > Now that you have learned how to use the melee attack, lets try using a spell.')
    wait()
    print("[Aphax] > You will again be fighting an Ooze, this time using a spell instead of a weapon.")
    wait()
    gap(1)
    print("[Aphax] > Begin by choosing the 'cast spell' option.")
    gap(1)
    wait()
    fight('Ooze')
    spell_tutorial=False
    gap(1)
    print('[Aphax] > Congratulations on defeating your foe once again.')
    time.sleep(1)
print('[Aphax] > Now that you have learned the basics of combat, it is time for you to face off against some of the arenas more challenging enemies.')
print('[Aphax] > I will not help you from now on so best of luck.')
wait()
gap(4)
encounter(2, 3)
gap(4)
print('[Aphax] > You have done well, I am impressed.')
time.sleep(1)
print('[Aphax] > You have mastered all I have to teach for now, head to the town square and purchase some better gear.')
print('[Aphax] > Here are some shards.')
gap(1)
gain_shards(12500)
gap(1)
start_quest('gear')
gap(1)
wait()
gap(3)
journey()
gap(3)
location="Town Square"
display_location(location)
gap(3)
wait()
gap(3)















