from langchain_core.tools import tool

@tool
def buscar_cupons_desconto() -> str:
    """
    Busca um cupom de desconto especial no banco de dados para acalmar clientes insatisfeitos ou que tiveram problemas.
    """
    # Aqui em produção você faria uma query no banco ou bateria em uma API de e-commerce (Ex: VTEX, Shopify)
    return "DESC_COMPENSACAO_20"