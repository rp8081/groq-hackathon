import re
from langchain_core.messages import AIMessage, HumanMessage
from typing import Dict, Any

class PortfolioInputAgent:
    name = "PortfolioInputAgent"

    def __init__(self, llm=None):
        self.llm = llm

    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        msgs = state.get("messages") or []
        goal = getattr(msgs[-1], "content", str(msgs[-1])) if msgs else ""

        alloc = {}
        # Parse patterns like RELIANCE 40, TCS 30
        for token in re.findall(r"([A-Z]{2,10})\s*(\d+)", goal.upper()):
            ticker, qty = token
            alloc[ticker] = int(qty)

        if alloc:
            total = sum(alloc.values())
            alloc_pct = {t: round(q/total, 4) for t,q in alloc.items()}
            state["current_alloc"] = alloc_pct
            state["messages"].append(AIMessage(content=f"[PortfolioInputAgent] Parsed allocations: {alloc_pct}"))
        else:
            state["messages"].append(AIMessage(content="[PortfolioInputAgent] No portfolio detected."))
        return state
