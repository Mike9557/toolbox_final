import pandas as pd
from elasticsearch_client import Elasticsearch_client
import datetime
import json
max_aggregation = 'resources/elasticsearch_query/max_aggregation.txt'
exist_field_record_per_trial_count = 'resources/elasticsearch_query/exist_field_record_per_trial_count.txt'
exist_field_for_all_trial = 'resources/elasticsearch_query/exist_field_for_all_trial.txt'
match_query = 'resources/elasticsearch_query/match_query.txt'
multiple_match_query = 'resources/elasticsearch_query/multiple_match_query.txt'
max_min_timestamp_cresp_per_trial = 'resources/elasticsearch_query/max_min_timestamp_cresp_per_trial.txt'
class eyeTracker_Subject_Analysis:
    def __init__(self, index_name):
        self.index_name = index_name
        try:
            with open(max_aggregation, 'r') as file:
                self.max_aggregation = file.read().replace('\n', '')
        except FileNotFoundError:
            print("max_aggregation File does not found")

        try:
            with open(exist_field_record_per_trial_count, 'r') as file:
                self.exist_field_record_per_trial_count = file.read().replace('\n', '')
        except FileNotFoundError:
            print("exist_field_record_per_trial_count File does not found")

        try:
            with open(exist_field_for_all_trial, 'r') as file:
                self.exist_field_for_all_trial = file.read().replace('\n', '')
        except FileNotFoundError:
            print("exist_field_for_all_trial File does not found")

        try:
            with open(match_query, 'r') as file:
                self.match_query = file.read().replace('\n', '')
        except FileNotFoundError:
            print("match_query File does not found")

        try:
            with open(multiple_match_query, 'r') as file:
                    self.multiple_match_query = file.read().replace('\n', '')
        except FileNotFoundError:
                print("multiple_match_query File does not found")

        try:
            with open(max_min_timestamp_cresp_per_trial, 'r') as file:
                self.max_min_timestamp_cresp_per_trial = file.read().replace('\n', '')
        except FileNotFoundError:
            print("max_min_timestamp_cresp_per_trial File does not found")


        self.elasticsearch_builder = Elasticsearch_client()
        self.client = self.elasticsearch_builder.get_client()

    def getMax(self,field_name):
        #should be an numberic field
        aggregation =  self.max_aggregation.replace('$field',field_name)

        res = self.client.search(index = self.index_name, body=aggregation)
        return (res['aggregations']['max']['value'])

    def getAllRecords(self,field_name):
        aggregation = self.exist_field_for_all_trial.replace('$field', field_name)
        res = self.client.count(index = self.index_name,body=aggregation)
        return res['count']

    def getRightAndWrongRespCount(self,fieldname, right_response,totalCount):
        aggregation = self.match_query.replace('$Field',fieldname).replace('$MatchValue',right_response)
        res = self.client.count(index=self.index_name, body=aggregation)
        wrong_count = totalCount - res['count']
        return res['count'],wrong_count

    def getExistRecordCount(self,field_name,trial_id):
        aggregation = self.exist_field_record_per_trial_count.replace('$Field', field_name).replace('$TrialId',trial_id)
        #print(aggregation)
        res = self.client.count(index=self.index_name, body=aggregation)
        return res['count']

    def getCountPerTrial(self,Field_1,Field_2,Value_1,Value_2,total_count):
        aggregation = self.multiple_match_query.replace('$Field_1',Field_1).replace('$Field_2',Field_2).replace('$Value_1',Value_1).replace('$Value_2',Value_2)

        res = self.client.count(index=self.index_name, body=aggregation)

        return res['count'],total_count - res['count']

    def getMaxMinTimestampPerTrial(self,trial_id):
        aggregation = self.max_min_timestamp_cresp_per_trial.replace('$Trial_ID',trial_id)
        res = self.client.search(index=self.index_name, body=aggregation)

        return res['aggregations']['min']['value'],res['aggregations']['max']['value']

    def getLeftAOIRecordInformation(self,trial_id, total_record_count, total_time):
        aggregation = self.multiple_match_query.replace('$Field_1', 'LeftAOI').replace('$Field_2', 'TrialId').replace('$Value_1', "1").replace('$Value_2', trial_id)
        res = self.client.count(index=self.index_name, body=aggregation)
        count = res['count']
        LeftAOITime = float(count/total_record_count) * total_time
        return count,round(LeftAOITime, 2)
    def getRightAOIRecordInformation(self,trial_id, total_record_count, total_time):
        aggregation = self.multiple_match_query.replace('$Field_1', 'RightAOI').replace('$Field_2', 'TrialId').replace('$Value_1', "1").replace('$Value_2', trial_id)
        res = self.client.count(index=self.index_name, body=aggregation)
        count = res['count']
        RightAOITime = float(count / total_record_count) * total_time
        return count, round(RightAOITime, 2)

    def getMouthAOIRecordInformation(self, trial_id, total_record_count, total_time):
        aggregation = self.multiple_match_query.replace('$Field_1', 'MouthAOI').replace('$Field_2', 'TrialId').replace('$Value_1', "1").replace('$Value_2', trial_id)
        res = self.client.count(index=self.index_name, body=aggregation)
        count = res['count']
        MouthAOITime = float(count / total_record_count) * total_time
        return count, round(MouthAOITime, 2)