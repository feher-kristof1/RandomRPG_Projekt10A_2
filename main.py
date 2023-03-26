import random


def main() -> None:
    randomnumbers: int = 0
    while randomnumbers != 9:
        r: int = random.randint(0, 100)
        randomnumbers += 1
        if r <= 20:
            enemyname = 'Bat'
        elif r <= 36 and r > 20:
            enemyname = 'Zombie'
        elif r <= 52 and r > 36:
            enemyname = 'Ogre'
        elif r <= 68 and r > 52:
            enemyname = 'Troll'
        elif r <= 84 and r > 68:
            enemyname = 'Snake'
        elif r <= 100 and r > 84:
            enemyname = 'Ghost'
              
    randomnumbers: int = 0
    while randomnumbers != 9:
        r: int = random.randint(0, 100)
        randomnumbers += 1
        if r <= 12:
            type = '.jpg'
        elif r <= 26 and r > 12:
            type = '.png'
        elif r <= 40 and r > 26:
            type = '.txt'
        elif r <= 52 and r > 40:
            type = '.mp3'
        elif r <= 64 and r > 52:
            type = '.mp4'
        elif r <= 76 and r > 64:
            type = '.rar'
        elif r <= 88 and r > 76:
            type = '.zip'
        elif r <= 100 and r > 88:
            type = '.iso'

    print(f'You have been attacked by a(n) {enemyname}{type}')


if __name__ == "__main__":
    main()
