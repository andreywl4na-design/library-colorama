import colorama

help(colorama)

from colorama import init, Fore, Back, Style

init()

print(Fore.RED + 'Червоний текст')
print(Back.YELLOW + 'Жовтий фон')
print(Style.BRIGHT + 'Яскравий текст')
print(Style.RESET_ALL + 'Звичайний текст')