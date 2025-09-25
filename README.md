📈 Finance Agent – Multi-Modal Portfolio Rebalancer

An advanced LangGraph + LangChain-Groq powered Finance Agent that helps you analyze, rebalance, and simulate portfolios with agentic workflows. Built to be hackathon-level complex — modular, extensible, and ready for real-world finance integrations.

🚀 Features

Multi-Agent Workflow (LangGraph)

PortfolioInputAgent → parses portfolio allocations from user input
MarketDataAgent → fetches historical prices (via yfinance)
RiskAgent → computes risk metrics (volatility, VaR, drawdown)
PortfolioAgent → suggests rebalancing allocations
ExecutionAgent → simulates trade orders
Supervisor → orchestrates the flow, avoids infinite loops

Groq LLM Integration

Uses Groq-hosted models (gemma2-9b-it) for reasoning and parsing
Ultra-low latency inference
Multi-Modal Input (🚧 In Progress 🚧)

Text (✅ Working): "RELIANCE 40, TCS 30, HDFCBANK 20, INFY 10"

Voice (Pipeline): 🎤 Whisper-based transcription (Groq/Whisper local)
Image (Pipeline): 🖼️ Extract allocations from screenshots, scanned docs, or notes

Visualization

Historical price charts
Orders exportable to CSV
Extensibility
Modular code (src/agents/, src/utils/, src/plotter.py)

Easy to plug new agents (e.g., compliance, execution with broker APIs)

📂 Project Structure
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
│       └── modality_preprocessors.py  # Voice/Image → Text (pipeline)
│── requirements.txt
│── README.md

⚙️ Installation
1. Clone & Setup
git clone https://github.com/yourusername/finance_agent.git
cd finance_agent
python -m venv venv
source venv/bin/activate   # (or venv\Scripts\activate on Windows)

2. Install Dependencies
pip install -r requirements.txt


Key dependencies:

langchain
langgraph
langchain-groq
gradio
pandas
matplotlib
yfinance
rapidfuzz
(Pipeline only) openai-whisper, imageio-ffmpeg
🔑 Environment Setup

Set your Groq API key:

export GROQ_API_KEY="your_groq_key_here"   # macOS/Linux
set GROQ_API_KEY=your_groq_key_here        # Windows PowerShell

▶️ Run the App
python -m src.app


Gradio UI will launch at:
👉 http://127.0.0.1:7860

🧪 Example Input

Text (working):

RELIANCE 40, TCS 30, HDFCBANK 20, INFY 10


Voice (pipeline):

I have 30 shares of TCS and 40 shares of Infosys


Image (pipeline):
A photo of a handwritten note:

TCS – 30
INFY – 40

📊 Output

Agent Trace (colored agent steps)

Final Orders Table

Price Chart 📈

CSV Download of orders

🛠️ Roadmap

 Core multi-agent workflow

 Price chart + CSV export

 🎤 Voice → Text via Whisper

 🖼️ Image → Text via Groq Vision

 ✅ MCP Integration

Market Data Fetcher (MCP tool for trading APIs)

Compliance Logger (MCP → DB for audit trail)

 🔗 Broker API (Zerodha, Upstox) integration

 🔒 Role-based access & auditability

 📱 Deployable as Streamlit / FastAPI microservice

