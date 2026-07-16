from LLMs.LLM_Gemini import llmGemini
from LLMs.LLM_Cohere import llmCohere
from langchain_core.messages import HumanMessage



# Interacción con los LLM
respuestaGemini= llmGemini.invoke("Planes para novios en Bogotá con el mejor precio")
print(f"Gemini: ", respuestaGemini.content)

respuestaCohere= llmCohere.invoke([HumanMessage(content="Planes para novios en Bogotá con el mejor precio")])
print(f"Cohere: ", respuestaCohere.content)