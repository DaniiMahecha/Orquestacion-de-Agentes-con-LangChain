from langchain_cohere import ChatCohere
from my_keys import COHERE_API_KEY

llmCohere = ChatCohere(
    api_key=COHERE_API_KEY
)
