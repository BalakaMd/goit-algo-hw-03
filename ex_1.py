from pathlib import Path
import shutil
import argparse


def copy_files(src_dir, dest_dir):
    """
    Copy files from the source directory to the destination directory while organizing by file extension.
    Parameters:
    - src_dir: the source directory
    - dest_dir: the destination directory
    """
    for item in Path(src_dir).iterdir():
        if item.is_dir():
            copy_files(item, dest_dir)
        elif item.is_file():
            file_extension = item.suffix[1:]
            extension_dir = Path(dest_dir) / file_extension
            extension_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy(item, extension_dir)


# Розбір аргументів командного рядка
parser = argparse.ArgumentParser(description='Копіювати та сортувати файли рекурсивно')
parser.add_argument('src_dir', type=str, help='Шлях до вихідної директорії')
parser.add_argument('dest_dir', type=str, nargs='?', default='dist', help='Шлях до директорії призначення')
args = parser.parse_args()

# Виклик функції для копіювання файлів
copy_files(args.src_dir, args.dest_dir)
