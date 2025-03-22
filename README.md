# Coder-Pilot: Autopilot para Desenvolvimento de Software

## Visão Geral
O Coder-Pilot é uma solução avançada de autopilot para desenvolvimento de software que utiliza múltiplos agentes de IA para auxiliar desenvolvedores em tarefas de codificação. O sistema é projetado para entender, gerar e executar código baseado na base de conhecimento do desenvolvedor, aumentando significativamente a produtividade.

## Arquitetura

### Componentes Principais

#### 1. Orquestrador
O coração do sistema é o `orchestrator_agent` que coordena o fluxo de trabalho entre os agentes especializados. Este agente decide quando direcionar tarefas para:
- O agente de codificação (`coder_agent`) - para gerar código baseado em padrões existentes
- O agente de operações (`computer_use`) - para executar comandos no sistema local

#### 2. Agentes Especializados
- **Coder Agent**: Especializado em desenvolvimento de software, utiliza uma base de conhecimento vetorizada para gerar código seguindo padrões estabelecidos.
- **Computer Use Agent**: Responsável por interagir com o sistema de arquivos e executar comandos, permitindo operações práticas como criação de arquivos e execução de aplicações.

#### 3. API
O projeto expõe uma API compatível com o padrão OpenAI Chat Completions, facilitando a integração com ferramentas existentes. A API é construída com FastAPI e oferece:
- Suporte a streaming de respostas
- Endpoint compatível com o formato do OpenAI

#### 4. Frontend
Um frontend simples construído com Streamlit que permite interagir com o sistema através de uma interface de chat.

#### 5. Ferramentas (Tools)
O sistema inclui ferramentas utilitárias que permitem aos agentes:
- Listar estruturas de diretórios
- Escrever conteúdo em arquivos
- Executar comandos no sistema operacional

### Diagrama de Fluxo
1. O usuário envia uma consulta através da API ou interface web
2. O orquestrador avalia a consulta e decide qual agente especializado deve responder
3. Se necessário, os agentes utilizam as ferramentas para realizar operações no sistema
4. A resposta é retornada ao usuário, possivelmente em formato de streaming

## Requisitos
- Python 3.9+
- Conta OpenAI com acesso a modelos GPT-4o e GPT-3.5
- ID de armazenamento vetorial para a base de conhecimento (configurado no .env)

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/coder-pilot.git
cd coder-pilot
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo .env:
```
API_DEFAULT_VECTOR_STORE_ID="seu_vector_store_id"
```

## Como Executar

### Servidor API
Para iniciar o servidor API:
```bash
cd coder-pilot
python -m src.app
```
O servidor estará disponível em http://localhost:8080

### Interface Web
Para iniciar a interface web Streamlit:
```bash
cd coder-pilot
streamlit run src/front/streamlit.py
```
A interface web estará disponível em http://localhost:8501

## Uso
1. Acesse a interface web ou conecte-se à API
2. Descreva a tarefa de desenvolvimento que você precisa realizar
3. O sistema irá gerar, modificar ou executar código conforme solicitado
4. Para tarefas complexas, o sistema pode solicitar informações adicionais

## Personalização
- Modifique o arquivo `src/agent/agent.py` para ajustar as instruções dos agentes
- Personalize as ferramentas em `src/tool/tool.py` conforme necessário
- Ajuste o valor de `base_path` em `tool.py` para o diretório do seu projeto

## Limitações
- O sistema requer acesso a modelos avançados de IA como GPT-4o
- As capacidades de execução de comandos devem ser utilizadas com cuidado em ambientes de produção

## Contribuições
Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar pull requests ou abrir issues para melhorias. 