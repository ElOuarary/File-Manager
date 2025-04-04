import os
from shutil import move
import sys

from file_types import file_types

# Check for the validity of the folder
def check_folder(folder_path: str) -> None:
    if not os.path.exists(folder_path):
        print(f'{folder_path} does not exists!')
        sys.exit()
    if not os.path.isdir(folder_path):
        print(f'{folder_path} is not a folder!')
        sys.exit()


# Get the source folder absolute path and check for it existence
def set_parameters() -> tuple[str, str]:
    source_folder = input('Enter the absolute path for the source folder: ')
    check_folder(source_folder)
    destination_folder = input('Enter the absolute path for the destination folder: ')
    check_folder(destination_folder)
    return (source_folder, destination_folder)


# Create the categorical folders
def create_folders(destination_path: str) -> None:
    for category in file_types.keys():
        folder_path = os.path.join(destination_path, category)
        if os.path.exists(folder_path):
            print(f'{category} folder already exists!')
            continue
        os.makedirs(folder_path)


# Organize the files
def organize(source_folder: str, destination_folder: str) -> None:
    source_dir = os.listdir(source_folder)
    for element in source_dir:
        element_path = os.path.join(source_folder, element)
        
        if os.path.isdir(element):
            continue
        
        _, extension = os.path.splitext(element_path)
        category = ''
        for cat, extensions in file_types.items():
            if extension.lower() in extensions:
                category = cat
                break
        
        destination_to_move = os.path.join(destination_folder, category, element)
        move(element_path, destination_to_move)
        print(f'{element} move from {element_path} -> {os.path.join(destination_folder, category)}')
        

source_folder, destination_folder = set_parameters()