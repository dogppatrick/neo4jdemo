from adaptor.databases import Neo4j

n4j = Neo4j()
geo = n4j.g

query = '''CALL gds.graph.create(
    'Membersimilary2',
    ['Post', 'Member'],
    {
        Read: {
            type: 'Read'
        }
    }
);
'''
geo.run(query)