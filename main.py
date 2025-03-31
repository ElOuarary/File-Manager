import os
from shutil import move
import sys


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
    destination_folder = input('Enter the absolute path for the destination folder: ')
    return (source_folder, destination_folder)


source_folder, destination_folder = set_parameters()
if not os.path.exists(source_folder):
    print(f'{source_folder} does not exists in your device.')
    sys.exit()


# Set the category for the different files type
file_types = {
    'Text': ['.txt', '.rtf', '.docx', '.csv', '.doc', '.wps', '.wpd', '.msg', '.pdf'],
    'Image': ['.jpg', '.png', '.webp', '.gif', '.tif', '.bmp', '.eps'],
    'Audio': ['.mp3', '.wma', '.snd', '.snd', '.wav', '.ra', '.au', '.aac'],
    'Video': ['.mp4', '3gp', '.avi', '.mpg', '.mov', '.wmv'],
    'Program': ['.c', '.cpp', '.java', '.py', '.js', '.ts', '.cs', '.swift', '.dta', '.pl', '.sh', '.bat', '.com', '.exe'],
    'Comressed': ['.rar', '.zip', '.hqx', '.arj', '.tar', '.arc', '.sit', '.gz', '.z'],
    'Web Page': ['.html', 'htm', '.xhtml', '.asp', '.css', '.aspx', '.rss']
}


# Create the categorical folders
for category in file_types.keys():
    folder_path = os.path.join(source_folder, category)
    if os.path.exists(folder_path):
        answer = input(f'{category} alrady exists do you want to overwrite it [Y/N]: ').lower()
        if answer == 'n':
            continue
        else:
            os.removedirs(folder_path)
    os.makedirs(folder_path, exist_ok=True)
    

# Get the list of files and folder in the source folder
ls_dir = os.listdir(source_folder)

# Organize the files
for element in ls_dir:
    element_path = os.path.join(source_folder, element)
    
    if os.path.isdir(element):
        continue
    
    _, extension = os.path.splitext(element_path)
    
    category = ''
    for cat, extensions in file_types.items():
        if extension.lower() in extensions:
            category = cat
            break
    
    destination_path = os.path.join(destination_folder, category, element)
    move(element_path, destination_path)