import tkinter
import tkinter.messagebox
class Mygui:
    def __init__(self):
        self.mainwindow = tkinter.Tk()
        self.mainwindow.title("Favorite Saying")
        self.label = tkinter.Label(self.mainwindow,text = '“Those who cannot remember the past are condemned to repeat it.” – George Santayana',borderwidth=100,relief='raised',)
        self.label.pack(side='left')
        tkinter.mainloop()
if __name__ == '__main__':
    mygui = Mygui()
