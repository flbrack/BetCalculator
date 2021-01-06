from tkinter import *
from tkinter import ttk
from BetTypes import *



#Create a bet calculator class
class BetCalculator:
    
    def __init__(self, master):

        self.master = master
        master.title("Bet Calculator")

        #----------Top Frame
        self.topframe = Frame(master)


        Label(self.topframe,justify=LEFT, text = "Stake").grid(row=0, column = 0, sticky=W)
        
        self.stakeinput = StringVar()
        Entry(self.topframe, width=10, textvariable = self.stakeinput, justify=LEFT).grid(row=0, column=1)

        Label(self.topframe, text = "Each-Way").grid(row=0, column = 2)

        self.ewinput = IntVar()
        r1 = Radiobutton(self.topframe, text="Yes", variable=self.ewinput, value=True).grid(row=0,column=3)
        r2 = Radiobutton(self.topframe, text="No",variable=self.ewinput, value=False).grid(row=0,column=4)

        Label(self.topframe, text="Bet Type").grid(row=1,column=0)

        self.bettype = StringVar()
        choices = ["Single/Accum", "Lucky 15 Type", "Yankee Type"]
        self.bettype.set("Pick an option")
        #ttk.Combobox(self.topframe, width=10 ,textvariable=self.bettype, values=choices, state='readonly').grid(row=1,column=1)
        OptionMenu(self.topframe, self.bettype, *choices).grid(row=1,column=1)

        Label(self.topframe, text="No. of Selections").grid(row=1, column=2)

        self.selections = StringVar()
        self.selections.set('4')
        selectchoices = [str(i) for i in range(1,9)]
        #ttk.Combobox(self.topframe, width=3, values=selectchoices, state="readonly").grid(row=1, column=3)
        OptionMenu(self.topframe,  self.selections, *selectchoices).grid(row=1, column=3)

        #----------Middle Frame
        self.midframe = Frame(master)

        def showMidframes(rows=1):

            Label(self.midframe, text="Odds").grid(row=rows, column = 0)
        
            self.odds = StringVar()
            Entry(self.midframe, width=5, textvariable = self.odds, justify = RIGHT).grid(row=rows, column=1)
        
            Label(self.midframe, text="E/W Terms").grid(row=rows, column = 2)

            self.ewterms = StringVar()
            Entry(self.midframe, width=5, textvariable = self.ewterms, justify=RIGHT).grid(row=rows, column=3)

            Label(self.midframe, text="Win?").grid(row=rows, column=4)

            self.win = StringVar()
            self.win.set("Win")
            winplace = ["Win", "Place"]
            OptionMenu(self.midframe, self.win, *winplace).grid(row=rows, column=5)

        
        for i in range(1,int(self.selections.get())+1):
            showMidframes(rows=i)

        #----------Bottom Frame
        self.bottomframe = Frame(master)

        Label(self.bottomframe, text = "Total Stake").grid(row=1, column=0)
        Label(self.bottomframe, text = "Payout").grid(row=1, column=2)

        self.totalstakes = StringVar()
        lblTotalStakes = Label(self.bottomframe, width=10, textvariable=self.totalstakes).grid(row=1, column=1)

        self.payout = StringVar()
        lblPayout = Label(self.bottomframe,width=10, textvariable=self.payout).grid(row=1, column=3)

        btComputeStakes = Button(self.bottomframe, text = "Compute Payout", command=self.computePayout).grid(row=0, column = 0,columnspan=2)

        

        self.topframe.pack(side=TOP)
        self.midframe.pack()
        self.bottomframe.pack(side=BOTTOM)

        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        
        
    #def Create Midframes(self):


    def computePayout(self):
        wins = {"Win":True,"Place":False}

        if self.bettype.get()=="Single/Accum":
            bet = Accum(stakes = float(self.stakeinput.get()), odds=[float(self.odds.get())], ew=self.ewinput.get(), ewterms=[float(self.ewterms.get())],winner=[wins[self.win.get()]])
        
        elif self.bettype.get()=="Lucky 15 Type":
            bet = LuckyFifteen(stakes = float(self.stakeinput.get()), odds=[float(self.odds.get())], ew=self.ewinput.get(), ewterms=[float(self.ewterms.get())],winner=[wins[self.win.get()]])

        elif self.bettype.get()=="Yankee Type":
            bet = Yankee(stakes = float(self.stakeinput.get()), odds=[float(self.odds.get())], ew=self.ewinput.get(), ewterms=[float(self.ewterms.get())],winner=[wins[self.win.get()]]) 

        self.totalstakes.set(bet.totalstakes())
        self.payout.set(bet.payout())


#Step 5: Execution
if __name__=='__main__':
    
    #Step 6: Create the main window of an application
    root = Tk()
    
    #Step 6: Tell our calculator class to use this window
    my_gui = BetCalculator(root)
    
    #Step 6: Executable loop on the application, waits for user input
    root.mainloop()
