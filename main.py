import random
import os
import time
from char_class import Playerstats
from enemies import Enemies
from enemies import Enemymods
from battle import battle


def main() -> None:
    enemies_list: list[Enemies] = []
    with open('enemies.txt', 'r', encoding='utf-8') as file:
        for sor in file.read().splitlines()[1:]:
            enemies_list.append(Enemies(sor))

    file_list: list[Enemymods] = []
    with open('files.txt', 'r', encoding='utf-8') as file:
        for fsor in file.read().splitlines():
            file_list.append(Enemymods(fsor))

    playerstat_list: list[Playerstats] = []
    with open('player.txt', 'r', encoding='utf-8') as file:
        for psor in file.read().splitlines():
            playerstat_list.append(Playerstats(psor))

    # print(f'You have been attacked by a(n) {enemies.Enemyname}{enemies.Enemytype}')
    # print(f'It has {enemies.Enemystats_hp} hitpoints.')
    # print(f'It deals {enemies.Enemystats_atk} hitpoints of damage with every hit.')
    # print(f'It has a speed of {enemies.Enemystats_spd}.')
    stage_calc: int = 0
    hppoints: int = 0
    atkpoints: int = 0
    spdpoints: int = 0
    random_points: int = 0
    while random_points != 10:
        skillpoint: int = random.randint(0, 3)
        if skillpoint == 1:
            hppoints += 1
            random_points += 1
        elif skillpoint == 2:
            atkpoints += 1
            random_points += 1
        elif skillpoint == 3:
            spdpoints += 1
            random_points += 1
        elif skillpoint == 0:
            hppoints += 1
            spdpoints += 1
            random_points += 1
    kill: bool = False
    while random_points != 20:
        skillpoint: int = random.randint(0, 3)
        if skillpoint == 1:
            hppoints += 1
            random_points += 1
        elif skillpoint == 2:
            atkpoints += 1
            random_points += 1
        elif skillpoint == 3:
            spdpoints += 1
            random_points += 1
        elif skillpoint == 0:
            hppoints += 1
            spdpoints += 1
            random_points += 1
    r = random.randint(0, len(enemies_list) - 2)
    fr = random.randint(0, len(file_list) - 2)
    rv = r
    frv = fr
    rs = random.randint(0, len(playerstat_list) - 1)

    mana: int = 10
    item: int = 5
    hp: int = playerstat_list[rs].player_hp + (hppoints * 15)
    atk: int = playerstat_list[rs].player_atk + (atkpoints * 5)
    spd: int = playerstat_list[rs].player_spd + spdpoints
    while stage_calc != 10:
        r = random.randint(0, len(enemies_list) - 2)
        fr = random.randint(0, len(file_list) - 2)
        rv = r
        frv = fr

        enemy_name: str = f'{enemies_list[rv].Name}{file_list[frv].file_name}'
        enemy_hp: int = int(enemies_list[rv].hp * file_list[frv].file_hp)
        enemy_atk: int = int(enemies_list[rv].atk * file_list[frv].file_atk)
        enemy_spd: int = int(enemies_list[rv].spd * file_list[frv].file_spd)
        rs = random.randint(0, len(playerstat_list) - 1)

        stage_calc += 1
        # print(f'{enemies_list[r].Name}{file_list[fr].file_name}')
        # print(enemies_list[r].hp * file_list[fr].file_hp)
        # print(enemies_list[r].atk * file_list[fr].file_atk)
        # print(enemies_list[r].spd * file_list[fr].file_spd)

        print(f'{stage_calc}. pálya')

        if stage_calc == 5:
            enemy_name: str = f'{enemies_list[-1].Name}{file_list[frv].file_name}'
            enemy_hp: int = int(enemies_list[-1].hp * file_list[frv].file_hp)
            enemy_atk: int = int(enemies_list[-1].atk * file_list[frv].file_atk)
            enemy_spd: int = int(enemies_list[-1].spd * file_list[frv].file_spd)
            kill, remaining_hp = battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            if remaining_hp + 50 > hp:
                remaining_hp = hp
            else:
                remaining_hp += 50
            hp = remaining_hp
            if kill is False:
                print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
                print('Wait...')
            time.sleep(2)
            os.system('cls')
        elif stage_calc == 10:
            enemy_name: str = f'{enemies_list[-1].Name}{file_list[-1].file_name}'
            enemy_hp: int = int(enemies_list[-1].hp * file_list[-1].file_hp)
            enemy_atk: int = int(enemies_list[-1].atk * file_list[-1].file_atk)
            enemy_spd: int = int(enemies_list[-1].spd * file_list[-1].file_spd)
            kill, remaining_hp = battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            if kill is False:
                print('Wait...')
            time.sleep(2)
            os.system('cls')
        else:
            kill, remaining_hp = battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            if remaining_hp + 50 > hp:
                remaining_hp = hp
            else:
                remaining_hp += 50
            hp = remaining_hp
            if kill is False:
                print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
                print('Wait...')
            time.sleep(2)
            os.system('cls')
        if kill is True:
            break
        # random_points = 0
        # while random_points != 1:
        #     skillpoint: int = random.randint(0, 3)
        #     if skillpoint == 1:
        #         hppoints += 1
        #         random_points += 1
        #     elif skillpoint == 2:
        #         atkpoints += 1
        #         random_points += 1
        #     elif skillpoint == 3:
        #         spdpoints += 1
        #         random_points += 1
        #     elif skillpoint == 0:
        #         hppoints += 1
        #         spdpoints += 1
        #         random_points += 1

    print("GAME END")


if __name__ == "__main__":
    main()

while True:
    inpp: str = str(input('Szeretnél új játékot kezdeni? (Y/N): '))
    if inpp not in ['Y', 'y', 'N', 'n']:
        print('Hibás input!')
    else:
        if inpp == 'Y' or inpp == 'y':
            os.system('cls')
            main()
        else:
            break
