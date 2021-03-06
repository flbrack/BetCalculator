from tkinter import *
from BetTypes import *
from functools import reduce

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

        OptionMenu(self.topframe, self.bettype, *choices).grid(row=1,column=1)

        Label(self.topframe, text="No. of Selections").grid(row=1, column=2)

        self.selections = StringVar()
        self.selections.set('4')
        selectchoices = [str(i) for i in range(1,9)]

        def ChangeMidFrames(event):
            for widget in self.midframe.winfo_children():
                widget.destroy()
            for i in range(1,int(event)+1):
                showMidframes(rows=i)
        
        OptionMenu(self.topframe,  self.selections, *selectchoices, command=ChangeMidFrames).grid(row=1, column=3)

        def storewin(event):
            wins = {"Win":True,"Place":False}       
            self.listOfWins.append(wins[event])

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
            OptionMenu(self.midframe, self.win, *winplace, command=storewin).grid(row=rows, column=5)

        
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
        
        self.listOfOdds = []
        self.listOfEWTerms = []
        self.listOfWins = [True]
        

    def computePayout(self):
        
        i=0
        for widget in self.midframe.winfo_children():
            if widget.winfo_class() == 'Entry' and i%2==0:
                self.listOfOdds.append(widget.get())
                i+=1
            elif widget.winfo_class() == 'Entry' and i%2==1:
                self.listOfEWTerms.append(widget.get())
                i+=1

        self.listOfOdds = [reduce(lambda x,y:x/y, list(map(float,item.split('/')))) for item in self.listOfOdds]
        self.listOfEWTerms = [reduce(lambda x,y:x/y, list(map(float,item.split('/')))) for item in self.listOfEWTerms]      
        
        if self.bettype.get()=="Single/Accum":
            bet = Accum(stakes = float(self.stakeinput.get()), odds=self.listOfOdds, ew=self.ewinput.get(), ewterms=self.listOfEWTerms, winner=self.listOfWins)
        
        elif self.bettype.get()=="Lucky 15 Type":
            bet = LuckyFifteen(stakes = float(self.stakeinput.get()), odds=self.listOfOdds, ew=self.ewinput.get(), ewterms=self.listOfEWTerms ,winner=self.listOfWins)

        elif self.bettype.get()=="Yankee Type":
            bet = Yankee(stakes = float(self.stakeinput.get()), odds=self.listOfOdds, ew=self.ewinput.get(), ewterms=self.listOfEWTerms,winner=self.listOfWins) 

        self.totalstakes.set(bet.totalstakes())
        self.payout.set(round(bet.payout(),2))


#Execution
if __name__=='__main__':
    
    #Step 6: Create the main window of an application
    root = Tk()
    
    #Step 6: Tell our calculator class to use this window
    my_gui = BetCalculator(root)
    
    #Step 6: Executable loop on the application, waits for user input
    root.mainloop()
