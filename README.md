# ShopAssist Mini
An AI support agent that investigates refund tickets using tools and asks a human to approve any refund.

## Who it's for / what it does / what "finished" means
- For: small online stores' support staff
- Task: resolve a refund ticket (lookup → policy check → recommendation → human approval)
- Finished: paste a ticket, see the agent's steps, approve/reject, database updates

## How to run
pip install -r requirements.txt
(add GEMINI_API_KEY to a .env file)
streamlit run ui.py

## AI Tools, Models & Libraries
- Model: Gemini 2.5 Flash via google-genai
- AI assistants used for coding: (list yours honestly)
- Libraries: streamlit, pydantic, python-dotenv