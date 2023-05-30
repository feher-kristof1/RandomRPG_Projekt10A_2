def menu(hp: int, atk: int, spd: int, mana: int, item: int, enemy_hp: int, enemy_atk: int, enemy_spd: int, enemy_name: str) -> str:
    hp_ret_string = f'Életerőd {hp}'
    atk_ret_string = f'Támadási erőd {atk}'
    spd_ret_string = f'Sebességed {spd}'
    mana_ret_string = f'Manád {mana}'
    item_ret_string = f'Itemek száma {item}'
    enemy_hp_ret_string = f'Ellenséged életereje {enemy_hp}'
    enemy_atk_ret_string = f'Ellenséged támadási ereje {enemy_atk}'
    enemy_spd_ret_string = f'Ellenséged sebessége {enemy_spd}'
    enemy_name_ret_string = f'Ellenséged: {enemy_name}'
    return f'{hp_ret_string}\n{atk_ret_string}\n{spd_ret_string}\n{mana_ret_string}\n{item_ret_string}\n{enemy_name_ret_string}\n{enemy_hp_ret_string}\n{enemy_atk_ret_string}\n{enemy_spd_ret_string}'

