from adaptor.databases import Neo4j, MongoDb
from py2neo import Node, Relationship
from pprint import pprint
from datetime import datetime
import pandas as pd
import numpy as np

# n = Neo4j()
# m = MongoDb()
# df = pd.read_csv("./case_name_map.csv",encoding="utf-8")
# map_name = {d[1]:d[0] for d in np.array(df)}
# n.clear_data()
# raw_log = m.get_case_near_log()
# nodes = n.nodes
# exist_node = {str(n.labels)[1:]:n for n in nodes.match(type='case').all()}
# raw_case = set()
# for data in raw_log:
#     raw_case.add(data.get('case_uid'))
#     raw_case.add(data.get('sub_uid'))

# for case in raw_case:
#     if case not in exist_node:
#         case_name = map_name.get(case,'')
#         exist_node[case] = Node(f'{case_name}',name=f'{case}', type='case')
#         n.add_nodes(exist_node[case])
#         print(f'new node add, label:{case}')

# for case_near_event in raw_log:
#     # print(case_near_event)
#     node1 = exist_node[case_near_event.get('case_uid')]
#     node2 = exist_node[case_near_event.get('sub_uid')]
#     rel_type = 'meet'
#     attr = {'rec_date':case_near_event['record_datetime']
#             ,'meet_distance': case_near_event.get('distance',0)
#             }
#     # attr['Point'] = {'latitude':f"{case_near_event['coordinates']['coordinates'][0]:.4f}"
#                 #    , 'longitude':f"{case_near_event['coordinates']['coordinates'][1]:.4f}"}
#     n.add_relationship(node1,node2,rel_type, **attr)
