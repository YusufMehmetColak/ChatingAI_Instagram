# ChatingAI_Instagram
To build an AI-powered system that automatically replies to thousands of customer messages on Instagram DMs and WhatsApp, using a GPT-based model (like OpenAI’s GPT-3.5). The system should provide accurate, up-to-date, and brand-aligned responses — especially in retail and e-commerce contexts.

Absolutely! Here’s a professional and clean README.md file tailored for your project — ideal for GitHub, team collaboration, or onboarding contributors.

⸻



# 🤖 AI-Powered Instagram & WhatsApp Chatbot

An automated customer service assistant powered by OpenAI’s GPT model, integrated with Instagram and WhatsApp through Meta’s Graph API and Cloud API.  
Perfect for retail/e-commerce brands handling large volumes of direct messages.

---

## 📌 Features

- 🔗 **Instagram & WhatsApp Integration** (via Meta API)
- 🧠 **GPT-3.5 Responses** — powered by OpenAI
- 🗃️ **Product Data Integration** — prices, stock, campaigns
- 🔍 **Fuzzy Matching** — typo-tolerant product search
- 💬 **Multi-platform Support** — extendable to Messenger, webchat
- 🧾 **Conversation Logging** — saves incoming & outgoing messages
- ⚙️ **Customizable Prompts** — brand tone & style
- 👤 **Human-in-the-loop (optional)**

---

## 🚀 Tech Stack

| Area          | Technology        |
|---------------|-------------------|
| Backend       | Python, FastAPI   |
| Server        | Uvicorn + Ngrok (for dev) |
| AI Engine     | OpenAI GPT-3.5    |
| Messaging     | Meta Graph API, WhatsApp Cloud API |
| Storage       | JSON / SQLite / Google Sheets |
| Dev Tools     | dotenv, rapidfuzz |

---

## 📁 Folder Structure

📦 project/
├── main.py                  # Webhook endpoints (GET + POST)
├── bot_core.py              # GPT logic, fuzzy matching, message sending
├── products.json            # Product data (dynamic knowledge)
├── .env                     # Environment variables (API keys, tokens)
├── log.txt                  # Logs incoming/outgoing messages
└── README.md                # You’re here!

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo

2. Install dependencies

pip install -r requirements.txt

3. Create .env file

OPENAI_API_KEY=sk-...
META_ACCESS_TOKEN=EAA...
VERIFY_TOKEN=your_webhook_token

4. Run the FastAPI server

uvicorn main:app --reload --port 8000

5. Start Ngrok (for webhook testing)

ngrok http 8000



⸻

🔐 Meta API Permissions Required
	•	pages_messaging
	•	instagram_basic
	•	instagram_manage_messages
	•	pages_show_list
	•	(For WhatsApp: setup via WhatsApp Cloud API)

📘 Meta Permissions Docs
📘 Instagram Messaging API

⸻

💡 Customization
	•	Customize prompt style in get_gpt_response() (tone, brand language)
	•	Replace products.json with your own product DB, API, or Google Sheet
	•	Enable function calling for smart actions (e.g. DB queries, shipping ETA)

⸻

🧪 Example Prompt

User: “beyaz snikır var mı?”
GPT: “Beyaz Sneaker ürünümüz 599 TL’dir ve şu anda 12 adet stok bulunmaktadır. Ayrıca ‘2 al 1 bedava’ kampanyası geçerlidir!”

⸻

📝 License

MIT License © 2025

⸻

🙋‍♂️ Contact / Contribute

Have ideas or want to contribute?
Reach out via Instagram or open a pull request!

---

