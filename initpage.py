from tkinter import *
from tkinter.messagebox import *
from mainpage import *
from fileinputpage import *
class InitPage(object):
    def __init__(self,master = None):
            self.root = master
            self.root.geometry(('%dx%d' % (300, 180)))
            self.username = StringVar()
            self.password = StringVar()
            self.createPage()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page).grid(row=0, stick = W)
        Label(self.page, text = 'Username').grid(row=1, stick=W, pady = 10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text = 'Password:').grid(row=2, stick=W, pady = 10)
        Entry(self.page, textvariable=self.password, show = '*').grid(row=2, column=1 ,stick= E)
        Button(self.page, text = 'Login', command = self.loginCheck).grid(row=3, stick=W, pady =10)
        Button(self.page, text = 'Exit', command = self.page.quit).grid(row=3, column = 1, stick = E)

    def loginCheck(self):
        name = self.username.get()
        secret = self.password.get()
        if name == 'BigBrain' and secret == 'BigBrain':
            self.page.destroy()
            FileInputPage(self.root)
        else:
            showinfo(title= 'Wrong', message='Wrong Password or Username(hint project name)！')