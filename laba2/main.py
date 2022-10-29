from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from colorama import Fore, Back, Style

def main():
    r = Rectangle("синего", 2, 2)
    c = Circle("зеленого", 2)
    s = Square("красного", 2)
    print(r)
    print(c)
    print(s)
    print(Fore.RED + 'Красная строка')
    print(Back.GREEN + Fore.BLACK + 'Черный текст на зеленом')
    print(Back.YELLOW + Fore.RED + 'yellow background')
    print(Style.BRIGHT + Fore.BLUE + 'Вряд ли видно, что тут')
    print(Style.RESET_ALL)
    print('back to normal now')

if __name__ == "__main__":
    main()


