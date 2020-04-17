import pandas as pd

class record:
    def __init__(self,header:pd.core.series.Series,recordId:int, column_name:list):
        #print("record now")
        self.dict  = {}
        for index in column_name:
            #print(str(header[index]) == 'nan')
            if str(header[index]) == 'nan':
                self.dict[index]= ""
            else:
                self.dict[index] = header[index]
        #print(self.dict)
    def getdict(self):
        return self.dict