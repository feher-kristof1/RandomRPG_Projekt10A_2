from pstats import Stats
import random


class Enemies:
    @property
    def Enemyname(self) -> str:
        randomnumbers: int = 0
        while randomnumbers != 9:
            enemyname: str = ''
            r: int = random.randint(0, 100)
            randomnumbers += 1
            if r <= 20:
                enemyname = 'Bat'
                return enemyname
            elif r <= 36 and r > 20:
                enemyname = 'Zombie'
                return enemyname
            elif r <= 52 and r > 36:
                enemyname = 'Ogre'
                return enemyname
            elif r <= 68 and r > 52:
                enemyname = 'Troll'
                return enemyname
            elif r <= 84 and r > 68:
                enemyname = 'Snake'
                return enemyname
            elif r <= 100 and r > 84:
                enemyname = 'Ghost'
                return enemyname

    @property
    def Enemytype(self) -> str:
        randomnumbers: int = 0
        while randomnumbers != 9:
            entype: str = ''
            r: int = random.randint(0, 100)
            randomnumbers += 1
            if r <= 12:
                entype = '.jpg'
                return entype
            elif r <= 26 and r > 12:
                entype = '.png'
                return entype
            elif r <= 40 and r > 26:
                entype = '.txt'
                return entype
            elif r <= 52 and r > 40:
                entype = '.mp3'
                return entype
            elif r <= 64 and r > 52:
                entype = '.mp4'
                return entype
            elif r <= 76 and r > 64:
                entype = '.rar'
                return entype
            elif r <= 88 and r > 76:
                entype = '.zip'
                return entype
            elif r <= 100 and r > 88:
                entype = '.iso'
                return entype

    @ property
    def Enemystats_hp(self) -> int:
        hp: int = 0
        return hp

    @ property
    def Enemystats_atk(self) -> int:
        atk: int = 0
        return atk

    @ property
    def Enemystats_spd(self) -> int:
        spd: int = 0
        return spd
    @property
    def fileread(self) -> list[str]:
        enemies: list[str] = []
        with open('enemies.txt', 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines()[1:]:
                enemies.append(sor)
        return enemies
    def __init__(self):
        pass
