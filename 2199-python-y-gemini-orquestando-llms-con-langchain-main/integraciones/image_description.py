# Se hacen los imports correspondientes con intreprete del ambiente .venv-gemini-3
from LLMs.LLM_Gemini import llmGemini
from langchain_core.messages import HumanMessage
from my_helper import encode_image


# Para hacer la prueba de la integreación con el LLM
# Usaremos una imagen dentro de datos/ usaremos my_helper
# Para pasar de la imagen a una cadena de texto
# Y le diremos al LLM que la describa.

imagen = encode_image('datos/ejemplo_grafico.jpg')
pregunta = "Describe la imagen: "

# HumanMessage con contenido mixto: un bloque de tipo texto y otro de tipo imagen,
# codificado como data URL (base64) para que el modelo pueda interpretarlo.
prompt = HumanMessage(
    content=[
        {
            "type":"text",
            "text":pregunta
        },
        {
            "type":"image_url",
            "image_url": f'data:image/jpeg;base64,{imagen}' 
        }
    ]
)

# Se envía el prompt al modelo y se obtiene la respuesta generada.
respuesta = llmGemini.invoke([prompt])

print(respuesta)