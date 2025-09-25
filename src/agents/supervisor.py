from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from typing import Dict, Any


class Supervisor:
    def __init__(self, llm):
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_template(
            "You are the Supervisor. Decide the next agent.\n"
            "Options: portfolioinput | market | risk | portfolio | execution | done\n"
            "Rules:\n"
            "- If no current_alloc -> portfolioinput\n"
            "- If no prices -> market\n"
            "- If no risk -> risk\n"
            "- If no target_alloc -> portfolio\n"
            "- If no orders -> execution\n"
            "- Else -> done\n\n"
            "State: {state}\n"
            "User goal: {goal}"
        )

    def route(self, state: Dict[str, Any]) -> str:
        goal = ""
        msgs = state.get("messages") or []
        if msgs:
            last = msgs[-1]
            goal = getattr(last, "content", str(last))

        try:
            msg = self.prompt.format(
                state=str({
                    "has_alloc": bool(state.get("current_alloc")),
                    "has_prices": bool(state.get("prices")),
                    "has_risk": bool(state.get("risk")),
                    "has_target": bool(state.get("target_alloc")),
                    "has_orders": state.get("orders") is not None,
                }),
                goal=goal
            )
            out = self.llm.invoke([HumanMessage(content=str(msg))])
            token = getattr(out, "content", "").strip().lower()
            if token in {"portfolioinput","market","risk","portfolio","execution","done"}:
                return token
        except Exception:
            pass

        # ✅ fallback (deterministic)
        if not state.get("current_alloc"):
            return "portfolioinput"
        if not state.get("prices"):
            return "market"
        if not state.get("risk"):
            return "risk"
        if not state.get("target_alloc"):
            return "portfolio"

        # ✅ execution guard: only allow once
        if state.get("orders") is None:
            if state.get("execution_count", 0) > 0:
                return "done"
            return "execution"

        return "done"
