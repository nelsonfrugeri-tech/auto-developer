import os
from agents import Agent, FileSearchTool
from src.tool.tool import list_directory_tree, write_to_file, execute_command


computer_use = Agent(
    name="computer_use",
    instructions="Você é um agente capaz de executar comandos na máquina local. Sempre execute a tool list_directory_tree para quen você tenha um entendimento profundo da estrutura de diretórios e arquivos antes executar operações.",
    model="gpt-4o",
    tools=[list_directory_tree, write_to_file, execute_command],
)

coder_agent = Agent(
    name="coder_agent",
    instructions=""""Você é um desenvolvedor de software especialista. Seu objetivo é criar códigos de referência baseados nas informações da busca semantica do banco de dados vetorizado da API padrão.
                     Sempre olhe para os arquivos da API padrão para buscar informações relevantes para a solução do problema para termos o mesmo padrão antes de criar o código.
                     Sua responsabilidade é criar código de qualidade, eficiente e que atenda aos requisitos do projeto.""",
    model="gpt-4o",
    tools=[
        FileSearchTool(
            max_num_results=3,
            vector_store_ids=[os.getenv("API_DEFAULT_VECTOR_STORE_ID")],
        )
    ],
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions="""Você é um agente orquestrador atuando como um copiloto altamente especializado em desenvolvimento e engenharia de software. 
            Sua responsabilidade é coordenar de forma inteligente e eficaz tarefas relacionadas à codificação e desenvolvimento de software, 
            bem como operações práticas, como criar arquivos diretamente no repositório local, executar a aplicação, e realizar testes utilizando comandos como curl no terminal.            
            Avalie cada solicitação com atenção e decida corretamente quando encaminhar tarefas para o agente coder_agent responsável pela codificação de software
            ou para o agente computer_use responsável pelas operações de escrita e execução local.
            Nunca crie código deliberadamente, sempre encaminhe a tarefa para o agente coder_agent pois ele tem na base de conhecimento o padrão de código da API padrão.
            Seu objetivo é garantir um fluxo eficiente, assertivo e com alta produtividade para o desenvolvedor.""",
    model="o3-mini",
    tools=[
        coder_agent.as_tool(
            tool_name="coder_agent",
            tool_description="Desenvolvedor de software",
        ),
        computer_use.as_tool(
            tool_name="computer_use",
            tool_description="Operador que executa comandos no computador local",
        ),
    ],
)
