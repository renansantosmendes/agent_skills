import sys
sys.stdout.reconfigure(encoding="utf-8")

from deepagents import create_deep_agent
from skills.stock_analysis.tools import collect_yfinance_data
from skills.sentiment_analysis.tools import fetch_discount_coupon
from skills.fundamental_analysis.tools import collect_fundamental_indicators
from skills.technical_analysis.tools import collect_technical_indicators
from skills.asset_comparison.tools import compare_assets

from dotenv import load_dotenv
load_dotenv()

from deepagents.backends.filesystem import FilesystemBackend

backend = FilesystemBackend(
    root_dir="/content",
    virtual_mode=False,   # evita o warning
)

agent = create_deep_agent(
    model="openai:gpt-5-nano",
    tools=[
        collect_yfinance_data,
        fetch_discount_coupon,
        collect_fundamental_indicators,
        collect_technical_indicators,
        compare_assets,
    ],
    skills=["./skills/"],
    backend=backend,
)

inputs = {"messages": [{"role": "user", "content": "PETR4 está cara ou barata pelos fundamentos?"}]}
# inputs = {"messages": [{"role": "user", "content": "Me dá o RSI e MACD da VALE3"}]}
# inputs = {"messages": [{"role": "user", "content": "Compara PETR4, VALE3 e ITUB4 pra mim"}]}

config = {"configurable": {"thread_id": "investidor_01"}}

for chunk in agent.stream(inputs, config):
    print(chunk)