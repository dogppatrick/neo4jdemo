import logging.config
from pymongo import MongoClient
from py2neo import Graph, Node, Relationship
from py2neo.matching import NodeMatcher as Nm

log = logging.getLogger(__name__)

class Neo4j:
    def __init__(self):
        uri = "bolt://localhost:7687"
        user = "neo4j"
        password = "!QAZ2wsx"
        self.g = Graph(uri=uri, user=user, password=password)
        self.nodes = Nm(self.g)

    def clear_data(self):
        self.g.delete_all()

    def add_node(self, label_name, **properties):
        """
        Create node object and insert to neo4j db
        """
        new_node = Node(f'{label_name}',**properties)
        self.g.create(new_node)
        return new_node

    def add_relationship(self, node1, node2, rel_type, **properties):
        rel = Relationship(node1, rel_type, node2, **properties)
        self.g.create(rel)

    def get_nodes(self,key='uid',match_type='case'):
        """
        return dict of nodes {key:Node()}
        """
        exist_node = {dict(n).get(key):n for n in self.nodes.match(type=match_type).all()}
        return exist_node
    


class MongoDb(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.data_test
        self.col_test_read = self.db.test_member_read
    
    def get_read_data(self):
        """
        test_sample = {
            "post_id": "1234",
            "sfct_cookie_id": "track_0987",
            "created_ts": "2022-04-19 18:42:27",
            "member_id": "5566"
        }"""
        return [d for d in self.col_test_read.find({})]