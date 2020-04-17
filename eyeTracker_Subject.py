import pandas as pd
from elasticsearch_client import Elasticsearch_client
import datetime
import json
from record import record
class eyeTracker_Subject:
    def __init__(self, filename:str, sheet_name:str,index_name:str,mapping_filename, insert_mapping_filename):

        #self.mapping = 1234
        try:
            with open(mapping_filename, 'r') as file:
                self.mapping=file.read().replace('\n', '')
                print("the mapping file", self.mapping)
        except FileNotFoundError:
            print("File does not found")

        #self.__validate(trial_date)
        self.__inputfile = filename
        self.insert_mapping = insert_mapping_filename
        self.index_name = index_name
        self.__sheet_name = sheet_name
        self.__readfile()



    def __readfile(self):
        dfs = pd.read_excel(self.__inputfile, self.__sheet_name)


        column_name = []

        for column in dfs.columns:
            column_name.append(column)

        print(column_name)
        elasticsearch_buildup = Elasticsearch_client(self.insert_mapping)
        client = elasticsearch_buildup.get_client()

        try:
            client.indices.create(index = self.index_name, body = self.mapping)
            print(self.index_name, " index is created ")
        except:
            print("Error：index ", self.index_name , "is already created ")

        for index, row in dfs.iterrows():
            temp_record = record(row,index, column_name)
            #print(temp_record)
            elasticsearch_buildup.upload_record(self.index_name,temp_record.getdict(),column_name)

    def __validate(self,date_text:str):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def main():
    test = eyeTracker_Subject("resources/data.xlsx","TETSimpleGaze_Order1-999-1","2020-02-03")
if __name__ == "__main__":

    main()  # call the main function in order to output the result
