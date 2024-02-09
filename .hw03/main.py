import sys
from pathlib import Path
from colorama import init, Fore, Back, Style

init()
rec_count: int = 0

def main(way: str) -> None:
    global rec_count
    rec_count += 1
    direct = Path(way)
    if direct.exists():
        print(Back.MAGENTA + Fore.BLACK + f"{'\t'*(rec_count-1)}Директорія {direct.name} : " + Style.RESET_ALL)
        for element in direct.iterdir():
            if element.is_dir():
                main(element)
            elif element.is_file():
                print(Fore.CYAN + f"{'\t'*rec_count}Файл {element.name}" + Style.RESET_ALL)
            else:
                print("Невизначений формат об'єкта")
    else:
        print("Директорія не існує")
    rec_count -=1 if rec_count > 0 else rec_count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Введіть шлях до папки в якості аргументу командного рядка")
        sys.exit(1)
    way = sys.argv[1]
    main(way)

# main("D:\\Programs\\fop")