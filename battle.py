from rich.console import Console
from menu import menu


console = Console()


def player_input():
    while True:
        console.print('Lehetőségeid:', style='bright_white')
        console.print('\t1 -> Támadás;\n\t2 -> Futás;\n\t3 -> Mágia használata;\n\t4 -> Item használata;', style='bright_white')
        inp: str = (input("Kérem a játékos lépését! "))
        if inp not in ["1", "2", "3", "4"]:
            console.print("Hibás input!", style='bright_red')
        else:
            return int(inp)


def battle_main_logic_enemy(hp: int, enemy_atk: int):
    hp -= enemy_atk
    if hp < 0:
        console.print(f"A játékos életereje {enemy_atk} értékkel csökkent, meghalt", style='black on red')
    else:
        console.print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt", style='green on black')
    return hp


def battle_escape_logic(spd: int, enemy_spd: int):
    if spd > enemy_spd:
        console.print("Sikeres menekülés", style='yellow on black')
        return True
    else:
        return False


def battle_PI_1(enemy_hp: int, atk: int):
    enemy_hp -= atk
    console.print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt", style='red on black')
    return enemy_hp


def battle_PI_3_1(hp: int, mana: int):
    max_hp: int = hp
    console.print("Karakter élete +30", style='green')
    hp += 30
    if hp > max_hp:
        hp = max_hp
    mana -= 5
    return hp, mana


def battle_PI_3_2(enemy_atk: int, mana: int):
    console.print("Ellenség támadása -7", style='dark_olive_green2')
    if enemy_atk - 7 < 0:
        enemy_atk = 0
        mana -= 3
    else:
        enemy_atk -= 7
        mana -= 3
    return enemy_atk, mana


def battle_PI_3_3(atk: int, mana: int):
    console.print("Támadásod +10", style='dark_olive_green2')
    atk += 10
    mana -= 4
    return atk, mana


def battle_PI_4_1(hp: int, item: int):
    max_hp: int = hp
    console.print("Vulnerary felhasználva (+50HP)", style='orange4')
    hp += 50
    if hp > max_hp:
        hp = max_hp
    item -= 1
    return hp, item


def battle_PI_4_2(enemy_hp: int, item: int):
    console.print("Killer felhasználva (enemy HP felezve)", style='orange4')
    enemy_hp = int(enemy_hp / 2)
    item -= 1
    return enemy_hp, item


def battle(hp: int, spd: int, atk: int, mana: int, item: int, enemy_hp: int, enemy_spd: int, enemy_atk: int, enemy_name: str):  # fő battle függvény
    enemy_max_atk: int = enemy_atk
    while hp > 0 and enemy_hp > 0:
        console.print(f'{menu(hp, atk, spd, mana, item, enemy_hp, enemy_atk, enemy_spd, enemy_name)}', style='grey62')
        player_input_value: int = int(player_input())
        if spd > enemy_spd:
            if player_input_value == 1:
                enemy_hp = battle_PI_1(enemy_hp, atk)
            elif player_input_value == 2:
                console.print("Sikeres menekülés", style='yellow on black')
                return False, (hp if hp > 0 else 0)
            elif player_input_value == 3:
                console.print('Varázslataid:', style='turquoise4')
                console.print('\t1 -> Healing:(+30 HP),(5 mana);\n\t2 -> Enemy atk down:(-7 atk),(3 mana);\n\t3 -> Your atk up:(+10 atk),(4 mana);', style='turquoise4')
                magic_select: int = int(input("Válassz varázslatot:"))
                if magic_select == 1 and mana >= 5:
                    hp, mana = battle_PI_3_1(hp, mana)
                elif magic_select == 2 and mana >= 3:
                    enemy_atk, mana = battle_PI_3_2(enemy_atk, mana)
                elif magic_select == 3 and mana >= 4:
                    atk, mana = battle_PI_3_3(atk, mana)
                else:
                    print("NINCS MANA")
            elif player_input_value == 4:
                console.print('Itemjeid:', style='orange3')
                console.print('\t1 -> Vulnerary: +50HP;\n\t2 -> Killer: Enemy HP halved;', style='orange3')
                item_select: int = int(input("Válassz itemet: "))
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
                console.print("Sikertelen menekülés", style='orange3')
            elif player_input_value == 3:
                console.print('Varázslataid:', style='turquoise4')
                console.print('\t1 -> Healing:(+30HP),(5 mana);\n\t2 -> Enemy atk down:(-7atk),(3 mana);\n\t3 -> Your atk up:(+10atk),(4 mana);', style='turquoise4')
                magic_select: int = int(input("Válassz varázslatot:"))
                if magic_select == 1 and mana >= 5:
                    hp, mana = battle_PI_3_1(hp, mana)
                elif magic_select == 2 and mana >= 3:
                    enemy_atk, mana = battle_PI_3_2(enemy_atk, mana)
                elif magic_select == 3 and mana >= 4:
                    atk, mana = battle_PI_3_3(atk, mana)
                else:
                    print("NINCS MANA")
            elif player_input_value == 4:
                console.print('Itemjeid:', style='orange3')
                console.print('1-> Vulnerary: +50HP;\n\t 2 -> Killer: Enemy HP halved;', style='ornage3')
                item_select: int = int(input("Válassz itemet: "))
                if item_select == 1 and item >= 1:
                    hp, item = battle_PI_4_1(hp, item)
                elif item_select == 2 and item >= 1:
                    enemy_hp, item = battle_PI_4_2(enemy_hp, item)
                else:
                    print("NINCS ITEM")

            mana += 1
        if enemy_atk + 1 > enemy_max_atk:
            pass
        else:
            enemy_atk += 1
    if enemy_hp > 0:
        console.print("VESZTETTÉL", style='grey85 on grey3')
        return True, (hp if hp > 0 else 0)
    elif hp > 0:
        console.print("NYERTÉL", style='gold1')
        return False, (hp if hp > 0 else 0)
