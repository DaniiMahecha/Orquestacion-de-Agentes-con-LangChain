from LangChainRecursos.prompt_template import template
from LLMs.LLM_Gemini import llmGemini
from langchain_core.output_parsers import StrOutputParser
from my_helper import encode_image

# Imagen en cadena de texto
image=encode_image("datos\ejemplo_grafico.jpg")

# LangChain Expression Language (LCEL).
lcel= template | llmGemini | StrOutputParser

# Respuesta del LLM
response=lcel.invoke({"image":image})

print(response)