__author__ = 'Barry'
##simple program to auto shutdown windows pc
#simple shutdown
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
class GUI():
    def __init__(self,parent,shutdownsys):
        self.shutdownsys=shutdownsys
        self.parent = parent
        self.parent.title("Shutdown") #This is bar at top on the line with the x to close
        self.frame = Frame(self.parent)
        self.frame.grid(row=0,column=0)

        self.labelfonttitle = ("TkDefaultFont", 14)
        self.shutdowntitle = Label(parent, text="In how many minutes would you like to Auto Shutdown?",)
        self.shutdowntitle.config(font = self.labelfonttitle)
        self.shutdowntitle.grid(row=0, column=0, columnspan=3,sticky=W+E)


        self.other = Label(parent, text="Other (In Minutes)")
        self.other.grid(row=1, column=5, sticky=W+E)

        self.min25 = Button(parent,text="25 Minutes",padx=30, command= lambda: self.value(25))
        self.min25.grid(row=2, column=0, sticky=W+E)


        self.min45 = Button(parent,text="45 Minutes",padx=30,command= lambda: self.value(45))
        self.min45.grid(row=2, column=1, sticky=W+E)

        self.min60 = Button(parent,text="60 Minutes",padx=30,command= lambda: self.value(60))
        self.min60.grid(row=2, column=2, sticky=W+E)

        self.min75 = Button(parent,text="75 Minutes" ,padx=30,command= lambda: self.value(75))
        self.min75.grid(row=2, column=3, sticky=W+E)


        self.min90 = Button(parent,text="90 Minutes",padx=30, command= lambda: self.value(90))
        self.min90.grid(row=2, column=4, sticky=W+E)

        self.user = Entry(parent)
        self.user.grid(row=2, column=5, sticky =W+E)

        self.Enter =Button(parent,text ="Other Shutdown",command =self.cal)
        self.Enter.grid(row=3,column =5 ,sticky =W+E)

        self.error =StringVar()
        self.errorlabel=Label(self.parent,textvariable = self.error)
        self.error.set("")
        self.errorlabel.grid(row=3,column=1,columnspan=3)



    def cal(self):
        success =False
        time = self.user.get()
        try:
            time =int(time)
            success =True

        except ValueError:
            self.error.set("ERROR ,\" {} \" is not a valid number".format(time))

        if success == True:
            self.shutdownsys.run(time)
            self.parent.destroy()



    def value(self,value):
        print(value)
        self.shutdownsys.run(value)
        self.parent.destroy()

class Shutdown():
    def __init__(self):
        self.cancel()
    def run(self,shutdown):
        self.shutdown =shutdown
        self.shutdown = (self.shutdown*60)
        time = ("shutdown -s -t {}".format(self.shutdown))
        print (time)
        os.system(time)

    def cancel(self):
        self.cancel = "shutdown /a"
        os.system(self.cancel)


def main():
    shutdown = Shutdown()
    root = Tk()
    GUI(root,shutdown)
    root.mainloop()



if __name__ == '__main__':
    main()
