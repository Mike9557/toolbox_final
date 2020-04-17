from elasticsearch import Elasticsearch
from record import record
es_url = 'http://localhost:9200/'
insert_mapping_default = 'resources/insert_mapping.txt'
class Elasticsearch_client:
    def __init__(self,insert_mapping = insert_mapping_default, url = es_url, ):
        self.client = Elasticsearch([url])
        try:
            with open(insert_mapping, 'r') as file:
                self.insert_mapping = file.read().replace('\n', '')
                #print("insert mapping", self.insert_mapping)
        except FileNotFoundError:
            print("Insert Mapping File does not found")

    def get_client(self):
        return self.client

    def upload_record(self,es_index, input_dict,column_name):
        es_body = self.insert_mapping
        for index in range(len(column_name)):
            es_body = es_body.replace("$" + str(index) + " ", str(input_dict[column_name[index]]));
        res = self.client.index(index = es_index, doc_type="_doc", id = str(input_dict['ID']), body = es_body )
        #print(es_index)
        print(input_dict['ID'], " is ",res['result'])
