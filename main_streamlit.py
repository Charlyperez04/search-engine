import os
import pandas as pd
import txtai
import streamlit as st
import kagglehub
import time
import subprocess

dataset_path = kagglehub.dataset_download("glushko/seth-godins-blogs-dataset")
csv_file = os.path.join(dataset_path, "seth-data.csv")

df = pd.read_csv(csv_file).dropna()
titles = df["title"].values
urls = df["url"].values
contents = df["content_plain"].values

file_path = 'embeddings_seth.tar.gz'

if not os.path.exists(file_path):
    st.write("El archivo embeddings_seth.tar.gz no se encuentra, generando el archivo...")
    
    subprocess.run(['python3', 'main.py'])

    time.sleep(10)

@st.cache_data
def load_data_embeddings():
    embeddings = txtai.Embeddings()
    embeddings.load(file_path)
    return titles, urls, contents, embeddings

titles, urls, contents, embeddings = load_data_embeddings()

st.title("📚 Seth's Blog Search")
st.write("Search Seth Godin's blog posts by topic or keyword.")

query = st.text_input("🔎 Enter your search:", "Books recommendation")

if st.button("🔍 Buscar"):
    if query:
        with st.spinner("Searching for results... ⏳"):
            time.sleep(1) 

            result = embeddings.search(query, 5)
            if result:
                st.subheader("Results:")
                for idx, (res_id, score) in enumerate(result):
                    title = titles[res_id]
                    url = urls[res_id]
                    content_snippet = " ".join(contents[res_id].split()[:20]) + "..." 

                    st.markdown(f"### {idx+1}. [{title}]({url})")
                    st.write(f"📖 {content_snippet}")
                    st.write(f"🔗 [Read more]({url})")
                    st.markdown("---")
            else:
                st.warning("No results found.")
    else:
        st.warning("Please enter a search term.")
