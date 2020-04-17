from tkinter import *
from view import *

class MainPage(object):
    def __init__(self,master=None):
        self.root = master
        self.root.geometry('%dx%d' % (600, 400))
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)
        self.queryPage = ExistedDataFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)

        self.inputPage.pack()
        menubar = Menu(self.root)
        menubar.add_command(label = '数据录入', command = self.inputData)
        menubar.add_command(label = '查询', command = self.queryData)
        menubar.add_command(label = '统计', command = self.countData)
        menubar.add_command(label = '关于', command = self.aboutDisp)
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
