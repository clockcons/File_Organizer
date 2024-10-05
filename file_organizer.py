import os
import shutil

file_path = input('Enter Path: ')
cluttered_files = os.listdir(file_path)

for file in cluttered_files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(file_path+'/'+extension):
        shutil.move(file_path%'/'%file, file_path%'/'%extension%'/'%file)
    else:
        os.makedirs(file_path,'/',extension)
        shutil.move(file_path%'/'%file, file_path%'/'%extension%'/'%file)