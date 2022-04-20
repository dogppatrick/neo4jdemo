from adaptor.databases import Neo4j, MongoDb
from adaptor.utils import ft_timer
import pandas as pd
import numpy as np

n4j = Neo4j()
n4j.clear_data()
mongodb = MongoDb()
data = mongodb.get_read_data()

@ft_timer
def insert_read_relate_nodes(data):
    member_node = dict()
    post_node = set()
    # cookie_node = set()

    r_member_post = set()
    # r_member_cookie = set()
    insert_node_count = 0
    insert_relation_count = 0

    for doc in data:
        member_id = doc.get('member_id')
        post_id = doc.get('post_id')
        cookie_id = doc.get('sfct_cookie_id')
        r_member_post.add((member_id,post_id,))
        # r_member_cookie.add((member_id,cookie_id,))
        member_node[member_id] = [member_id,cookie_id]
        post_node.add(post_id)
        # cookie_node.add(cookie_id)

    exist_node = dict()

    for member_id in member_node:
        if member_id in exist_node:
            continue
        member_info = {'id':member_id, 'cookie':member_node.get(member_id)[1]}
        node = n4j.add_node('Member', **member_info)
        exist_node[member_id] = node
        insert_node_count +=1

    for post_id in post_node:
        if post_id in exist_node:
            continue
        post_info = {'id':post_id}
        node = n4j.add_node('Post', **post_info)
        exist_node[post_id] = node
        insert_node_count +=1

    # for cookie_id in cookie_node:
    #     if cookie_id in exist_node:
    #         continue
    #     cookie_info = {'id':cookie_id}
    #     node = n4j.add_node('Cookie', **cookie_info)
    #     exist_node[cookie_id] = node
    #     insert_node_count +=1

    for r_pair in r_member_post:
        member_id, post_id = r_pair
        node_member = exist_node.get(member_id)
        node_post = exist_node.get(post_id)
        n4j.add_relationship(node_member,node_post,'Read')
        n4j.add_relationship(node_post,node_member,'Opened')
        insert_relation_count+=1

    # for r_pair in r_member_cookie:
    #     member_id, cookie_id = r_pair
    #     node_member = exist_node.get(member_id)
    #     node_cookie = exist_node.get(cookie_id)
    #     n4j.add_relationship(node_member,node_cookie,'Use')
    #     insert_relation_count+=1
    return {'node_add':insert_node_count,'relation_add':insert_relation_count}

result = insert_read_relate_nodes(data)
print(result)
# map_name = {d[1]:d[0] for d in np.array(df)}
