from LLMs import LLM_Gemini
from LangChainRecursos.prompt_template import agent_prompt
from langchain_core.globals import set_debug
from langchain.agents import create_react_agent, Tool
from LangChainRecursos import image_analysis_tool


set_debug(False)

class AgenteOrquestador:
    def __init__(self):
        self.LLM_Orquestador=LLM_Gemini

        image_analysis= image_analysis_tool.ImageAnalysisTool()

        self.tools=[
            Tool(
                name=image_analysis.name,
                func=image_analysis.run,
                description=image_analysis.description,
                return_direct=image_analysis.return_direct
            )
        ]

        prompt = agent_prompt,

        self.agent = create_react_agent(self.LLM_Orquestador, self.tools, prompt)
