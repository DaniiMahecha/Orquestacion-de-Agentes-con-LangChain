from LangChainRecursos.prompt_template import template_entrada, template_salida, json_parser
from LLMs.LLM_Gemini import llmGemini
from LLMs.LLM_Cohere import llmCohere
from langchain_core.output_parsers import StrOutputParser
from my_helper import encode_image
from langchain_core.globals import set_debug



# Modo Depuración para observar la cadena de procesos paso a paso.
set_debug(True)

# Imagen en cadena de texto
image=encode_image("datos\ejemplo_grafico.jpg")

# LangChain Expression Language (LCEL).
image_analysis = template_entrada | llmGemini | StrOutputParser()
sumary = template_salida | llmCohere | json_parser

result = (image_analysis | sumary)

# Respuesta del LLM
# StrOutputParser limpia la respuesta del modelo y se encarga de
# devolver la respuesta en un simple cadena de caracteres.
response=result.invoke({"image":image})