import yfinance as yf
import json
from langchain_core.tools import tool

@tool
def coletar_dados_yfinance(ticker: str) -> str:
    """
    Coleta dados financeiros em tempo real e indicadores de uma ação usando o Yahoo Finance.
    O formato do ticker deve ser o padrão do Yahoo (ex: 'PETR4.SA' para Petrobras ou 'AAPL' para Apple).
    """
    try:
        acao = yf.Ticker(ticker)
        info = acao.info
        
        # Filtramos apenas o que o agente realmente precisa para a regra do SKILL.md
        dados_filtrados = {
            "ticker": ticker,
            "nome": info.get("longName", "N/A"),
            "preco_atual": info.get("currentPrice") or info.get("regularMarketPrice"),
            "preco_fechamento_anterior": info.get("previousClose"),
            "media_50_dias": info.get("fiftyDayAverage"),
            "volume_atual": info.get("volume"),
            "volume_medio": info.get("averageVolume"),
            "moeda": info.get("currency", "BRL")
        }
        
        # Calcula a variação percentual do dia para ajudar o agente
        if dados_filtrados["preco_atual"] and dados_filtrados["preco_fechamento_anterior"]:
            var = ((dados_filtrados["preco_atual"] - dados_filtrados["preco_fechamento_anterior"]) / dados_filtrados["preco_fechamento_anterior"]) * 100
            dados_filtrados["variacao_dia"] = round(var, 2)
        else:
            dados_filtrados["variacao_dia"] = 0.0

        return json.dumps(dados_filtrados, ensure_ascii=False)
        
    except Exception as e:
        return json.dumps({"erro": f"Não foi possível coletar dados para o ticker {ticker}. Motivo: {str(e)}"})