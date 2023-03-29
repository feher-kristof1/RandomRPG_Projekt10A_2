def menu(hp: int, atk: int, spd: int, enemy_hp: int, enemy_atk: int, enemy_spd: int, enemy_name: str) -> str:
    hp_ret_string = f'életerőd {hp}'
    atk_ret_string = f'támadási erőd {atk}'
    spd_ret_string = f'sebességed {spd}'
    enemy_hp_ret_string = f'ellenséged életereje {enemy_hp}'
    enemy_atk_ret_string = f'ellenséged támadási ereje {enemy_atk}'
    enemy_spd_ret_string = f'ellenséged sebessége {enemy_spd}'
    enemy_name_ret_string = f'ellenséged {enemy_name}'
    return f'{hp_ret_string}\n{atk_ret_string}\n{spd_ret_string}\n{enemy_name_ret_string}\n{enemy_hp_ret_string}\n{enemy_atk_ret_string}\n{enemy_spd_ret_string}'
