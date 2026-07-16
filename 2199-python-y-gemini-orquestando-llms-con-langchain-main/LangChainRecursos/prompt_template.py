from langchain.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            Asume que eres analista de imagénes. 
            Tu principal tarea consiste en:
            Analizar una imagen para extraer las informaciones más relevantes de manera objetiva
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


