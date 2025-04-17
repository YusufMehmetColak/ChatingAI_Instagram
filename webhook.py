from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


@app.get("/webhook")
async def verify_webhook(request: Request):
    params = dict(request.query_params)

    if params.get("hub.mode") == "subscribe" and params.get("hub.verify_token") == VERIFY_TOKEN:
        print("✅ Webhook doğrulandı.")
        return int(params["hub.challenge"])
    
    print("❌ Webhook doğrulama başarısız.")
    return {"status": "error", "message": "Invalid token"}

@app.post("/webhook")
async def receive_webhook(request: Request):
    data = await request.json()
    print("🎯 GELEN MESAJ:", data)  # gelen mesajı logla
    
    # Buradan mesaj metnini al
    user_message = data["entry"][0]["messaging"][0]["message"]["text"]
    
    # GPT'ye gönder
    response = get_gpt_response(user_message)
    
    return {"status": "ok"}