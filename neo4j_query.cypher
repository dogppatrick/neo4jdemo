// find m0's reads' also reads
match (m0:Member)-[r0:Read]-(p1:Post)-[r1:Read]-(m1:Member)-[r2:Read]-(p2:Post)
where p1 <> p2
and m0.id = '134626'
return m0,p1,m1,p2
Limit 50

CALL gds.graph.create(
    'Membersimilary',
    ['Post', 'Member'],
    {
        Read: {
            type: 'Read'
        }
    }
);
CALL gds.nodeSimilarity.stream('Membersimilary')
YIELD node1, node2, similarity
Where similarity > 0.5
RETURN gds.util.asNode(node1).id AS Member1, gds.util.asNode(node2).id AS Member2, similarity
ORDER BY similarity DESCENDING, Member1, Member2

// get member post similary
CALL gds.graph.create(
    'Postsimilary',
    ['Member', 'Post'],
    {
        Read: {
            type: 'Opened'
        }
    }
);
CALL gds.nodeSimilarity.stream('Postsimilary')
YIELD node1, node2, similarity
Where similarity > 0.5
RETURN gds.util.asNode(node1).id AS Post1, gds.util.asNode(node2).id AS Post2, similarity
ORDER BY similarity DESCENDING, Post1, Post2