from menu import menu


def player_input(): # A bevitelt kezelő függvény
    while True:
        inp: str = (input("Kérem a játékos lépését! [1 -> Támadás, 2 -> Futás, 3 -> Magic, 4 -> Item]: "))
        if inp not in ["1", "2", "3", "4"]:
            print("Hibás input")
        else:
            return int(inp)


def battle(hp: int, spd: int, atk: int, mana: int, item: int, enemy_hp: int, enemy_spd: int, enemy_atk: int, enemy_name: str): # fő battle függvény
    enemy_max_atk: int = enemy_atk
    while hp > 0 and enemy_hp > 0:
        print(menu(hp, atk, spd, mana, item, enemy_hp, enemy_atk, enemy_spd, enemy_name))
        player_input_value: int = int(player_input())
        if spd > enemy_spd:
            if player_input_value == 1:
                enemy_hp = battle_PI_1(enemy_hp, atk)
            elif player_input_value == 2:
                print("Sikeres menekülés!")
                return False, (hp if hp > 0 else 0)
            elif player_input_value == 3:
                magic_select: int = int(input("Válassz varázslatot! [1 -> Healing (+30HP) (5 mana), 2 -> Enemy atk down (-7atk) (3 mana), 3 -> Player atk up (+10atk) (4 mana)]: "))
                if magic_select == 1 and mana >= 5:
                    hp, mana = battle_PI_3_1(hp, mana)
                elif magic_select == 2 and mana >= 3:
                    enemy_atk, mana = battle_PI_3_2(enemy_atk, mana)
                elif magic_select == 3 and mana >= 4:
                    atk, mana = battle_PI_3_3(atk, mana)
                else:
                    print("NINCS MANA")
            elif player_input_value == 4:
                item_select: int = int(input("Melyik itemet használod? [1-> Vulnerary (+50HP), 2 -> Killer (ellenség HP felezése)]: "))
                if item_select == 1 and item >= 1:
                    hp, item = battle_PI_4_1(hp, item)
                elif item_select == 2 and item >= 1:
                    enemy_hp, item = battle_PI_4_2(enemy_hp, item)
                else:
                    print("NINCS ITEM")
            hp = battle_main_logic_enemy(hp, enemy_atk)
        else:
            hp = battle_main_logic_enemy(hp, enemy_atk)
            if player_input_value == 1:
                enemy_hp = battle_PI_1(enemy_hp, atk)
            elif player_input_value == 2:
                print("Sikertelen menekülés!")
            elif player_input_value == 3:
                magic_select: int = int(input("Válassz varázslatot! [1 -> Healing (+30HP) (5 mana), 2 -> Enemy atk down (-7atk) (3 mana), 3 -> Player atk up (+10atk) (4 mana)]: "))
                if magic_select == 1 and mana >= 5:
                    hp, mana = battle_PI_3_1(hp, mana)
                elif magic_select == 2 and mana >= 3:
                    enemy_atk, mana = battle_PI_3_2(enemy_atk, mana)
                elif magic_select == 3 and mana >= 4:
                    atk, mana = battle_PI_3_3(atk, mana)
                else:
                    print("NINCS MANA")
            elif player_input_value == 4:
                item_select: int = int(input("Melyik itemet használod? [1-> Vulnerary (+50HP), 2 -> Killer (ellenség HP felezése)]: "))
                if item_select == 1 and item >= 1:
                    hp, item = battle_PI_4_1(hp, item)
                elif item_select == 2 and item >= 1:
                    enemy_hp, item = battle_PI_4_2(enemy_hp, item)
                else:
                    print("NINCS ITEM")

        mana += 1
        if enemy_max_atk > enemy_atk:
            enemy_atk += 1
    if enemy_hp > 0:
        print("VESZTETTÉL")
        return True, (hp if hp > 0 else 0)
    elif hp > 0:
        print("NYERTÉL")
        return False, (hp if hp > 0 else 0)


def battle_main_logic_enemy(hp: int, enemy_atk: int):
    hp -= enemy_atk
    if hp < 0:
        print(f"A játékos életereje {enemy_atk} értékkel csökkent, meghalt")
    else:
        print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt")
    return hp


def battle_escape_logic(spd: int, enemy_spd: int):
    if spd > enemy_spd:
        print("Sikeres menekülés!")
        return True
    else:
        return False
    

def battle_PI_1(enemy_hp: int, atk: int): # PI = Player Input
    enemy_hp -= atk
    print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
    return enemy_hp


def battle_PI_3_1(hp: int, mana: int): # PI = Player Input
    max_hp: int = hp
    print("Karakter élete +30")
    hp += 30
    if hp > max_hp:
        hp = max_hp
    mana -= 5
    return hp, mana


def battle_PI_3_2(enemy_atk: int, mana: int): # PI = Player Input
    print("Ellenség támadása -7")
    if enemy_atk - 7 < 0:
        enemy_atk = 0
        mana -= 3
    else:
        enemy_atk -= 7
        mana -= 3
    return enemy_atk, mana


def battle_PI_3_3(atk: int, mana: int): # PI = Player Input
    print("Támadásod +10")
    atk += 10
    mana -= 4
    return atk, mana

def battle_PI_4_1(hp: int, item: int): # PI = Player Input
    max_hp: int = hp
    print("Vulnerary felhasználva (+50HP)")
    hp += 50
    if hp > max_hp:
        hp = max_hp
    item -= 1
    return hp, item


def battle_PI_4_2(enemy_hp: int, item: int): # PI = Player Input
    print("Killer felhasználva (enemy HP/2)")
    enemy_hp = int(enemy_hp / 2)
    item -= 1
    return enemy_hp, item
