from menu import menu


def player_input():
    while True:
        inp: str = (input("Kérem a játékos lépését! [1 -> Támadás, 2 -> Futás, 3 -> Magic, 4 -> Item]: "))
        if inp not in ["1", "2", "3", "4"]:
            print("Hibás input")
        else:
            return int(inp)


def battle(hp: int, spd: int, atk: int, mana: int, item: int, enemy_hp: int, enemy_spd: int, enemy_atk: int, enemy_name: str):
    enemy_max_atk: int = enemy_atk
    while hp > 0 and enemy_hp > 0:
        print(menu(hp, atk, spd, mana, item, enemy_hp, enemy_atk, enemy_spd, enemy_name))
        player_input_value: int = int(player_input())
        if spd > enemy_spd:
            if player_input_value == 1:
                enemy_hp -= atk
                print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
            elif player_input_value == 2:
                print("Sikeres menekülés")
                return False, (hp if hp > 0 else 0)
            elif player_input_value == 3:
                magic_select: int = int(input("Válassz varázslatot! [1 -> Healing (+30HP) (5 mana), 2 -> Enemy atk down (-7atk) (3 mana), 3 -> Player atk up (+10atk) (4 mana)]: "))
                if magic_select == 1 and mana >= 5:
                    print("Karakter élete +30")
                    hp += 30
                    mana -= 5
                elif magic_select == 2 and mana >= 3:
                    print("Ellenség támadása -7")
                    if enemy_atk - 7 < 0:
                        enemy_atk = 0
                    else:
                        enemy_atk -= 7
                    mana -= 3
                elif magic_select == 3 and mana >= 4:
                    print("Támadásod +10")
                    atk += 10
                    mana -= 4
                else:
                    print("NINCS MANA")

            elif player_input_value == 4:
                item_select: int = int(input("Melyik itemet használod? [1-> Vulnerary (+50HP), 2 -> Killer (ellenség HP felezése)]: "))
                if item_select == 1 and item >= 1:
                    print("Vulnerary felhasználva (+50HP)")
                    hp += 50
                    item -= 1
                elif item_select == 2 and item >= 1:
                    print("Killer felhasználva (enemy HP/2)")
                    enemy_hp = int(enemy_hp / 2)
                    item -= 1
                else:
                    print("NINCS ITEM")
            hp -= enemy_atk
            if hp < 0:
                print(f"A játékos életereje {enemy_atk} értékkel csökkent, meghalt")
            else:
                print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt")
            mana += 1
        else:
            hp -= enemy_atk
            if hp < 0:
                print(f"A játékos életereje {enemy_atk} értékkel csökkent, meghalt")
            else:
                print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt")
            if player_input_value == 1:
                enemy_hp -= atk
                if hp < 0:
                    print(f"Az ellenség életereje {atk} értékkel csökkent, meghalt")
                else:
                    print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
            elif player_input_value == 2:
                print("Sikertelen menekülés")
            elif player_input_value == 3:
                magic_select: int = int(input("Válassz varázslatot! [1 -> Healing (+30HP) (5 mana), 2 -> Enemy atk down (-7atk) (3 mana), 3 -> Player atk up (+10atk) (4 mana)]: "))
                if magic_select == 1 and mana >= 5:
                    print("Karakter élete +30")
                    hp += 30
                    mana -= 5
                elif magic_select == 2 and mana >= 3:
                    print("Ellenség támadása -7")
                    if enemy_atk - 7 < 0:
                        enemy_atk = 0
                    else:
                        enemy_atk -= 7
                    mana -= 3
                elif magic_select == 3 and mana >= 4:
                    print("Támadásod +10")
                    atk += 10
                    mana -= 4
                else:
                    print("NINCS MANA")
            elif player_input_value == 4:
                item_select: int = int(input("Melyik itemet használod? [1-> Vulnerary (+50HP), 2 -> Killer (ellenség HP felezése)]: "))
                if item_select == 1 and item >= 1:
                    print("Vulnerary használva(+50HP)")
                    hp += 50
                    item -= 1
                elif item_select == 2 and item >= 1:
                    print("Killer használva(enemy HP/2)")
                    enemy_hp = int(enemy_hp / 2)
                    item -= 1
                else:
                    print("NINCS ITEM")
            mana += 1
        if enemy_atk + 1 > enemy_max_atk:
            pass
        else:
            enemy_atk += 1
    if enemy_hp > 0:
        print("VESZTETTÉL")
        return True, (hp if hp > 0 else 0)
    elif hp > 0:
        print("NYERTÉL")
        return False, (hp if hp > 0 else 0)
