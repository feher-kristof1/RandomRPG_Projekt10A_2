import random
import os
import time
import pygame
from pygame.locals import *
from char_class import Playerstats
from enemies import Enemies
from enemies import Enemymods
from battle import battle

pygame.init()
os.system('cls')


def reader(filename: str, loader_class: str, skip_num: int):
    target_list = []
    with open(filename, "r", encoding='utf-8') as file:
        for sor in file.read().splitlines()[skip_num:]:
            target_list.append(loader_class(sor))
    return target_list


def main() -> None:
    pygame.mixer.music.load("battle.ogg")
    pygame.mixer.music.play(-1, 0.0)
    enemies_list: list[Enemies] = []
    enemies_list = reader('enemies.txt', Enemies, 1)
    file_list: list[Enemymods] = reader('files.txt', Enemymods, 0)
    playerstat_list: list[Playerstats] = []
    playerstat_list = reader('player.txt', Playerstats, 0)

    stage_calc: int = 0
    hppoints: int = 0
    atkpoints: int = 0
    spdpoints: int = 0
    random_points: int = 0
    kill: bool = False
    remaining_hp: int = -999
    item: int = 5
    while random_points != 5:
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
    health: int = playerstat_list[rs].player_hp + (hppoints * 10)
    atk: int = playerstat_list[rs].player_atk + (atkpoints * 2)
    spd: int = playerstat_list[rs].player_spd + spdpoints
    while stage_calc != 10:
        r = random.randint(0, len(enemies_list) - 3)
        fr = random.randint(0, len(file_list) - 3)
        rv = r
        frv = fr

        enemy_name: str = f'{enemies_list[rv].name}{file_list[frv].file_name}'
        enemy_hp: int = int(enemies_list[rv].health * file_list[frv].file_hp)
        enemy_atk: int = int(enemies_list[rv].attack * file_list[frv].file_atk)
        enemy_spd: int = int(enemies_list[rv].speed * file_list[frv].file_spd)
        rs = random.randint(0, len(playerstat_list) - 1)

        stage_calc += 1

        print(f'{stage_calc}. pálya')

        if stage_calc == 5:
            pygame.mixer.music.load("boss1.mp3")
            pygame.mixer.music.play(-1, 0.0)
            enemy_name: str = f'{enemies_list[-1].name}{file_list[frv].file_name}'
            enemy_hp: int = int(enemies_list[-1].health * file_list[frv].file_hp)
            enemy_atk: int = int(enemies_list[-1].attack * file_list[frv].file_atk)
            enemy_spd: int = int(enemies_list[-1].speed * file_list[frv].file_spd)
            kill, remaining_hp = battle(health, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            if remaining_hp > 1:
                print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
            if remaining_hp + 50 > health:
                remaining_hp = health
            else:
                remaining_hp += 50
            health = remaining_hp
            if kill is False:
                print('Várj...')
            time.sleep(2)
            os.system('cls')
            pygame.mixer.music.load("battle.ogg")
            pygame.mixer.music.play(-1, 0.0)
        elif stage_calc == 10:
            pygame.mixer.music.load("boss2.wav")
            pygame.mixer.music.play(-1, 0.0)
            enemy_name: str = f'{enemies_list[-1].name}{file_list[-1].file_name}'
            enemy_hp: int = int(enemies_list[-1].health * file_list[-1].file_hp)
            enemy_atk: int = int(enemies_list[-1].attack * file_list[-1].file_atk)
            enemy_spd: int = int(enemies_list[-1].speed * file_list[-1].file_spd)
            kill, remaining_hp = battle(health, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            if remaining_hp > 1:
                print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
            if remaining_hp + 50 > health:
                remaining_hp = health
            else:
                remaining_hp += 50
            health = remaining_hp
            if kill is False:
                print('Várj...')
            time.sleep(2)
            os.system('cls')
        else:
            kill, remaining_hp = battle(health, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            if remaining_hp > 1:
                print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
            if remaining_hp + 50 > health:
                remaining_hp = health
            else:
                remaining_hp += 50
            health = remaining_hp
            if kill is False:
                print('Várj...')
            time.sleep(2)
            os.system('cls')

        if kill is True:
            break

    print("JÁTÉK VÉGE")


if __name__ == "__main__":
    main()

inpcheck: str = ''
while inpcheck != "N":
    yes = ['y', 'Y']
    no = ['n', 'N']
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play(-1, 0.0)
    inpcheck = str(input('Szeretnél új játékot kezdeni? (Y/N): '))
    if inpcheck in yes:
        os.system('cls')
        main()
    elif inpcheck in no:
        break
