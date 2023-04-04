from char_class import Playerstats
from enemies import Enemies
from enemies import Enemymods
from battle import battle
import random


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
    randomnumber: int = 0
    while randomnumber != 1:
        r = random.randint(0, len(enemies_list) - 2)
        fr = random.randint(0, len(file_list) - 1)
        rv = r
        frv = fr
        enemy_name: str = f'{enemies_list[rv].Name}{file_list[frv].file_name}'
        enemy_hp: int = int(enemies_list[rv].hp * file_list[frv].file_hp)
        enemy_atk: int = int(enemies_list[rv].atk * file_list[frv].file_atk)
        enemy_spd: int = int(enemies_list[rv].spd * file_list[frv].file_spd)
        rs = random.randint(0, len(playerstat_list) - 1)
        random_points: int = 0
        hppoints: int = 0
        atkpoints: int = 0
        spdpoints: int = 0
        mana: int = 10
        item: int = 5
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
        hp: int = playerstat_list[rs].player_hp + (hppoints * 10)
        atk: int = playerstat_list[rs].player_atk + (atkpoints * 10)
        spd: int = playerstat_list[rs].player_spd + spdpoints
        randomnumber += 1
        # print(f'{enemies_list[r].Name}{file_list[fr].file_name}')
        # print(enemies_list[r].hp * file_list[fr].file_hp)
        # print(enemies_list[r].atk * file_list[fr].file_atk)
        # print(enemies_list[r].spd * file_list[fr].file_spd)
    battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)


if __name__ == "__main__":
    main()
