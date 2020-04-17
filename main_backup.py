from eyeTracker_Subject import eyeTracker_Subject


def insert_sheet_name(window,textfield):
    sheet_name = textfield.get('1.0','end-1c')
    print(sheet_name)
    test = eyeTracker_Subject(window.filename, sheet_name)

def insert_file(window,input_text, following_label, following_text, following_button):

    canvas = tk.Canvas(window, height=25, width=500)
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("excel files", "*.xlsx"), ("all files", "*.*")))
    print(window.filename)
    input_text.config(state="normal")
    input_text.insert('insert', window.filename)
    input_text.config(state="disabled")
    if len(window.filename) !=0:
        canvas.pack()
        following_label.pack()
        following_text.pack()
        canvas.pack()
        following_button.pack()

    #print("hello from insert file")

###
import tkinter as tk
from tkinter import filedialog


def main():
    window = tk.Tk()
    first_canvas = tk.Canvas(window, height=50, width=500)
    second_canvas = tk.Canvas(window, height=25, width=500)

    window.title('Eye Tracker Toolbox')

    text = tk.Text(window, height=2, width=60)

    After_insert_text = tk.Text(window, height=2, width=40)
    After_insert_label = tk.Label(window, text='Insert the Sheet Name', font=('Arial', 12))
    After_insert_button = tk.Button(window, text='insert sheet name', width=15, height=2, command=lambda :insert_sheet_name(window,After_insert_text))


    window.geometry('600x400')

    tk.Label(window, text='EyeTracker Toolbox', font=('Arial', 16)).pack()
    first_canvas.pack()
    text.config(state="disabled")
    text.pack()
    second_canvas.pack()
    b1 = tk.Button(window, text='insert file', width=10, height=2,command=lambda:insert_file(window, text, After_insert_label, After_insert_text, After_insert_button))
    b1.pack()
    window.mainloop()

if __name__ =="__main__":
    main() # call the main function in order to output the result


























###
#test = eyeTracker_Subject('../resources/data.xlsx','TETSimpleGaze_Order1-999-1')