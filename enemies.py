import random


class Enemies:
    @property
    def Enemyname(self) -> str:
        randomnumbers: int = 0
        while randomnumbers != 1:
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

    @property
    def fileread(self) -> list[str]:
        enemies: list[str] = []
        with open('enemies.txt', 'r', encoding='utf-8') as file:
            for sor in file.read().splitlines()[1:]:
                enemies.append(sor)
        return enemies

    @property
    def Stats_hp(self) -> list[int]:
        HP: list[int] = []
        while len(HP) != 1:
            if self.Enemyname == 'Bat' or self.Enemyname == 'Snake':
                En_hp = 10
                HP.append(En_hp)
            elif self.Enemyname == 'Zombie' or self.Enemyname == 'Ghost':
                En_hp = 20
                HP.append(En_hp)
            elif self.Enemyname == 'Ogre' or self.Enemyname == 'Troll':
                En_hp = 50
                HP.append(En_hp)
            elif self.Enemyname == 'Dragon':
                En_hp = 100
                HP.append(En_hp)
        return HP
    
    @property
    def Stats_spd(self) -> list[int]:
        SPD: list[int] = []
        while len(SPD) != 1:
            if self.Enemyname == 'Bat':
                En_spd = 3
                SPD.append(En_spd)
            elif self.Enemyname == 'Zombie' or self.Enemyname == 'Ogre' or self.Enemyname == 'Snake':
                En_spd = 2
                SPD.append(En_spd)
            elif self.Enemyname == 'Ghost' or self.Enemyname == 'Troll':
                En_spd = 1
                SPD.append(En_spd)
            elif self.Enemyname == 'Dragon':
                En_spd = 100
                SPD.append(En_spd)
        return SPD
    
    @property
    def Stats_atk(self) -> list[int]:
        ATK: list[int] = []
        while len(ATK) != 1:
            if self.Enemyname == 'Bat' or self.Enemyname == 'Zombie' or self.Enemyname == 'Ogre':
                En_atk = 10
                ATK.append(En_atk)
            elif self.Enemyname == 'Ghost' or self.Enemyname == 'Snake' or self.Enemyname == 'Troll':
                En_atk = 20
                ATK.append(En_atk)
            elif self.Enemyname == 'Dragon':
                En_atk = 100
                ATK.append(En_atk)
        return ATK
            

    def __init__(self):
        pass
