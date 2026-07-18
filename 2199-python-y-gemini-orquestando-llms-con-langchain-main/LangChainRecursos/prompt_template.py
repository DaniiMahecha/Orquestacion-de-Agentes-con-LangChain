from langchain_core.prompts import ChatPromptTemplate, PromptTemplate 

# TEMPLATE PARA LLM MULTIMODALES
template_entrada = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Asume que eres analista de imagénes. 
            Tu principal tarea consiste en:
            Analizar una imagen para extraer las informaciones más relevantes de manera objetiva

            # FORMATO DE SALIDA
            Descripción de la imagen: Tu descripción de la imagen aquí.
            Etiquetas: Una lista con 3 palabras-clave separadas por comas (,)
            """
        ),
        (   "user",
            [
                {
                    "type":"text",
                    "text":"Descrine la imagen: "
                },
                {
                    "type":"image_url",
                    "image_url":"data:image/jpeg;base64,{image}"
                }
            ]
        )
    ]
)

# TEMPLATE PARA LLM QUE ESPECIALIZADOS EN SOLO TEXTO O MÁS SENCILLOS
template_salida = PromptTemplate(
    template = """
                Genera un resumen, utilizando un lenguaje claro y objetivo,
                enfocado en el publico colombiano. La idea es que la comunicación del resultado sea
                lo más sencilla posible, priorizando los registros para consultas posteriores.

                #RESULTADO DE LA IMAGEN
                {image_analysis}
                """,
                input_variables=["image_analysis"]
)
