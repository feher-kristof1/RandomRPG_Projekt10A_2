
class Enemies:
    Name: str
    hp: int
    atk: int
    spd: int

    # @property
    # def fileread(self) -> list[Enemies]:
    # enemies: list[Enemies] = []
    # with open('enemies.txt', 'r', encoding='utf-8') as file:
    #     for sor in file.read().splitlines()[1:]:
    #         enemies.append(Enemies(sor))
    # return enemies

    def __init__(self, sor: str):
        stat = sor.split(' ')
        self.Name = stat[0]
        self.hp = int(stat[1])
        self.atk = int(stat[2])
        self.spd = int(stat[3])


class Enemymods:
    file_name: str
    file_hp: float
    file_atk: float
    file_spd: int

    def __init__(self, fsor: str):
        file = fsor.split(' ')
        self.file_name = file[0]
        self.file_hp = float(file[1])
        self.file_atk = float(file[2])
        self.file_spd = int(file[3])
