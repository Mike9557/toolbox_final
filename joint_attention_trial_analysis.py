from tkinter import *
from view import *
from eyeTracker_Subject_Analysis import *

class joint_attention_trial_analysis(object):
    def __init__(self, subject:eyeTracker_Subject_Analysis,trial_id, master=None, ):
        self.subject = subject
        self.root = master
        self.trial_id = trial_id
        self.root.geometry('%dx%d' % (300,600))
        self.createPage()
    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        record_count = self.subject.getExistRecordCount('CRESP', str(self.trial_id))
        correct_count_per_trial, wrong_count_per_trial = self.subject.getCountPerTrial('CRESP', 'TrialId', '1', str(self.trial_id),record_count)

        Label(self.page, text="TrialID:  "+ self.trial_id, font=("Helvetica", 9, "bold")).grid(row=1, stick=W,pady=10)
        Label(self.page, text="Record Count： " + str(record_count), font=("Helvetica", 9, "bold")).grid(row=2,stick=W,pady=10)
        Label(self.page, text="Right Count: " + str(correct_count_per_trial), font=("Helvetica", 9, "bold")).grid(row=3,stick=W,pady=10)
        Label(self.page, text="Wrong Count: " + str(wrong_count_per_trial), font=("Helvetica", 9, "bold")).grid(row=4, stick=W,pady=10)
        min_timestamp, max_timestamp = self.subject.getMaxMinTimestampPerTrial(self.trial_id)
        if (not (min_timestamp is None) and not (max_timestamp is None)):

            Label(self.page, text="Trial Starting Timestamp: " + str(int(min_timestamp)), font=("Helvetica", 9, "bold")).grid(row=5,stick=W,pady=10)
            Label(self.page, text="Trial End Timestamp: " + str(int(max_timestamp)), font=("Helvetica", 9, "bold")).grid(row=6, stick=W, pady=10)
            Label(self.page, text="Trial Total Time: " + str(int(max_timestamp) - int(min_timestamp)), font=("Helvetica", 9, "bold")).grid(row=7,stick=W,pady=10)


            process_time = int(max_timestamp) - int(min_timestamp)
            LeftAOICount,LeftAOITime = self.subject.getLeftAOIRecordInformation(self.trial_id,record_count,process_time)
            RightAOICount, RightAOITime = self.subject.getRightAOIRecordInformation(self.trial_id, record_count, process_time)
            MouthAOICount, MouthAOITime = self.subject.getMouthAOIRecordInformation(self.trial_id, record_count, process_time)

            Label(self.page, text="Left AOI Count : " + str(LeftAOICount),font=("Helvetica", 9, "bold")).grid(row=8, stick=W, pady=10)
            Label(self.page, text="Left AOI Time : " + str(LeftAOITime), font=("Helvetica", 9, "bold")).grid(row=9,stick=W,pady=10)
            Label(self.page, text="Right AOI Count : " + str(RightAOICount), font=("Helvetica", 9, "bold")).grid(row=10,stick=W,pady=10)
            Label(self.page, text="Right AOI Time : " + str(RightAOITime), font=("Helvetica", 9, "bold")).grid(row=11, stick=W,pady=10)
            Label(self.page, text="Mouth AOI Count : " + str(MouthAOICount), font=("Helvetica", 9, "bold")).grid(row=12, stick=W,pady=10)
            Label(self.page, text="Mouth AOI Time : " + str(MouthAOITime),font=("Helvetica", 9, "bold") ).grid(row=13, stick=W,pady=10)



#joint_attention_2020-02-21