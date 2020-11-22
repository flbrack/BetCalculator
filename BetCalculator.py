from tkinter import *
from BetTypes import *



#Create a bet calculator class
class BetCalculator:




    #Step 2 and 3: create the first method
    def __init__(self, master):

        '''
        DOCSTRING: Define what to do on initialization
        '''

        #Step 4: Assign reference to the main window of the application
        self.master = master

        #Step 4: Add a name to our application
        master.title("Bet Calculator")

        Label(master, text = "Stake").grid(row=1, column = 1)
        Label(master, text = "Each-Way").grid(row=1, column = 3)
        Label(master, text = "Total Stake").grid(row=2, column=1)
        Label(master, text = "Payout").grid(row=2, column=3)

        self.stakeinput = StringVar()
        Entry(master, width=10, textvariable = self.stakeinput, justify=RIGHT).grid(row=1, column=2)

        self.ewinput = IntVar()
        r1 = Radiobutton(master, variable=self.ewinput, justify=RIGHT).grid(row=1, column=4)

        self.totalstakes = StringVar()
        lblTotalStakes = Label(master, textvariable=self.totalstakes).grid(row=2, column=2)

        self.payout = StringVar()
        lblPayout = Label(master, textvariable=self.payout).grid(row=2, column=4)

        self.totalstakes.set('100')
        self.payout.set('1000')

#Step 5: Execution
if __name__=='__main__':
    
    #Step 6: Create the main window of an application
    root = Tk()
    
    #Step 6: Tell our calculator class to use this window
    my_gui = BetCalculator(root)
    
    #Step 6: Executable loop on the application, waits for user input
    root.mainloop()
