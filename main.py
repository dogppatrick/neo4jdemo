from adaptor.databases import Neo4j

n4j = Neo4j()
geo = n4j.g

# query = '''CALL gds.graph.create(
#     'Membersimilary2',
#     ['Post', 'Member'],
#     {
#         Read: {
#             type: 'Read'
#         }
#     }
# );
# '''
# geo.run(query)

query = '''
CALL gds.nodeSimilarity.stream('Membersimilary2')
YIELD node1, node2, similarity
Where similarity > 0.5
RETURN gds.util.asNode(node1).id AS Member1, gds.util.asNode(node2).id AS Member2, similarity
ORDER BY similarity DESCENDING, Member1, Member2
'''
result = geo.run(query).to_data_frame()
result.to_csv('Membersimilary2.csv',index=False)