File Organizer using Python

import os import shutil

File types dictionary

file_types = { "Images": ['.jpg', '.jpeg', '.png'], "Documents": ['.pdf', '.docx', '.txt'], "Videos": ['.mp4', '.mov', '.mkv'], "Music": ['.mp3', '.wav'], "Archives": ['.zip', '.rar'] }

def organize_files(folder_path): for filename in os.listdir(folder_path): name, extension = os.path.splitext(filename) if extension == "": continue

moved = False
    for folder, extensions in file_types.items():
        if extension.lower() in extensions:
            folder_path_full = os.path.join(folder_path, folder)
            if not os.path.exists(folder_path_full):
                os.makedirs(folder_path_full)
            shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path_full, filename))
            moved = True
            break

    if not moved:
        others_path = os.path.join(folder_path, "Others")
        if not os.path.exists(others_path):
            os.makedirs(others_path)
        shutil.move(os.path.join(folder_path, filename), os.path.join(others_path, filename))

if name == "main": path = input("Enter the folder path: ") if os.path.exists(path): organize_files(path) print("Files Organized Successfully!") else: print("Invalid Path. Please check again.")

