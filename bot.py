from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")


@app.route("/upload", methods=["POST"])
def upload():
    photo = request.files.get("photo")

    if not photo:
        return jsonify({"error": "No photo received"}), 400

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    files = {
        "photo": ("photo.jpg", photo.stream, "image/jpeg")
    }

    data = {
        "chat_id": CHAT_ID,
        "caption": "تم استلام الصورة بعد موافقة المستخدم على الكاميرا."
    }

    response = requests.post(
        telegram_url,
        data=data,
        files=files,
        timeout=30
    )

    if response.ok:
        return jsonify({"success": True})

    return jsonify({"success": False}), 500


@app.route("/")
def home():
    return "Server is running."


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
  )
