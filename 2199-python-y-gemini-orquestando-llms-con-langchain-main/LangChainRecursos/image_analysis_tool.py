from langchain.tools import BaseTool
from LangChainRecursos import prompt_template
from LLMs import LLM_Gemini
from detalles_imagen_json import DetallesImagenJSON
from langchain_core.output_parsers import JsonOutputParser
from my_helper import encode_image
import ast

class ImageAnalysisTool(BaseTool):
    name:str = "ImageAnalisysTool"
    description:str = """
                        Utiliza esta herramienta siempre  que te sea solicitado
                        realizar un análisis de imagen.

                        # ENTRADAS REQUERIDAS
                        - 'nombre_imagen' (str) : Nombre de la imagen a ser analizada con extensión JPG.
                        Ejemplo: test.jps o test.jpeg
                        """
    return_direct:bool = False

    def _run(self,action):
        action= ast.literal_eval(action)
        image_route = action.get("image_name","")

        llmGemini = LLM_Gemini
        image = encode_image(f'datos{image_route}')
        json_parser = JsonOutputParser(
            pydantic_object=DetallesImagenJSON
        )

        image_analysis = prompt_template.template_entrada | llmGemini | StrOutputParser()
        sumary = prompt_template.template_salida | llmGemini | json_parser

        result = (image_analysis | sumary)  

        # Respuesta del LLM
        # StrOutputParser limpia la respuesta del modelo y se encarga de
        # devolver la respuesta en un simple cadena de caracteres.
        response=result.invoke({"image":image})


        return response