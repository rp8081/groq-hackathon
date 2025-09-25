from langgraph.graph import StateGraph, START, END
from .state import FinanceState
from .agents import Supervisor, PortfolioInputAgent, MarketDataAgent, RiskAgent, PortfolioAgent, ExecutionAgent


def build_finance_graph(llm):
    sup = Supervisor(llm)

    # ✅ FIX: supervisor must return dict, not raw string
    def supervisor_node(state: FinanceState) -> dict:
        decision = sup.route(state)
        return {"_next": decision}

    graph = StateGraph(FinanceState)

    # --- nodes ---
    graph.add_node("supervisor", supervisor_node)
    graph.add_node("portfolioinput", PortfolioInputAgent().run)
    graph.add_node("market", MarketDataAgent().run)
    graph.add_node("risk", RiskAgent().run)
    graph.add_node("portfolio", PortfolioAgent().run)
    graph.add_node("execution", ExecutionAgent().run)

    # --- edges ---
    graph.add_edge(START, "supervisor")

    graph.add_conditional_edges(
        "supervisor",
        lambda state: state["_next"],
        {
            "portfolioinput": "portfolioinput",
            "market": "market",
            "risk": "risk",
            "portfolio": "portfolio",
            "execution": "execution",
            "done": END,
        }
    )

    for node in ["portfolioinput", "market", "risk", "portfolio", "execution"]:
        graph.add_edge(node, "supervisor")

    return graph.compile()
