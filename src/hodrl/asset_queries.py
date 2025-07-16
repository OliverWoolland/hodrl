from hodrl import utils

def get_all_assets():
    query = """
PREFIX odrl: <http://www.w3.org/ns/odrl/2/>
    
SELECT DISTINCT ?asset WHERE {
    ?asset a odrl:Asset .
}
"""
    
    result = utils.query_fuseki(query)
    print(result)
    return result
