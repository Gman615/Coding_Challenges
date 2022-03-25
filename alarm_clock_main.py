import shutil
import os, sys, time
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time as tm

#import alarm_clock_func
#import alarm_clock_gui

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,200)
        self.master.maxsize(500,200)
        self.master.title("Alarm Clock")
        self.master.configure(bg="black")
        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        arg = self.master
        digital_time = tm.strftime("%I:%M %p")
        
        self.txt_path = tk.Label(self.master,width=41,height=1,text=digital_time)
        self.txt_path.grid(row=1,column=1,padx=(25,0),pady=(20,10),sticky=W)
        #self.btn_time = tk.Button(self.master,width=12,height=1,text="current time",command=lambda: current_time(self))
        #self.btn_time.grid(row=1,column=0,padx=(25,0),pady=(20,10))

        #alarm_clock_gui.load_gui(self)
def ask_quit(self):
    if messagebox.askokcancel("Exit Program", "Do you want to close?"):
        # closes the app
        self.master.destroy()


                        


    
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
        
