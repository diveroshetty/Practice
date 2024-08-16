
import os

import shutil
from tkinter import Variable

#define the directory and connect the path. expanduser just lets you type the name without defining the path
directory = os.path.join(os.path.expanduser("~"), "Downloads")

extensions = {
    ".jpg" : "_Images",
    ".jpeg" : "_Images",
    ".jfif" : "_Images",
    ".tif" : "_Images",
    ".png" : "_Images",
    ".gif" : "_Images",
    ".3dm" : "_DesignFiles",
    ".dwg" : "_DesignFiles",
    ".indd" : "_DesignFiles",
    ".pdf" : "_PDF",
    ".mp3" : "_AV",
    ".mp4" : "_AV",
    ".wav" : "_AV",
    ".mov" : "_AV",
    ".rar" : "_Delete",
    ".pkf" : "_Delete",
    ".docx" : "_Text",
    ".doc" : "_Text",
    ".xlsx" : "_Excel",
    ".zip" : "_Zip",
    ".exe" : "_SetupFiles",
    ".xls" : "_Excel"
    }

#loop over every file name in the directory
for filename in os.listdir (directory):
    file_path = os.path.join (directory, filename) #the defines the file path and makes sure we are only looking at files and not directories
    
    if os.path.isfile(file_path): #once you find a file
        extension = os.path.splitext(filename)[1].lower() #make only the extension lower case. split- splits the file name at . by specifying the list index
        
        if extension in extensions: #if extension matches the list of extensions
            folder_name = extensions[extension] #folder name will be a dictionary of the specified extensions if we find extension in extensions
            
            folder_path = os.path.join(directory, folder_name) #creates a new folder path in the directory based on folder name specified above
            #os.makedirs(folder_path, exist_ok = True) #makedirs creates a new directory if the folder name is found and folder path is made
            
            destination_path = os.path.join(folder_path, filename) #specify location of the file
            shutil.move(file_path, destination_path) #move from downloads to new destination path
            
            print(f"Moved {filename} to {folder_name} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        print(f"Skipped {filename}. It is a directory.")


print("File Organization Complete")

    



