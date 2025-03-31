import os
from twilio.rest import Client
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Get credentials from .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
to_whatsapp = os.getenv("TO_WHATSAPP_NUMBER")
content_sid = os.getenv("TEMPLATE_SID")

client = Client(account_sid, auth_token)

prayer_schedule = {
    "Monday": {
        "title": "Overturning the Enemy’s Agenda",
        "message": "By the blood of Jesus, I overturn every plan... (Isaiah 54:17)"
    },
    "Tuesday": {
        "title": "Releasing Supernatural Increase",
        "message": "I release the increase... (Deuteronomy 1:11)"
    },
    "Wednesday": {
        "title": "Wisdom & Academic Excellence",
        "message": "I receive wisdom... (Daniel 1:17)"
    },
    "Thursday": {
        "title": "Marital Blessings & Fruitfulness",
        "message": "I declare unity and peace... (Ecclesiastes 4:12)"
    },
    "Friday": {
        "title": "Career Breakthrough",
        "message": "Father, grant me favor... (Psalm 90:17)"
    },
    "Saturday": {
        "title": "Financial Overflow",
        "message": "I declare dominion over finances... (Psalm 115:14)"
    },
    "Sunday": {
        "title": "Protection & Restoration",
        "message": "My household is covered... (Joel 2:25)"
    }
}

today = datetime.today().strftime("%A")
prayer = prayer_schedule.get(today)

title = prayer["title"]  # Keep this short and plain
message_body = prayer["message"].replace("*", "").replace("\n", " ").strip()

if prayer:
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    to=to_whatsapp,
    content_sid=content_sid,
    content_variables=f'{{"1":"{title}", "2":"{message_body}"}}'
    )
    print(f"✅ Sent: {message.sid}")
else:
    print("⛔ No prayer found for today.")