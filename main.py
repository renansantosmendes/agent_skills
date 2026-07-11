import sys
sys.stdout.reconfigure(encoding="utf-8")

from deepagents import create_deep_agent
# Importa as ferramentas de suas respectivas pastas
from skills.analise_acoes.tools import coletar_dados_yfinance
from skills.analise_sentimento.tools import buscar_cupons_desconto
from dotenv import load_dotenv
load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

# Inicializa o agente passando a lista de TODAS as ferramentas disponíveis
agent = create_deep_agent(
    model="openai:gpt-5-nano",
    tools=[coletar_dados_yfinance, buscar_cupons_desconto],
    skills=["./skills/"] # Varre a pasta raiz de skills e acha os dois SKILL.md
)


inputs = {"messages": [{"role": "user", "content": "O produto chegou todo quebrado, estou muito chateado!"}]}

# inputs = {"messages": [{"role": "user", "content": "Veja o preço da VALE3 para mim?"}]}

# inputs = {"messages": [{"role": "user", "content": "Dá uma olhada em como tá a Petrobras hoje e me diz se vale a pena comprar"}]}
config = {"configurable": {"thread_id": "investidor_01"}}

for chunk in agent.stream(inputs, config):
    print(chunk)