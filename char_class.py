class Playerstats:
    player_hp: int
    player_atk: int
    player_spd: int

    def __init__(self, psor: str):
        file = psor.split(' ')
        self.player_hp = int(file[1])
        self.player_atk = int(file[2])
        self.player_spd = int(file[3])
