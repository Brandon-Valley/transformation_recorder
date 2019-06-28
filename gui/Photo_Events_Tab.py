from tkinter import *
from tkinter.ttk import *


import GUI
import Tab


class Photo_Events_Tab(Tab.Tab):
    def __init__(self, master, tab_control):
        self.tab_control = tab_control
    
        Tab.Tab.__init__(self, master)
       
        self.photo_events_____widget_setup()
       
        self.grid_widgets()
		
        
    def photo_events_____widget_setup(self):
        self.photo_events_lf = LabelFrame(self.master, text=" Photo Events: ")
        
        # add btn
        def add_btn_clk(event=None):
            print('in photo events tab, add')
            
        self.add_btn = Button(self.photo_events_lf, text="Add Photo Event", command = add_btn_clk)

        
        # name text box
        def update_add_btn_state(event=None):
            print(' in photo events tab, update add btn state')
        
        self.name_tb = Entry(self.photo_events_lf)
        self.bind_to_edit(self.name_tb, update_add_btn_state)

        
        
    def grid_widgets(self):
        # self.master.grid_columnconfigure(3, weight=1)
        
        self.photo_events_lf.grid(column=1, row=1, sticky='NSEW', padx=5, pady=2, ipadx=5, ipady=5)
        self.name_tb        .grid(column=1, row=100)
        self.add_btn        .grid(column=2, row=100)
        
        
if __name__ == '__main__':
    GUI.main()