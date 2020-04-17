from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from joint_attention_analysis import*
from elasticsearch_client import *
from eyeTracker_Subject_Analysis import*
from eyeTracker_Subject import *
class fileInputFrame(Frame):
    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.root = master
        self.fileName = StringVar()
        self.sheetName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row = 0, stick = W, pady = 10)
        Label(self, text = 'filename: ').grid(row = 1, stick = W, pady = 10)
        Entry(self, textvariable = self.fileName).grid(row = 1, column = 1 , stick = E)
        Label(self, text = 'sheetname').grid(row = 2, stick = W, pady = 10)
        Entry(self, textvariable = self.sheetName).grid(row = 2, column = 1 , stick = E)
        Button(self, text = 'submit').grid(row = 4, column = 1, stick = E , pady = 10)

class InputFrame(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.root = master
        self.FileName = StringVar()
        self.SheetName = StringVar()
        self.DatasetName = StringVar()
        self.MappingName = StringVar()
        self.InsertMapping = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='File Name: ').grid(row=1, stick=W, pady=10)

        fileEntry = Entry(self, textvariable=self.FileName,width=40)
        fileEntry.grid(row=1, column=1, stick=E)
        Button(self, text='Input', width = 10,command=lambda:self.insert_file(fileEntry,"excel file",".xlsx")).grid(row=2,column=1, stick=E, pady=10)

        Label(self, text='Sheet Name: ').grid(row=3, stick=W, pady=10)
        sheetEntry = Entry(self, textvariable=self.SheetName, width=40)
        sheetEntry.grid(row=3, column=1, stick=E)

        Label(self, text='Dataset Name: ').grid(row=4, stick=W, pady=10)
        nameEntry = Entry(self, textvariable=self.DatasetName, width=40)
        nameEntry.grid(row=4, column=1, stick=E)

        Label(self, text='Index Mapping Name: ').grid(row=5, stick=W, pady=10)
        mappingEntry = Entry(self, textvariable=self.MappingName,width=40)
        mappingEntry.grid(row=5, column=1, stick=E)
        Button(self, text='Input', width=10, command=lambda: self.insert_file(mappingEntry,"text file",".txt")).grid(row=6, column=1,stick=E,pady=10)

        Label(self, text='Insert Mapping Name: ').grid(row=7, stick=W, pady=10)
        insertMappingEntry = Entry(self, textvariable=self.InsertMapping,width = 40 )
        insertMappingEntry.grid(row=7, column=1, stick=E)
        Button(self, text='Input', width=10, command=lambda: self.insert_file(insertMappingEntry,"text file",".txt")).grid(row=8, column=1, stick=E, pady=10)
        Button(self, text='Upload', command=lambda: self.upload()).grid(row=9, column=1, stick=E, pady=10)


    def insert_file(self,entry,filetype,fileformat):
        Frame.filename = filedialog.askopenfilename(initialdir="resources", title="Select file", filetypes=((filetype, fileformat), ("all files", "*.*")))
        entry.insert(0, Frame.filename)

    def upload(self):
        message = ""
        if(self.FileName.get() == ""):
            message += "File name cannot be empty!\n"
        if(self.SheetName.get() == ""):
            message += "Sheet name cannot be empty!\n"
        if(self.DatasetName.get() == "" or not self.DatasetName.get().islower()):
            message += "Dataset name cannot be empty and must be lower case!\n"
        if(self.MappingName.get() == ""):
            message += "Mapping file name cannot be empty!\n"
        if(self.InsertMapping.get() == ""):
            message += "Insert mapping file name cannot be empty"

        if(message == ""):
            upload = eyeTracker_Subject(self.FileName.get(), self.SheetName.get(), self.DatasetName.get(),self.MappingName.get(), self.InsertMapping.get())
            subject = eyeTracker_Subject_Analysis(self.DatasetName.get())
            showinfo(title='Success', message='Upload Successful')
            self.pack_forget()
            joint_attention_analysis_page(subject,self.root)
        else:
            showinfo(title='bad', message = message)

        #print(self.FileName.get(), self.SheetName.get(), self.MappingName.get(), self.InsertMapping.get()) TETSimpleGaze_Order1-999-1
        #showinfo(title='Wrong', message=message)
class ExistedDataFrame(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.root = master
        self.DataSet = StringVar()
        self.elasticsearch_builder = Elasticsearch_client()
        self.client = self.elasticsearch_builder.get_client()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='Dataset Name: ').grid(row=1, stick=W, pady=10)
        fileEntry = Entry(self, textvariable=self.DataSet, width=40)
        fileEntry.grid(row=1, column=1, stick=E)
        Button(self, text='Input', width=10 , command = lambda:self.selectDataset()).grid(row=2, column=1, stick=E,pady=10)

        Label(self, text='Existed Dataset: ').grid(row=3, stick=W, pady=10)
        row_count = 4
        for index in self.client.indices.get('*'):
            if index[0] != '.':
                Label(self, text=index).grid(row=row_count, stick=W, pady=10)
                row_count+=1

    def selectDataset(self):
        subject = eyeTracker_Subject_Analysis(self.DataSet.get())
        #joint_attention_analysis_page(subject)
        self.pack_forget()
        print("self.root is ", self.root)
        joint_attention_analysis_page(subject, self.root)
class CountFrame(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()
    def createPage(self):
        Label(self, text = '统计页面').pack()

class AboutFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.root = master
        self.createPage()


    def createPage(self):
        Label(self, text = '关于界面').pack()
