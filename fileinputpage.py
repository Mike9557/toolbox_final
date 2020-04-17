from tkinter import *
from view import *
class FileInputPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('%dx%d' % (900, 600))
        self.createPage()
    def createPage(self):
        self.inputPage = InputFrame(self.root)
        self.queryPage = ExistedDataFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)

        self.inputPage.pack()
        menubar = Menu(self.root)
        menubar.add_command(label='Joint Attention New Dataset', command=self.inputData)
        menubar.add_command(label='Joint Attention Existed Dataset', command=self.queryData)
        menubar.add_command(label='Waiting For Implementation', command=self.countData)
        menubar.add_command(label='Waiting For Implementation', command=self.aboutDisp)
        self.root['menu'] = menubar

    def inputData(self):
        self.inputPage.pack()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def queryData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack()
        self.countPage.pack_forget()
        self.aboutPage.pack_forget()

    def countData(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack()
        self.aboutPage.pack_forget()

    def aboutDisp(self):
        self.inputPage.pack_forget()
        self.queryPage.pack_forget()
        self.countPage.pack_forget()
        self.aboutPage.pack()