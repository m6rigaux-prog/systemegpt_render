import requests

# Remplace par le token de ton bot Telegram
TOKEN = "TON_TOKEN_ICI"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

print("Envoie un message à ton bot sur Telegram (ex: 'salut') puis appuie sur Entrée ici.")
input("Appuie sur Entrée après avoir envoyé ton message... ")

r = requests.get(url)
data = r.json()

try:
    chat_id = data["result"][-1]["message"]["chat"]["id"]
    print(f"✅ Ton chat_id est : {chat_id}")
except Exception as e:
    print("❌ Impossible de récupérer le chat_id. Vérifie que tu as bien envoyé un message au bot.")
    print(e)
