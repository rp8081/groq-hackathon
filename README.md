# 📈 Finance Agent – Multi-Modal Portfolio Rebalancer

An advanced **LangGraph + LangChain-Groq** powered Finance Agent that helps you analyze, rebalance, and simulate portfolios with **agentic workflows**.  


---

## 🚀 Features

### 🧩 Multi-Agent Workflow (LangGraph)
- **PortfolioInputAgent** → parses portfolio allocations from user input  
- **MarketDataAgent** → fetches historical prices (via yfinance)  
- **RiskAgent** → computes risk metrics (volatility, VaR, drawdown)  
- **PortfolioAgent** → suggests rebalancing allocations  
- **ExecutionAgent** → simulates trade orders  
- **Supervisor** → orchestrates the flow, avoids infinite loops  

### ⚡ Groq LLM Integration
- Uses Groq-hosted models (`gemma2-9b-it`) for reasoning and parsing  
- Ultra-low latency inference  

### 🖼️ Multi-Modal Input (🚧 In Pipeline)
- **Text (✅ Working):**  
  `RELIANCE 40, TCS 30, HDFCBANK 20, INFY 10`  
- **Voice (🚧 In Progress):** 🎤 Whisper-based transcription  
- **Image (🚧 In Progress):** 🖼️ Extract allocations from screenshots, scanned docs, or notes  

### 📊 Visualization
- Historical price charts  
- Orders exportable to CSV  

### 🔧 Extensibility
- Modular code (`src/agents/`, `src/utils/`, `src/plotter.py`)  
- Easy to plug new agents (e.g., compliance, broker API execution, MCP tools)  

---

## 📂 Project Structure

```text
finance_agent/
│── src/
│   ├── app.py                  # Gradio UI entry point
│   ├── graph_builder.py        # LangGraph workflow
│   ├── plotter.py              # Price chart generator
│   ├── agents/
│   │   ├── supervisor.py       # Supervisor logic
│   │   ├── portfolio_input_agent.py
│   │   ├── market_data_agent.py
│   │   ├── risk_agent.py
│   │   ├── portfolio_agent.py
│   │   └── execution_agent.py
│   └── utils/
│       └── modality_preprocessors.py   # Voice/Image → Text (pipeline)
│── requirements.txt
│── README.md

# 📈 Installation

### 🔧 Clone & Setup

git clone https://github.com/yourusername/finance_agent.git
cd finance_agent
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

