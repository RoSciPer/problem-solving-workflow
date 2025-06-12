import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph():
    G = nx.DiGraph()
    G.add_edges_from([
        ("Identify\nComplex Problem", "Analyze\nand Research"),
        ("Analyze\nand Research", "Develop\nSolution"),
        ("Develop\nSolution", "Automate\nRepetitive Tasks"),
        ("Automate\nRepetitive Tasks", "Deploy\nand Monitor")
    ])
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, with_labels=True, node_color='skyblue',
            node_size=3000, font_size=10, arrows=True, arrowsize=20)
    st.pyplot(plt)

st.set_page_config(page_title="Problem Solving Diagram", layout="centered")
st.title("🧠 Problem-Solving Workflow")
st.markdown("Visual representation of how I approach complex problems, from analysis to automation.")
draw_graph()
