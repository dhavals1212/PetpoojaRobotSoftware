#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
from PIL import ImageTk, Image, ImageOps
from tkinter import font
import webbrowser as wb
import requests
import threading

__author__ = 'Dhaval Shukla'
__copyright__ = 'Copyright(C) 2022 Dhaval Shukla'
__credits__ = ['Dhaval Shukla', 'Raj Mehta', 'Dharmik Prajapati', 'Aanal Patel', 'Pranav Patel', 'Deep Joshi']
__license__ = 'MIT License(MIT)'
__version__ = '1.1'
__maintainer__ = 'Dhaval Shukla'
__email__ = 'dhaval.shukla912@gmail.com'
__status__ = 'Beta'
_AppName_ = 'Robot Software'

class Main:
    def __init__(self, parent):
        def check_updates():
            try:
                # -- Online version of the file.
                # -- Replace the url of the older one with the one below.
                response = requests.get(
                    'https://raw.githubusercontent.com/dhavals1212/PetpoojaRobotSoftware/main/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    mb.showinfo('Software Update', 'A new update is available!')
                    mb1 = mb.askyesno('Update available', f'{_AppName_} v{__version__} can be updated to version {data}\n\nWould you like to update now?')
                    if mb1 is True:
                        # Replace the file with your url online with this below:
                        wb.open_new_tab('https://github.com/dhavals1212/PetpoojaRobotSoftware/blob/main/Updates/RobotSoftware.py?raw=true')
                        parent.destroy()
                    else:
                        pass
                else:
                    mb.showinfo('Software update', 'No new updates are available.')
            except Exception as e:
                mb.showinfo('Software update', 'Unable to check for update, Error:' + str(e))

        button1 = ttk.Button(parent, text='Update', command=check_updates)
        button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def main():
    root = tk.Tk()
    root.title(_AppName_ + ' ' + str(__version__))
    root.geometry('400x150')
    root.resizable(width=True, height=True)
    label = tk.Label(root, text="Hello Dhaval")
    label.pack()
    Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
