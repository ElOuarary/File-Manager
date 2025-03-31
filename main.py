import os
from shutil import move

source_folder = 'C:\\Users\\dell\\Downloads'

# Set the category for different files type
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
    os.makedirs(folder_path, exist_ok=True)
    

# Manage the files
ls_dir = os.listdir(source_folder)

for element in ls_dir:
    element_path = os.path.join(source_folder, element)
    
    if os.path.isdir(element):
        continue
    
    _, extension = os.path.splitext(element_path)
    
    category = ''
    for cat, extensions in file_types.items():
        if extension in extensions:
            category = cat
            break
    
    destination_path = os.path.join(source_folder, category, element)
    move(element_path, destination_path)