from neo4j import GraphDatabase

def execute_cypher_query(query):
    uri = "bolt://localhost:7687"
    username = 'neo4j'
    password = 'pass@123'
    
    driver = GraphDatabase.driver(uri, auth=(username, password))
    
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]

def query_players():
    # Cypher query to retrieve all players
    cypher_query = """
    MATCH (player:PLAYER)
    RETURN player
    """
    
    result = execute_cypher_query(cypher_query)
    print("Players:")
    for record in result:
        print(record)

def query_teams():
    # Cypher query to retrieve all teams
    cypher_query = """
    MATCH (team:TEAM)
    RETURN team
    """
    
    result = execute_cypher_query(cypher_query)
    print("Teams:")
    for record in result:
        print(record)

def query_coaches():
    # Cypher query to retrieve all coaches
    cypher_query = """
    MATCH (coach:COACH)
    RETURN coach
    """
    
    result = execute_cypher_query(cypher_query)
    print("Coaches:")
    for record in result:
        print(record)

def query_teammates(player_name):
    # Cypher query to retrieve teammates of a specific player
    cypher_query = f"""
    MATCH (:PLAYER{{name: "{player_name}"}})-[:TEAMMATES]->(teammate)
    RETURN teammate
    """
    
    result = execute_cypher_query(cypher_query)
    print(f"Teammates of {player_name}:")
    for record in result:
        print(record)

def query_players_of_team(team_name):
    # Cypher query to retrieve players of a specific team
    cypher_query = f"""
    MATCH (player:PLAYER)-[:PLAYS_FOR]->(:TEAM{{name: "{team_name}"}})
    RETURN player
    """
    
    result = execute_cypher_query(cypher_query)
    print(f"Players of {team_name}:")
    for record in result:
        print(record)

# Example usage:
if __name__ == "__main__":
    query_players()
    query_teams()
    query_coaches()
    query_teammates("LeBron James")
    query_players_of_team("LA Lakers")
