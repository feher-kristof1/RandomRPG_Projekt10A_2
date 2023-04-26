import pygame
from pygame.locals import *
import random
import os
import time
from char_class import Playerstats
from enemies import Enemies
from enemies import Enemymods
from battle import battle

pygame.init()


def main() -> None:
    pygame.mixer.music.load("battle.ogg")
    pygame.mixer.music.play(-1, 0.0)
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

    stage_calc: int = 0
    hppoints: int = 0
    atkpoints: int = 0
    spdpoints: int = 0
    random_points: int = 0
    kill: bool = False
    remaining_hp: int = -999
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

        print(f'{stage_calc}. pálya')
        
        if stage_calc == 5:
            pygame.mixer.music.load("boss1.mp3")
            pygame.mixer.music.play(-1, 0.0)
            enemy_name: str = f'{enemies_list[-1].Name}{file_list[frv].file_name}'
            enemy_hp: int = int(enemies_list[-1].hp * file_list[frv].file_hp)
            enemy_atk: int = int(enemies_list[-1].atk * file_list[frv].file_atk)
            enemy_spd: int = int(enemies_list[-1].spd * file_list[frv].file_spd)
            kill, remaining_hp = battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
            if remaining_hp + 50 > hp:
                remaining_hp = hp
            else:
                remaining_hp += 50
            hp = remaining_hp
            if kill is False:
                print('Wait...')
            time.sleep(2)
            os.system('cls')
            pygame.mixer.music.load("battle.ogg")
            pygame.mixer.music.play(-1, 0.0)
        elif stage_calc == 10:
            pygame.mixer.music.load("boss2.wav")
            pygame.mixer.music.play(-1, 0.0)
            enemy_name: str = f'{enemies_list[-1].Name}{file_list[-1].file_name}'
            enemy_hp: int = int(enemies_list[-1].hp * file_list[-1].file_hp)
            enemy_atk: int = int(enemies_list[-1].atk * file_list[-1].file_atk)
            enemy_spd: int = int(enemies_list[-1].spd * file_list[-1].file_spd)
            kill, remaining_hp = battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
            if remaining_hp + 50 > hp:
                remaining_hp = hp
            else:
                remaining_hp += 50
            hp = remaining_hp
            if kill is False:
                print('Wait...')
            time.sleep(2)
            os.system('cls')
        else:
            kill, remaining_hp = battle(hp, spd, atk, mana, item, enemy_hp, enemy_spd, enemy_atk, enemy_name)
            print(f"Maradék élet: {remaining_hp}, +50 a következő körben")
            if remaining_hp + 50 > hp:
                remaining_hp = hp
            else:
                remaining_hp += 50
            hp = remaining_hp
            if kill is False:
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
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.play(-1, 0.0)
    inpp: str = str(input('Szeretnél új játékot kezdeni? (Y/N): '))
    if inpp == 'Y':
        os.system('cls')
        main()
    else:
        break
