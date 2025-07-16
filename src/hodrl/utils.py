from SPARQLWrapper import SPARQLWrapper, JSON

FUSEKI_ENDPOINT = "metadata-store:3030"
DATASET = "system"

def query_fuseki(query):
    # Set up query endpoint
    sparql = SPARQLWrapper(f"http://{FUSEKI_ENDPOINT}/{DATASET}/query")
    sparql.setReturnFormat(JSON)
    sparql.setCredentials("admin", "admin")

    # Set the query to be performed
    sparql.setQuery(query)

    # Perform query
    try:
        ret = sparql.queryAndConvert()
        bindings = ret.get("results").get("bindings")
    except Exception as e:
        print(e)

    # Return
    return bindings
