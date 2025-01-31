import kagglehub
import os
import pandas as pd
import txtai

dataset_path = kagglehub.dataset_download("glushko/seth-godins-blogs-dataset")

csv_file = os.path.join(dataset_path, "seth-data.csv") 

df = pd.read_csv(csv_file).dropna()

content = df["content_plain"].values

embeddings = txtai.Embeddings({
    'path': 'sentence-transformers/all-MiniLM-L6-v2',
})

embeddings.index([(i, text, None) for i, text in enumerate(content)])

embeddings.save('embeddings_seth.tar.gz')

print("✅ Embeddings generados y guardados en 'embeddings_seth.tar.gz'")
