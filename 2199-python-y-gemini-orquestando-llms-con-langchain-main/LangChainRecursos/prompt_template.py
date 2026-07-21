from langchain_core.prompts import ChatPromptTemplate, PromptTemplate 
from langchain_core.output_parsers import JsonOutputParser
from detalles_imagen_json import DetallesImagenJSON
from langchain import hub

# JSON PARSER
json_parser = JsonOutputParser(
    pydantic_object=DetallesImagenJSON
)

# TEMPLATE PROMPT LLMs AGENT
agent_prompt = hub.pull("hwchase17/react")
# Answer the following questions as best you can. You have access to the following tools:
# 
# {tools}
#
# Use the following format:
#
# Question: the input question you must answer
# Thought: you should always think about what to do
# Action: the action to take, should be one of [{tool_names}]
# Action Input: the input to the action
# Observation: the result of the action
# ... (this Thought/Action/Action Input/Observation can repeat N times)
# Thought: I now know the final answer
# Final Answer: the final answer to the original input question
#
# Begin!
#
# Question: {input}
# Thought:{agent_scratchpad}

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

                #FORMATO DE SALIDA
                {output_format}
                """,
                input_variables=["image_analysis"],
                partial_variables={
                    "output_format":json_parser.get_format_instructions
                }
)
