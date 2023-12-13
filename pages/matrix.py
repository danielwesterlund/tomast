import os
#import openai
#import py2neo
#import streamlit_neo4j
import streamlit as st

#from py2neo import Graph
#from streamlit_neo4j import neo4j_component

# ------- General UI -------

def homeui():
    st.title("This is The Relationship Matrix")
    
    # Connect to Neo4j Database
    #graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

    # Input box for CYPHER query
    query = st.text_input('Enter your CYPHER query here', 'MATCH (n) RETURN n')

    # If no query is entered, display the complete graph
    if query == '':
        query = 'MATCH (n) RETURN n'

    # Use the Streamlit Component to display the Neo4j Graph
    #neo4j_component(graph.run(query).data())

    # Input box for user prompt to change the matrix
    prompt = st.text_input('Enter your prompt to change the matrix')
    if st.button('Submit'):
        # Show the query as CYPHER and update the graph
        st.write('Your CYPHER query: ', prompt)
        #neo4j_component(graph.run(prompt).data())


        # Confirm changes and update the graph on the Neo4j server
        if st.button('Confirm'):
            #graph.run(prompt)
            st.success('Graph updated successfully!')

def main():
    homeui()

if __name__ == "__main__":
    main()