import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageOps
from tkinter import font
import webbrowser
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

_AppName_ = 'Food server robot software'

class Main:
    def __init__(self, parent):
        def check_updates():
            try:
                # -- Online version of the file.
                # -- Replace the url of the older one with the one below.
                response - requests.get(
                    'https://github.com/dhavals1212/Food-server-robot-software/blob/main/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    messagebox.showinfo('Software Update', 'A new update is available!')
                    mb1 = messagebox.askyesno('Update available', f'{_AppName_} {__version__} can be updated to version {data}')
                    if mb1 is True:
                        # Replace the file with your url online with this below:
                        webbrowser.open_new_tab('https://github.com/dhavals1212/Food-server-robot-software/blob/main/Updates/RobotSoftware.exe?raw=true')
                        parent.destroy()
                    else:
                        pass
                else:
                    messagebox.showinfo('Software update', 'No new updates are available.')
            except Exception as e:
                messagebox.showinfo('Software update', 'Unable to check for update, Error:' + str(e))

        button1 = ttk.Button(parent, text='Check for updates', command=check_updates)
        button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def main():
    root = tk.Tk()
    root.title(_AppName_ + ' ' + str(__version__))
    root.geometry('400x150')
    root.resizable(width=False, height=False)
    label = tk.Label(root, text="Hello Dhaval")
    label.pack()
    root.wm_iconbitmap('Images/petpooja.ico')#Path stored locally on PC.
    Main(root)
    root.mainloop()

if __name__ == '__main__':
    main()
