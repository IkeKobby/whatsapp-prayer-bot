import os
import json
import re
from twilio.rest import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Load credentials from environment
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
to_whatsapp = os.getenv("TO_WHATSAPP_NUMBER")
content_sid = os.getenv("TEMPLATE_SID")

client = Client(account_sid, auth_token)

# Clean dynamic content for Twilio template compatibility
def sanitize_text(text):
    text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove emojis/special chars
    text = text.replace('*', '').replace('\n', ' ')
    return text.strip()

# Daily prayer schedule
prayer_schedule = {
    "Monday": {
        "title": "Overturning the Enemy’s Agenda",
        "message": "By the blood of Jesus, I overturn every plan and advantage the enemy is using against my life, marriage, and family. (Isaiah 54:17)"
    },
    "Tuesday": {
        "title": "Releasing Supernatural Increase",
        "message": "I release increase over my household, academics, life, and marriage. (Deuteronomy 1:11)"
    },
    "Wednesday": {
        "title": "Wisdom & Academic Excellence",
        "message": "I receive divine wisdom, insight, and mental clarity. (Daniel 1:17)"
    },
    "Thursday": {
        "title": "Marital Blessings & Fruitfulness",
        "message": "I declare peace, joy, and unity in my marriage. (Ecclesiastes 4:12)"
    },
    "Friday": {
        "title": "Career Breakthrough",
        "message": "Father, establish the work of my hands and open doors of favor. (Psalm 90:17)"
    },
    "Saturday": {
        "title": "Financial Overflow",
        "message": "I walk in divine provision and wealth with purpose. (Psalm 115:14)"
    },
    "Sunday": {
        "title": "Protection & Restoration",
        "message": "My household is covered. I receive restoration and peace. (Joel 2:25)"
    }
}

# Get today's prayer
today = datetime.today().strftime("%A")
prayer = prayer_schedule.get(today)

if prayer:
    title = sanitize_text(prayer["title"])
    message_body = sanitize_text(prayer["message"])

    print("Sending WhatsApp message with:")
    print(f"FROM: whatsapp:+14155238886")
    print(f"TO: {to_whatsapp}")
    print(f"TEMPLATE SID: {content_sid}")
    print(f"CONTENT VARIABLES: {{\"1\":\"{title}\", \"2\":\"{message_body}\"}}")


    print("📍 Loaded updated script. Media URL is: https://raw.githubusercontent.com/IkeKobby/whatsapp-prayer-bot/master/img.png")

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to=to_whatsapp,
        content_sid=content_sid,
        content_variables=json.dumps({
            "1": title,
            "2": message_body
        }),
        media_url=["https://raw.githubusercontent.com/IkeKobby/whatsapp-prayer-bot/master/img.png"]
    )


    print(f"✅ Prayer sent: {message.sid}")
else:
    print("⛔ No prayer found for today.")