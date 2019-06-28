from tkinter import *
from tkinter.ttk import *


import GUI
import Tab


class Run_Tab(Tab.Tab):
    def __init__(self, master, tab_control):
        self.tab_control = tab_control
    
        Tab.Tab.__init__(self, master)
       
        self.grid_widgets()
		
    def grid_widgets(self):
        # self.master.grid_columnconfigure(3, weight=1)
        pass
    
        
        
        
if __name__ == '__main__':
    GUI.main()