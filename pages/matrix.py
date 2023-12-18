import streamlit as st
import openai
import py2neo
import streamlit_neo4j


from py2neo import Graph
from streamlit_neo4j import neo4j_component

# ------- Constants and Configuration --------

st.set_page_config(page_title="Tomast", page_icon="🪖", layout='wide')

#st.session_state['model'] = "gpt-3.5-turbo" 
st.session_state['model'] = "gpt-4"
st.session_state['language'] = "German"


# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# Create an instance of the OpenAI API client
client = openai.OpenAI()


# ------- OpenAI Call -------

def call_openai_api(prompt, max_tokens=3000, temperature=0.4):
    model = st.session_state['model']
    language = st.session_state['language']
    system = f"""You always generate in {language}."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except (KeyError, Exception) as e:
        return f"An error occurred: {e}"
    
  # ------- Scenario Summary  -------#

def matrix():
    prompt = f"""This is the current scenario:  {st.session_state['scenario']}
Create a graph database of all the relationships within this graph using nodes and connections.

Output the graph database in CYPHER.

    """
    matrix = call_openai_api(prompt, max_tokens=2000)
    st.session_state['scenario'] = matrix_cypher
    st.success("Summary generated...")
    return matrix_cypher



# ------- General UI -------
###Create a toggle for advanced settings to show the cypher box or not
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