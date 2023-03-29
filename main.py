from enemies import Enemies
from enemies import Enemymods
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
        fr = random.randint(0, len(file_list))
        randomnumber += 1
        print(f'{enemies_list[r].Name}{file_list[fr].file_name}')
        print(enemies_list[r].hp * file_list[fr].file_hp)
        print(enemies_list[r].atk * file_list[fr].file_atk)
        print(enemies_list[r].spd * file_list[fr].file_spd)


if __name__ == "__main__":
    main()
