from langchain_community.embeddings import HuggingFaceEmbeddings
from  config import EMBEDDING_MODEL

class EmbeddingModel:
    '''
    
    responsible  for loading the embedding model from the hugging face'''

    def __init__(self):
        self.embedding=HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    def get_embedding(self):
        return self.embedding    