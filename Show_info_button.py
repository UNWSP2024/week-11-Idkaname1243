import tkinter
import tkinter.messagebox
class Mygui:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Name Button")
        self.namebutton = tkinter.Button(self.mainwindow,text='Show Info',command=self.displayname)
        self.exitbutton = tkinter.Button(self.mainwindow, text='Exit',command=self.mainwindow.destroy)
        self.namebutton.pack()
        self.exitbutton.pack()
        tkinter.mainloop()
    def displayname(self):
        tkinter.messagebox.showinfo('Name and Address', 'Name:   Anders Kjelland Address: 1280 county road J west Mn 55126')
if __name__ == '__main__':
    mygui = Mygui()
