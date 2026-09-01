from flask import Flask, render_template, request
from gtts import gTTS
import uuid

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():

    text = request.form.get("text", "").strip()

    if not text:
        return render_template(
            "index.html",
            error="Please enter some Tamil text."
        )

    try:
        # Create Tamil speech
        tts = gTTS(text=text, lang="ta")

        # Create a unique filename
        audio_file = "tamil_audio_" + str(uuid.uuid4()) + ".mp3"

        # Save audio
        tts.save("static/" + audio_file)

        return render_template(
            "index.html",
            audio_file=audio_file
        )

    except Exception:
        return render_template(
            "index.html",
            error="Unable to generate audio. Please check your internet connection and try again."
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)