from langchain_core.tools import tool


@tool
def fetch_discount_coupon() -> str:
    """
    Fetch a special discount coupon from the database to soothe dissatisfied customers or those who had issues.
    """
    return "DESC_COMPENSACAO_20"
