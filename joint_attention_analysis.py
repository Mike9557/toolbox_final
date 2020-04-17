from tkinter import *
from view import *
from eyeTracker_Subject_Analysis import *
from joint_attention_trial_analysis import*
import xlsxwriter
import datetime
class joint_attention_analysis_page(object):
    def __init__(self, subject:eyeTracker_Subject_Analysis,master=None, ):
        self.subject = subject
        self.root = master
        self.root.geometry('%dx%d' % (1200, 900))
        self.trial_inspect_id = StringVar()
        self.createPage()
    def createPage(self):
        self.page = Frame(self.root)

        self.page.pack()

        Total_Trial = int(self.subject.getMax('TrialId'))
        total_record_count = self.subject.getAllRecords('CRESP')
        right_count, wrong_count = self.subject.getRightAndWrongRespCount('CRESP','1',total_record_count)
        Label(self.page).grid(row=0, stick = W)

        Label(self.page, text='Total Trial: ' + str(Total_Trial) ,font=("Helvetica", 9)).grid(row=1,column = 1,stick=W,pady=10,padx=10)
        Label(self.page, text= " Total Record Count： " + str(total_record_count),font=("Helvetica", 9)).grid(row=1,column =2,stick=W,pady=10,padx=10)
        Label(self.page, text= " Right Count: " + str(right_count),font=("Helvetica", 9)).grid(row=1,column = 3,stick=W,pady=10,padx=10)
        Label(self.page, text= " Wrong Count: " + str(wrong_count),font=("Helvetica", 9)).grid(row=1,column = 4,stick=W,pady=10,padx=10)

        Entry(self.page, textvariable=self.trial_inspect_id, width=10).grid(row=1,column = 5,stick=W,pady=10,padx=10)


        Button(self.page, text='inspect', command=lambda :self.inspect_detail()).grid(row=1, column=5)
        row_count = 5
        row = 2
        column = 1

        #output_file
        currentDT = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        workbook = xlsxwriter.Workbook('./results/joint_attention_' + currentDT + ".xlsx")
        worksheet = workbook.add_worksheet("Results")
        worksheet_row = 0
        worksheet_column = 0
        print("workbook creation completed")
        Title = ["TrialID", "Record Count", "Right Count","Wrong Count","Trial Starting Timestamp","Trial End Timestamp","Trial Total Time","Left AOI Count","Left AOI Time","Right AOI Count","Right AOI Time", "Mouth AOI Count","Mouth AOI Time"]
        for i in range(0, len(Title)):
            worksheet.write(worksheet_row, worksheet_column,Title[i])
            worksheet_column += 1
        worksheet_row += 1
        for i in range(1,Total_Trial+1):

            record_count = self.subject.getExistRecordCount('CRESP', str(i))
            correct_count_per_trial,wrong_count_per_trial = self.subject.getCountPerTrial('CRESP','TrialId','1',str(i),record_count)
            message = 'TrialID: ' + str(i) + " cresp record count: " + str(record_count) + '\n' + "Correct Count: " + str(correct_count_per_trial) + '\n' + ' Wrong Count: ' + str(wrong_count_per_trial)

            label = Label(self.page, text=message,font=("Helvetica", 9),relief="solid",fg="black")
            label.grid(row=row,column = column,stick=W,pady=10,padx=10)
            if (record_count != 0):
                worksheet.write(worksheet_row, 0, str(i))
                worksheet.write(worksheet_row, 1, record_count)
                worksheet.write(worksheet_row, 2, correct_count_per_trial)
                worksheet.write(worksheet_row, 3, wrong_count_per_trial)

                min_timestamp, max_timestamp = self.subject.getMaxMinTimestampPerTrial(str(i))

                process_time = int(max_timestamp) - int(min_timestamp)
                LeftAOICount, LeftAOITime = self.subject.getLeftAOIRecordInformation(str(i), record_count, process_time)
                RightAOICount, RightAOITime = self.subject.getRightAOIRecordInformation(str(i), record_count, process_time)
                MouthAOICount, MouthAOITime = self.subject.getMouthAOIRecordInformation(str(i), record_count, process_time)

                worksheet.write(worksheet_row, 4, min_timestamp)
                worksheet.write(worksheet_row, 5, max_timestamp)
                worksheet.write(worksheet_row, 6, process_time)
                worksheet.write(worksheet_row, 7, LeftAOICount)
                worksheet.write(worksheet_row, 8, LeftAOITime)
                worksheet.write(worksheet_row, 9, RightAOICount)
                worksheet.write(worksheet_row, 10, RightAOITime)
                worksheet.write(worksheet_row, 11, MouthAOICount)
                worksheet.write(worksheet_row, 12, MouthAOITime)
                worksheet_row += 1


            column += 1
            if (i % row_count == 0):
                column = 1
                row += 2
        worksheet_row += 1
        worksheet.write(worksheet_row, 0, "Total Trial: ")
        worksheet.write(worksheet_row, 1, str(Total_Trial))
        worksheet.write(worksheet_row, 2, "Total Record Count: ")
        worksheet.write(worksheet_row, 3, str(total_record_count))
        worksheet.write(worksheet_row, 4, "Right Count: ")
        worksheet.write(worksheet_row, 5, str(right_count))
        worksheet.write(worksheet_row, 6, "Wrong Count: ")
        worksheet.write(worksheet_row, 7, str(wrong_count))
        workbook.close()
    def inspect_detail(self):
        trial_id = self.trial_inspect_id.get()
        root2 = Tk()
        root2.title('EyeTracker ToolBox')

        joint_attention_trial_analysis(self.subject,trial_id,root2)


















