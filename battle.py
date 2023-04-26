from menu import menu


def player_input():
    while True:
        inp: str = (input("kérem a játékos lépését [1 -> támadás, 2 -> Futás, 3 -> magic, 4 -> item]: "))
        if inp not in ["1", "2", "3", "4"]:
            print("Hibás input")
        else:
            return int(inp)


def battle(hp: int, spd: int, atk: int, mana: int, item: int, enemy_hp: int, enemy_spd: int, enemy_atk: int, enemy_name: str):
    while hp > 0 and enemy_hp > 0:
        print(menu(hp, atk, spd, mana, item, enemy_hp, enemy_atk, enemy_spd, enemy_name))
        player_input_value: int = int(player_input())
        if spd > enemy_spd:
            if player_input_value == 1:
                enemy_hp -= atk
                print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
            elif player_input_value == 2:
                print("Sikeres menekülés")
                return False, hp if hp > 0 else 0
            elif player_input_value == 3:
                while True:
                    magic_select: int = int(input("válassz varázslatot[1 -> healing(+30HP)(5 mana), 2 ->enemy atk down(-7atk)(3 mana), 3 -> your atk up(+10atk)(4mana)]: "))
                    if magic_select not in [1, 2, 3]:
                        print('Hibás input!')
                    else:
                        
                if magic_select == 1 and mana >= 5:
                    print("karakter élete +30")
                    hp += 30
                    mana -= 5
                elif magic_select == 2 and mana >= 3:
                    print("ellenség támadása -7")
                    if enemy_atk - 7 < 0:
                        enemy_atk = 0
                    else:
                        enemy_atk -= 7
                    mana -= 3
                elif magic_select == 3 and mana >= 4:
                    print("támadásod +10")
                    atk += 10
                    mana -= 4
                else:
                    print("NO MANA")

            elif player_input_value == 4:
                item_select: int = int(input("melyik itemet használod[1-> vulnerary(+50HP), 2 -> killer(enemy HP halved)]: "))
                if item_select == 1 and item >= 1:
                    print("vulnerary használva(+50HP)")
                    hp += 50
                    item -= 1
                elif item_select == 2 and item >= 1:
                    print("killer használva(enemy HP/2)")
                    enemy_hp = int(enemy_hp / 2)
                else:
                    print("NO ITEMS")
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
                magic_select: int = int(input("válassz varázslatot[1 -> healing(+30HP)(5 mana), 2 ->enemy atk down(-7atk)(3 mana), 3 -> your atk up(+10atk)(4mana)]: "))
                if magic_select == 1 and mana >= 5:
                    print("karakter élete +30")
                    hp += 30
                    mana -= 5
                elif magic_select == 2 and mana >= 3:
                    print("ellenség támadása -7")
                    if enemy_atk - 7 < 0:
                        enemy_atk = 0
                    else:
                        enemy_atk -= 7
                    mana -= 3
                elif magic_select == 3 and mana >= 4:
                    print("támadásod +10")
                    atk += 10
                    mana -= 4
                else:
                    print("NO MANA")
            elif player_input_value == 4:
                item_select: int = int(input("melyik itemet használod[1-> vulnerary(+50HP), 2 -> killer(enemy HP halved)]: "))
                if item_select == 1 and item >= 1:
                    print("vulnerary használva(+50HP)")
                    hp += 50
                    item -= 1
                elif item_select == 2 and item >= 1:
                    print("killer használva(enemy HP/2)")
                    enemy_hp = int(enemy_hp / 2)
                else:
                    print("NO ITEMS")
            mana += 1
    if enemy_hp > 0:
        print("YOU LOSE")
        return True, hp if hp > 0 else 0
    elif hp > 0:
        print("YOU WIN")
        return False, hp if hp > 0 else 0
