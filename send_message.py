import os
import requests
from dotenv import load_dotenv

# Charger le fichier .env
load_dotenv()

# Récupérer les infos du .env
TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not TOKEN or not CHAT_ID:
    print("❌ Erreur : TOKEN ou CHAT_ID manquant dans le .env")
    exit()

# Message de test
message = "✅ Test réussi ! Le bot Telegram SystèmeGPT_Render est connecté 🚀"

# Envoi du message
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {"chat_id": CHAT_ID, "text": message}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("✅ Message envoyé avec succès !")
else:
    print(f"❌ Erreur lors de l’envoi : {response.text}")
