from menu import menu


def player_input():
    inp = int(input("kérem a játékos lépését [1 -> támadás, 2 -> Futás, 3 -> magic, 4 -> item]: "))
    return inp


def battle(hp: int, spd: int, atk: int, mana: int, item: int, enemy_hp: int, enemy_spd: int, enemy_atk: int, enemy_name: str):
    mana_val: int = mana
    while hp > 0 and enemy_hp > 0:
        print(menu(hp, atk, spd, mana, item, enemy_hp, enemy_atk, enemy_spd, enemy_name))
        player_input_value: int = int(player_input())
        if spd > enemy_spd:
            if player_input_value == 1:
                enemy_hp -= atk
                print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
            elif player_input_value == 2:
                print("Sikeres menekülés")
                return 0  # kill battle
            elif player_input_value == 3:
                magic_select: int = int(input("válassz varázslatot[1 -> healing(+30HP)(5 mana), 2 ->enemy atk down(-1atk)(3 mana), 3 -> your atk up(+1atk)(3mana)]: "))
                if magic_select == 1 and mana >= 5:
                    print("karakter élete +30")
                    hp += 30
                    mana -= 5
                elif magic_select == 2 and mana >= 3:
                    print("ellenség támadása -1")
                    enemy_atk -= 1
                    mana -= 3
                elif magic_select == 3 and mana >= 3:
                    print("támadásod +1")
                    atk += 1
                    mana -= 3
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
            print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt")
        else:
            hp -= enemy_atk
            print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt")
            if player_input_value == 1:
                enemy_hp -= atk
                print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
            elif player_input_value == 2:
                print("Sikertelen menekülés")
            elif player_input_value == 3:
                magic_select: int = int(input("válassz varázslatot[1 -> healing(+30HP)(5 mana), 2 ->enemy atk down(-1atk)(3 mana), 3 -> your atk up(+1atk)(3mana)]: "))
                if magic_select == 1 and mana >= 5:
                    print("karakter élete +30")
                    hp += 30
                    mana -= 5
                elif magic_select == 2 and mana >= 3:
                    print("ellenség támadása -1")
                    enemy_atk -= 1
                    mana -= 3
                elif magic_select == 3 and mana >= 3:
                    print("támadásod +1")
                    atk += 1
                    mana -= 3
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
        mana_val += 1
    if enemy_hp > 0:
        print("YOU LOSE")
    elif hp > 0:
        print("YOU WIN")
