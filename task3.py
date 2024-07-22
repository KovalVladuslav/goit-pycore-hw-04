import sys
from pathlib import Path
from colorama import init, Fore

def show_roadmap_file(directory, prefix=""):        
    for item in directory.iterdir():
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}/")
            show_roadmap_file(item, prefix + "    ")
        elif item.is_file():
            print(f"{prefix}{Fore.GREEN}{item.name}")
                
if __name__ == "__main__":
    try:
        input_path = sys.argv[1]

        directory = Path(input_path)

        init()

        if not directory.exists():
            print(f"{directory} не існує")
        if not directory.is_dir():
            print(f"{Fore.RED}{directory} не є директорією")
        else:
            show_roadmap_file(directory)

    except IndexError:
        print("Будь ласка, вкажіть шлях як аргумент командного рядка.")
    except Exception as e:
        print(f"Сталася помилка: {e}")
