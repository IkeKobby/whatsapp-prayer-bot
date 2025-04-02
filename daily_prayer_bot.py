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
        "title": "🗓 Monday: Overturning the Enemy’s Agenda",
        "message": "🕊️ “By the blood of Jesus, I overturn every plan, reaction, and advantage the enemy is using against my life, marriage, family, academics, and finances. I nullify it by covenant authority!”\n"
                   "📖 Isaiah 54:17"
    },
    "Tuesday": {
        "title": "🗓 Tuesday: Releasing Supernatural Increase",
        "message":  "🌾 “I release the increase of my household, my academic journey, my marriage, and the land I dwell in. I declare divine fruitfulness and favor over all that concerns me.”\n"
                   "📖 Deuteronomy 1:11"
    },
    "Wednesday": {
        "title": "🗓 Wednesday: Wisdom & Academic Excellence",
        "message": "🎓 “I receive wisdom, insight, and understanding. My mind is anointed for comprehension, retention, and divine acceleration in all academic matters.”\n"
                   "📖 Daniel 1:17"
    },
    "Thursday": {
        "title": "🗓 Thursday: Marital Blessings & Fruitfulness",
        "message":  "💍 “I declare unity, joy, peace, and fruitfulness in my marriage. The Lord is at the center; we are walking in divine harmony and fulfillment of purpose.”\n"
                   "📖 Ecclesiastes 4:12"
    },
    "Friday": {
        "title": "🗓 Friday: Career Breakthroughs & Purposeful Work",
        "message": "📈 “Father, grant me favor, innovation, and open doors in my career. I walk in excellence and impact. My work glorifies You and elevates lives.”\n"
                   "📖 Psalm 90:17"
    },
    "Saturday": {
        "title": "🗓 Saturday: Financial Overflow & Landed Increase",
        "message": "💰 “I declare dominion over my finances. I receive overflow, divine provision, and stewardship. The land yields its increase because I am rooted in God.”\n"
                   "📖 Psalm 115:14"
    },
    "Sunday": {
        "title": "🗓 Sunday: Protection, Restoration, and Alignment",
        "message": "🛡️ “My household is covered. The Lord restores everything lost—time, joy, peace, relationships. I walk in full alignment with His will.”\n"
                   "📖 Joel 2:25"
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
    print("Sending message using content SID:", content_sid)


    # print("📍 Loaded updated script. Media URL is: https://raw.githubusercontent.com/IkeKobby/whatsapp-prayer-bot/master/img.png")

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to=to_whatsapp,
        content_sid=content_sid,
        content_variables=json.dumps({
            "1": title,
            "2": message_body
        }),
        # media_url=["https://raw.githubusercontent.com/IkeKobby/whatsapp-prayer-bot/master/img.png"]
    )


    print(f"✅ Prayer sent: {message.sid}")
else:
    print("⛔ No prayer found for today.")