from menu import menu


def player_input():
    inp = int(input("kérem a játékos lépését [1 -> támadás, 2 -> Futás]: "))
    return inp


def battle(hp: int, spd: int, atk: int, enemy_hp: int, enemy_spd: int, enemy_atk: int, enemy_name: str):
    while hp > 0 and enemy_hp > 0:
        print(menu(hp, atk, spd, enemy_hp, enemy_atk, enemy_spd, enemy_name))
        if spd > enemy_spd:
            if player_input() == 1:
                enemy_hp -= atk
                print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
            else:
                print("Sikeres menekülés")
                return 0  # kill battle
            hp -= enemy_atk
            print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt")
        else:
            hp -= enemy_atk
            print(f"A játékos életereje {enemy_atk} értékkel csökkent, {hp} élete maradt")
            if player_input() == 1:
                enemy_hp -= atk
                print(f"Az ellenség életereje {atk} értékkel csökkent, {enemy_hp} élete maradt")
            else:
                print("Sikertelen menekülés")
    if enemy_hp > 0:
        print("YOU LOSE")
    elif hp > 0:
        print("YOU WIN")
