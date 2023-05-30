class Enemies:
    name: str
    health: int
    attack: int
    speed: int


    def __init__(self, sor: str):
        stat = sor.split(' ')
        self.name = stat[0]
        self.health = int(stat[1])
        self.attack = int(stat[2])
        self.speed = int(stat[3])


class Enemymods:
    file_name: str
    file_hp: float
    file_atk: float
    file_spd: float

    def __init__(self, fsor: str):
        file = fsor.split(' ')
        self.file_name = file[0]
        self.file_hp = float(file[1])
        self.file_atk = float(file[2])
        self.file_spd = float(file[3])
