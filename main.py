import random


def main() -> None:
    randomnumbers: int = 0
    while randomnumbers != 9:
        r: int = random.randint(0, 100)
        randomnumbers += 1
        if r <= 20:
            print('Bat')
        elif r <= 36 and r > 20:
            print('Zombie')
        elif r <= 52 and r > 36:
            print('Ogre') 
        elif r <= 68 and r > 52:
            print('Troll')
        elif r <= 84 and r > 68:
            print('Snake') 
        elif r <= 100 and r > 84:
            print('Ghost')
              


if __name__ == "__main__":
    main()
