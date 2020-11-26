from tkinter import *

class Example():
    def __init__(self, master):

        self.master = master

        
        master.title("some application")

        # menu left
        self.menu_left = Frame(master, width=150, bg="#ababab")
        self.menu_left_upper = Frame(self.menu_left, width=150, height=150, bg="red")
        self.menu_left_lower = Frame(self.menu_left, width=150, bg="blue")

        self.test = Label(self.menu_left_upper, text="test")
        self.test.pack()

        self.menu_left_upper.pack(side="top", fill="both", expand=True)
        self.menu_left_lower.pack(side="top", fill="both", expand=True)

        # right area
        self.some_title_frame = Frame(master, bg="#dfdfdf")

        self.some_title = Label(self.some_title_frame, text="some title", bg="#dfdfdf")
        self.some_title.pack()

        self.canvas_area = Canvas(master, width=500, height=400, background="#ffffff")
        self.canvas_area.grid(row=1, column=1)

        # status bar
        self.status_frame = Frame(master)
        self.status = Label(self.status_frame, text="this is the status bar")
        self.status.pack(fill="both", expand=True)

        self.menu_left.grid(row=0, column=0, rowspan=2, sticky="nsew")
        self.some_title_frame.grid(row=0, column=1, sticky="ew")
        self.canvas_area.grid(row=1, column=1, sticky="nsew") 
        self.status_frame.grid(row=2, column=0, columnspan=2, sticky="ew")

        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(1, weight=1)

        




if __name__=='__main__':
    
    #Step 6: Create the main window of an application
    root = Tk()
    
    #Step 6: Tell our calculator class to use this window
    my_gui = Example(root)
    
    #Step 6: Executable loop on the application, waits for user input
    root.mainloop()
