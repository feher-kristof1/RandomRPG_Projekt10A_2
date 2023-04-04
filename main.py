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

    # print(f'You have been attacked by a(n) {enemies.Enemyname}{enemies.Enemytype}')
    # print(f'It has {enemies.Enemystats_hp} hitpoints.')
    # print(f'It deals {enemies.Enemystats_atk} hitpoints of damage with every hit.')
    # print(f'It has a speed of {enemies.Enemystats_spd}.')
    randomnumber: int = 0
    while randomnumber != 1:
        r = random.randint(0, len(enemies_list) - 1)
        fr = random.randint(0, len(file_list) - 1)
        rv = r
        frv = fr
        enemy_name: str = f'{enemies_list[rv].Name}{file_list[frv].file_name}'
        enemy_hp: int = int(enemies_list[rv].hp * file_list[frv].file_hp)
        enemy_atk: int = int(enemies_list[rv].atk * file_list[frv].file_atk)
        enemy_spd: int = int(enemies_list[rv].spd * file_list[frv].file_spd)
        hp: int = 100
        atk: int = 10
        spd: int = 10
        mana: int = 10
        item: int = 5
        
        randomnumber += 1
        # print(f'{enemies_list[r].Name}{file_list[fr].file_name}')
        # print(enemies_list[r].hp * file_list[fr].file_hp)
        # print(enemies_list[r].atk * file_list[fr].file_atk)
        # print(enemies_list[r].spd * file_list[fr].file_spd)
    battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)


if __name__ == "__main__":
    main()
