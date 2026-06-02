from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import os

app = Flask(__name__)

# =============================
# SAFE MEMORY
# =============================
call_state = {}
student_phone = {}

# =============================
# SAFE FUNCTIONS
# =============================
def get_state(call_id):
    return call_state.get(call_id, {"stage": "intro"})

def update_state(call_id, state):
    call_state[call_id] = state

def get_turn(call_id):
    return 0

def increment_turn(call_id):
    pass

def add_to_history(*args, **kwargs):
    pass

def is_affirmative(text):
    return "yes" in text.lower()

def is_negative(text):
    return "no" in text.lower()

def extract_course(text):
    return "python"

def extract_day(text):
    return "monday"

def extract_time(text):
    return "10am"

def detect_question_type(text):
    return ("general", True)

def generate_answer(question_type, text):
    return "Ok"

def create_booking(**kwargs):
    return {"status": "ok"}

def try_general_question_response(*args, **kwargs):
    return False

# =============================
# HOME ROUTE
# =============================
@app.route("/", methods=["GET"])
def home():
    return "AI Voice Bot Running"

# =============================
# VOICE ROUTE
# =============================
@app.route("/voice", methods=["GET", "POST"])
def voice():
    response = VoiceResponse()
    gather = Gather(input="speech", action="/process", method="POST")

    gather.say("Hello, are you interested in course? Say yes or no")
    response.append(gather)

    return str(response)

# =============================
# PROCESS ROUTE
# =============================
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

# =============================
# RUN (IMPORTANT FOR RAILWAY)
# =============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)