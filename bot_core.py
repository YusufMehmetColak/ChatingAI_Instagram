import openai
import requests
import json
from rapidfuzz import process
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN")
INSTAGRAM_SENDER_ID = os.getenv("INSTAGRAM_SENDER_ID")

def get_gpt_response(user_message):
    product_info = get_product_info(user_message)

    if not product_info:
        return (
            "Üzgünüm, belirttiğiniz ürünün hangi ürünümüz olduğunu anlayamadım. "
            "Lütfen ürün adını biraz daha açık yazar mısınız? Örneğin 'Beyaz Sneaker' gibi."
        )

    # Eğer ürün bulunduysa, GPT’ye bilgi ver
    system_prompt = (
        f"Sen bir müşteri temsilcisisin. Ürün bilgileri:\n"
        f"- Ürün adı: {product_info['name']}\n"
        f"- Fiyat: {product_info['price']}\n"
        f"- Stok: {product_info['stock']} adet\n"
    )
    if product_info["campaign"]:
        system_prompt += f"- Kampanya: {product_info['campaign']}\n"

    response = openai.ChatCompletion.create(
        model="gpt-insta-finetune",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    return response.choices[0].message.content.strip()



def send_message_to_user(recipient_id: str, message: str):
    url = f"https://graph.facebook.com/v19.0/me/messages"
    payload = {
        "messaging_type": "RESPONSE",
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    print("📬 Meta'ya mesaj gönderildi:", response.status_code, response.text)
    
    


def get_product_info(user_message):
    with open("products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    product_names = [product["name"] for product in products]

    # En benzer eşleşmeyi bul
    match = process.extractOne(user_message, product_names)

    if match:
        matched_name, score, _ = match
        print(f"🔍 En yakın eşleşme: {matched_name} (Skor: {score})")

        if score < 60:
            print("⚠️ Eşleşme skoru çok düşük, ürün yok sayılacak.")
            return None  # ürün yokmuş gibi davran

        # Skor yeterliyse, eşleşen ürünü döndür
        for product in products:
            if product["name"] == matched_name:
                return product

    return None

def log_to_file(content: str):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{now}] {content}\n"

    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log_line)