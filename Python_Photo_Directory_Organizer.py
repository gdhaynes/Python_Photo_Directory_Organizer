import os
import shutil

photoDirectory = input("Photo directory: ")
for yearFolder in os.listdir(photoDirectory):
    if os.path.isdir(os.path.join(photoDirectory, yearFolder)):
        for subfolder in os.listdir(os.path.join(photoDirectory, yearFolder)):
            if os.path.isdir(os.path.join(photoDirectory, yearFolder, subfolder)):
                if os.path.exists(os.path.join(photoDirectory, yearFolder, subfolder, "Raw")) == False:
                    os.mkdir(os.path.join(photoDirectory, yearFolder, subfolder, "Raw"))
                for item in os.listdir(os.path.join(photoDirectory, yearFolder, subfolder)):
                    if "CR2" in item.upper() or "ARW" in item.upper():
                        if os.path.exists(os.path.join(photoDirectory, yearFolder, "Raw", item)) and os.path.exists(os.path.join(photoDirectory, yearFolder, subfolder, item)):
                            os.remove(os.path.join(photoDirectory, yearFolder, "Raw", item))
                        shutil.move(os.path.join(photoDirectory, yearFolder, subfolder, item), os.path.join(photoDirectory, yearFolder, subfolder, "Raw"))