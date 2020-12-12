import streamlit as st
import plotly.graph_objs as go

st.title("Engagement rates")
f = st.text_input('Enter username of the first profile to compare')
s = st.text_input('Enter username of the second profile to compare')
st.header("Graphs of engagement of the entered profiles")

first = go.Scatter(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=[48, 81, 158, 4619, 3632, 7182, 897, 516, 75, 312], name=f)
trace1 = go.Scatter(x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], y=[3298, 93, 15, 1783, 5690, 2369, 520, 431, 46, 173], name=s)
data = [first, trace1]
st.write(data)