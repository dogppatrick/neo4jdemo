from adaptor.databases import Neo4j, MongoDb
from py2neo import Node, Relationship
from pprint import pprint
from datetime import datetime
import pandas as pd
import numpy as np

# def format_data(d):
#     _, name, uid , pro_name = d
#     name = f"{pro_name} {name[0]}'X'{name[-1]}"
#     return [name, uid]

# df = pd.read_csv("./case_name_map.csv",encoding="utf-8")
# arr = np.array(df)
# df = pd.DataFrame([format_data(d) for d in arr], columns=['name', 'uid'])
# df.to_csv("./case_map_result.csv", encoding='utf-8', index=False)



n = Neo4j()
