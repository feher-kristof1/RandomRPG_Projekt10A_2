from enemies import Enemies


def main() -> None:
    enemies: Enemies = Enemies()

    print(f'You have been attacked by a(n) {enemies.Enemyname}{enemies.Enemytype}')
    print(f'It has {enemies.Enemystats_hp} hitpoints.')
    print(f'It deals {enemies.Enemystats_atk} hitpoints of damage with every hit.')
    print(f'It has a speed of {enemies.Enemystats_spd}.')
    print(enemies.fileread[0])

if __name__ == "__main__":
    main()
