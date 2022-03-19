import logging.config
from pymongo import MongoClient
from py2neo import Graph, Node, Relationship
from py2neo.matching import NodeMatcher as Nm
from config import MongodbConfig



log = logging.getLogger(__name__)

class Neo4j:
    def __init__(self):
        uri = "bolt://10.100.0.168:7687"
        user = "neo4j"
        password = "!QAZ2wsx"
        self.g = Graph(uri=uri, user=user, password=password)
        self.nodes = Nm(self.g)

    def clear_data(self):
        self.g.delete_all()

    def add_node(self, label_name, **properties):
        """
        Create a new node and add into DB
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

class MongoDb:
    def __init__(self):
        try:
            self.client = MongoClient(host=MongodbConfig.URL,
                                    username=MongodbConfig.USERNAME,
                                    password=MongodbConfig.PASSWORD, 
                                    authSource=MongodbConfig.AUTH_DB)
            # self.client = MongoClient()
            self.db = self.client.moj
            self.col_case_near_log = self.db.case_near_log
        except Exception as e:
            print(f'init error!!')
            log.critical(f'mongodb_create fail {e}')
    
    def reset_test_case_near_log(self,data):
        self.col_case_near_log.delete_many({'version':"test_neo4j"})
        self.col_case_near_log.insert_many(data)
    
    def get_case_near_log(self):
        return [d for d in self.col_case_near_log.find({})]
    