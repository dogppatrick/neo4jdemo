from adaptor.databases import Neo4j, MongoDb
import pandas as pd
import numpy as np

n = Neo4j()
# n.clear_data()
df = pd.read_csv("./case_map_result.csv",encoding="utf-8")
map_name = {d[1]:d[0] for d in np.array(df)}

with open("./case_pair.txt",mode='r') as f:
    raw_pair = f.read()

uid_pair = [d.split(",") for d in raw_pair.split("\n")]
exist_node = n.get_nodes()
# for label in exist_node:
    # print(label,exist_node[label])
    
# Create node 
raw_case = set()
for case_uid, sub_id, meet_count in uid_pair:
    raw_case.add(case_uid)
    raw_case.add(sub_id)

rel = dict()

for case_uid, sub_id, meet_count in uid_pair:
    if int(case_uid[-4:]) < int(sub_id[-4:]):
        case_uid, sub_id = sub_id, case_uid 
    key = tuple([case_uid, sub_id])
    rel[key] = rel.get(key,0) + int(meet_count)

# reduce case_uid by hr_crimial and merge
linked_case = set()
min_meets = 10

for pair, count in rel.items():
    if count < min_meets:
        continue
    else:
        linked_case.add(pair[0])
        linked_case.add(pair[1])

case_add = 0
for case in raw_case:
    if case not in exist_node and case in linked_case:
        if not map_name.get(case):
            continue
        dist_name , case_name = map_name.get(case).split(" ")
        case_info = {'name':f'{case_name}', 'uid':case, 'type':'case'}
        new_node = n.add_node(dist_name,**case_info)
        exist_node[case] = new_node
        case_add +=1
print(f'case:{case_add} add')
rel_add_count = 0
for pair, count in rel.items():
    if count < min_meets or pair[0] not in exist_node or pair[1] not in exist_node:
        continue
    node1 = exist_node[pair[0]]
    node2 = exist_node[pair[1]]
    rel_type = 'meet'
    attr = {'meet_count':count}
    # attr = {'rec_date':case_near_event['record_datetime']
            # ,'meet_distance': case_near_event.get('distance',0)
            # }
    # attr['Point'] = {'latitude':f"{case_near_event['coordinates']['coordinates'][0]:.4f}"
                #    , 'longitude':f"{case_near_event['coordinates']['coordinates'][1]:.4f}"}
    n.add_relationship(node1,node2,rel_type, **attr)
    rel_add_count +=1

print(f'relatation update {rel_add_count}')