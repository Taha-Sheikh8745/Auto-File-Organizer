import os
import shutil

# Customize your folder path here
folder_path = 'C:/Users/jave'

# Define folder types
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mkv'],
    'Music': ['.mp3', '.wav'],
    'Code': ['.py', '.js', '.html', '.css'],
    'Archives': ['.zip', '.rar']
}

# Make folders and move files
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()
        for folder, extensions in file_types.items():
            if ext in extensions:
                folder_dest = os.path.join(folder_path, folder)
                os.makedirs(folder_dest, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_dest, filename))
                break

print("✅ Files organized successfully!")
