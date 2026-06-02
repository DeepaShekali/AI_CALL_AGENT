from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)

call_state = {}

@app.route("/", methods=["GET"])
def home():
    return "AI Voice Bot Running"

@app.route("/voice", methods=["POST", "GET"])
def voice():
    response = VoiceResponse()
    gather = Gather(input="speech", action="/process", method="POST")

    gather.say("Hello, are you interested in course? Say yes or no")
    response.append(gather)

    return str(response)

@app.route("/process", methods=["POST"])
def process():
    user_input = request.form.get("SpeechResult", "")

    response = VoiceResponse()

    if "yes" in user_input.lower():
        response.say("Great! We will contact you.")
    else:
        response.say("Okay thank you!")

    response.hangup()
    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)