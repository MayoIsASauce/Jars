# Collect all loose files and place in alphabatized folders

from pathlib import Path
from os import listdir, mkdir
from os.path import isfile, join


class GnomeClutter(object):
    def __init__(self, folder:str) -> None:
        self.folder = folder+'/'
        self.loose_dict = {}
        self.loose_files = [file for file in listdir(folder) if isfile(join(folder, file))]

        print(self.loose_files, len(self.loose_files), end="\n\n")

        for file in self.loose_files:
            if not file[0].upper() in list(self.loose_dict.keys()):
                self.loose_dict[file[0].upper()] = []
            self.loose_dict[file[0].upper()].append(file)

    def filename_validation(self, file, num):
        try:
            if num == 1:
                Path(self.folder+file).rename(self.folder+file[0]+"/"+file)
            else:
                Path(self.folder+file).rename(".".join((self.folder+file[0]+"/"+file).split('.')[:-1])+"_"+str(num)+"(DUP)."+(self.folder+file[0]+"/"+file).split('.')[-1])
        except FileExistsError:
            print(f'Duplicate found: {file +("_"+str(num) if num > 1 else "")} attempting {file+"_"+str(num)}')
            self.filename_validation(file, num+1)
        
        return file + ("_"+str(num) if num > 1 else "")

    def prepare(self):
        for folder_key in self.loose_dict.keys():
            try:
                mkdir(self.folder+folder_key)
                print(f'Folder needed: {folder_key}')
                print(f'Folder created: {self.folder+folder_key}', end="\n\n")
            except FileExistsError:
                print(f'Folder exists: {self.folder+folder_key}', end="\n")
            
        return self
        
    def organize(self) -> None:
        folder_DNE = []
        count: int = 0
        print("")
        for file in self.loose_files:
            try:
                if self.folder+file[0]+'/' not in folder_DNE:
                    new_name = self.filename_validation(file, 1)
                    print(f'{count}: [{new_name}] moved to [{self.folder+file[0]}/]')
                    count += 1
            except FileNotFoundError:
                print(f'Folder not found: {self.folder+file[0]}/')
                folder_DNE.append(f'{self.folder+file[0]}/')

        return None

# Create the interface

import tkinter as tk
from tkinter import filedialog

HEIGHT = 500
WIDTH = 500

window = tk.Tk()

folder_selected = ""

header = tk.Label(window, text="matt's super cool declutterer")
header.configure(font=('Helvetica bold', 14))
header.pack()


def select_folder(folder="-[0x410]"):
    def organize():
        GnomeClutter(folder).prepare().organize()
        window.quit()

    if folder != "-[0x410]":
        tk.Button(window, text="BEGIN", command=organize).place(x=(WIDTH/2)-20, y=HEIGHT-50)
        return None

    folder_name = filedialog.askdirectory()
    tk.Label(window, text="Selected Folder: "+folder_name).place(x=20, y=130)
    return select_folder(folder_name)

tk.Button(window, text="Select Folder", command=select_folder).place(x=(WIDTH/2)-20, y=100)
tk.Label(window, text="Folder: ").place(x=(WIDTH/2)-80, y=100)


window.geometry(f'{WIDTH}x{HEIGHT}+300+200')
window.title("matts super cool declutterer")
window.mainloop()