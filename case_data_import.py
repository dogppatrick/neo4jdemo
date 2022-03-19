import json
from datetime import datetime
from adaptor.databases import MongoDb

def format_data(data):
    data.pop("_id","")
    data['version'] = 'test_neo4j'
    data['record_datetime'] = datetime.strptime(data['record_datetime']['$date'][:19], "%Y-%m-%dT%H:%M:%S")
    return data
mongodb = MongoDb()
with open('./test_case_near.json',mode='r',encoding='utf-8') as f:
    data = f.read()


data = json.loads(data)
data = [format_data(d) for d in data]
# [print(d) for d in data[:5]]
mongodb.reset_test_case_near_log(data)