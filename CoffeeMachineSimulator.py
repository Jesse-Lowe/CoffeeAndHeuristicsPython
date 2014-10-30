'''
Created on 30 Oct 2014

@author: Jesse
'''

import Tkinter
from Tkinter import Tk
from multiprocessing.managers import State
from Tkconstants import DISABLED

class coffeeMakerGUI():
    
    
    
    def __init__(self): 
            
            self.mainWindow = Tk()
            
            powerOn = False
            potFull = False
            potOn = False
            boilerFull = False
            boilerOn = False
            heaterOn = False
            valveClosed = False
           
            
            def powerToggle():
                if powerOn == False:
                    print ("Power On")
                    powerOn =True
                else:
                    print ("Power Off")
            
            def potOnToggle():
                if potOn == False:
                    print ("Pot On")
                    potOn = True
                else:
                    print ("Pot Off")
                    
            def fillBoiler():
                if boilerFull == False:
                    print ("Boiler filled")
                    boilerFull = True
                else:
                    print ("Boiler already full")
                    
            def emptyPot():
                if potFull == False:
                    print ("Pot already empty")
                else:
                    print ("Pot emptyed")
                    
            def runBrew():
                print("Brewing")
                print("Finished Brewing")
            
            def heaterOnToggle():
                if heaterOn == False:
                    print ("Heater on.")
                    heaterOn = True
                else:
                    print ("heater off.")
                    
            def boilerOnToggle():
                if boilerOn == False:
                    print ("Boiler on.")
                    boilerOn = True
                else:
                    print ("Boiler off.")
                    
            def boilerFillEmpty():
                if boilerFull == False:
                    print ("Boiler filled")
                    boilerFull = True
                else:
                    print("Boiler Emptied")
                    boilerFull = False

            def potFillEmpty():
                if potFull == False:
                    print ("Pot filled")
                    potFull = True
                else:
                    print("Pot Emptied")
                    potFull = False
                    
            def valveOpenClose():
                if valveClosed == False:
                    print ("Valve closed")
                    valveClosed = True
                else:
                    print("Valve opened")
                    valveClosed = False       
            
            self.powerButton = Tkinter.Button(self.mainWindow, text = "Power on.", command = powerToggle)
            self.potPlacementButton = Tkinter.Button(self.mainWindow, text = "Pot on.", command = potOnToggle)
            self.fillBoilerButton = Tkinter.Button(self.mainWindow, text = "Fill Boiler", command = fillBoiler)
            self.brewButton = Tkinter.Button(self.mainWindow, text = "Brew.", command = runBrew)
            self.emptyPotButton = Tkinter.Button(self.mainWindow, text = "Empty Pot.", command = emptyPot)
            self.animationFrame = Tkinter.Canvas(self.mainWindow, width = 400, height = 400)
            self.heaterPowerButton = Tkinter.Button(self.mainWindow, text = "Heater On", command = heaterOnToggle)
            self.boilerPowerButton = Tkinter.Button(self.mainWindow, text = "Boiler On", command = boilerOnToggle)
            self.boilerFillEmptyButton = Tkinter.Button(self.mainWindow, text = "Fill boiler", command = boilerFillEmpty)
            self.potFillEmptyButton = Tkinter.Button(self.mainWindow, text = "Fill pot", command = potFillEmpty)
            self.valveOpenCloseButton = Tkinter.Button(self.mainWindow, text = "Close Valve", command = valveOpenClose)
            self.textOutputFrame = Tkinter.Frame(self.mainWindow, height = 100)
            self.textOutput = Tkinter.Text(self.textOutputFrame)
            self.textScroller = Tkinter.Scrollbar(self.textOutputFrame, command = self.textOutput.yview)
            
            self.brewButton.grid(row = 3, column = 0, sticky = "nsew") 
            self.emptyPotButton.grid(row = 4, column = 0, sticky = "nsew")
            self.fillBoilerButton.grid(row = 2, column = 0, sticky = "nsew")
            self.potPlacementButton.grid(row = 1, column = 0, sticky = "nsew")
            self.powerButton.grid(row = 0, column = 0, sticky = "nsew")
            self.animationFrame.grid(row = 0, column = 1, columnspan = 5, rowspan = 5) 
            self.heaterPowerButton.grid(row = 0, column = 7, sticky = "nsew")
            self.boilerPowerButton.grid(row = 1, column = 7, sticky = "nsew")
            self.boilerFillEmptyButton.grid(row = 2, column = 7, sticky = "nsew")
            self.potFillEmptyButton.grid(row = 3, column = 7, sticky = "nsew")
            self.valveOpenCloseButton.grid(row = 4, column = 7, sticky = "nsew")
            self.textOutputFrame.grid(row = 6, column = 0, columnspan = 8, rowspan = 3)
            self.textOutput.pack(side = "left")
            self.textScroller.pack(side = "left", fill = "y")
            
            self.textOutput['yscrollcommand'] = self.textScroller.set
            self.textOutput.config(state = DISABLED)
            
            self.mainWindow.resizable(width = False, height = False)
            
            self.mainWindow.mainloop()
            

                    
                          
            
            
coffeeMakerGUI()