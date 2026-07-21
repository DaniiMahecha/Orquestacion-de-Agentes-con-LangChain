from langchain.agents import AgentExecutor
from LLMs.LLM_agent import AgenteOrquestador

def main():
    agente = AgenteOrquestador()
    executor = AgentExecutor(
        agent=agente.agent,
        tools=agente.tools,
        verbose = True
    )

    pregunta = "Realiza el análisis de la imagen ejemplo_grafico.jpg"
    response= executor.invoke({"input":pregunta})

    print(response)

if __name__ == '__main__':
    main()