import os
from dotenv import load_dotenv
load_dotenv()

GROQ_API_KEY=os.getenv('GROQ_API_KEY')

MODEL_NAME=os.getenv('MODEL_NAME')
MAX_TOKEN_ALLOWED=int(os.getenv('MAX_TOKEN_ALLOWED'))
MODEL_TEMPERATURE=float(os.getenv('MODEL_TEMPERATURE'))

#hugging face for embedding model
EMBEDDING_MODEL=os.getenv('EMBEDDING_MODEL')



