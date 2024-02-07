import sys
from pathlib import Path

rec_count: int = 0

def main(way: str) -> None:
    global rec_count
    rec_count += 1
    direct = Path(way)
    if direct.exists():
        print(f"Директорія {direct.name} : ")
        for element in direct.iterdir():
            if element.is_dir():
                # print(f"\tДиректорія {element.name} : ")
                main(element)
            elif element.is_file():
                print(f"{'\t'*rec_count}Файл {element.name}")
            else:
                print("Невизначений формат об'єкта")
    else:
        print("Директорія не існує")
    rec_count -=1 if rec_count > 0 else rec_count

# if __name__ == "__main__":
    # if len(sys.argv) < 2:
    #     print("Введіть шлях до папки в якості аргументу командного рядка")
    #     sys.exit(1)
    # way = sys.argv[1]

main("D:\\Programs\\fop")