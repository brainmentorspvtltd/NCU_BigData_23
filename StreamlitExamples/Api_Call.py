import urllib.request as url
import json
import streamlit as st
name = st.selectbox("News Category",
                       ["Sports","Business","Entertainment","Science","Health","Technology"])
btn = st.button("Fetch News")
if btn:
    path = f"https://newsapi.org/v2/top-headlines?country=in&category={name}&apiKey=695e07af402f4b119f0703e9b19f4683"
    response = url.urlopen(path)

    data = json.load(response)
    articles = data['articles']

    for i in range(len(articles)):
        st.write(articles[i]["title"])
        st.write("*"*30)
    