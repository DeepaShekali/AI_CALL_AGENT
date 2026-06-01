from flask import Flask, request, render_template, jsonify
from twilio.twiml.voice_response import VoiceResponse, Gather
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

# =============================
# STATE STORAGE
# =============================
call_state = {}
conversation_history = {}
turn_count = {}
student_phone = {}

# =============================
# HELPERS
# =============================
def get_state(call_id):
    return call_state.get(call_id, {
        "stage": "intro",
        "student_name": None,
        "student_mobile": None,
        "course_selected": None,
        "demo_date": None,
        "demo_time": None
    })

def update_state(call_id, state):
    call_state[call_id] = state

def add_history(call_id, role, text):
    conversation_history.setdefault(call_id, []).append({
        "role": role,
        "text": text
    })

def get_turn(call_id):
    return turn_count.get(call_id, 0)

def increment_turn(call_id):
    turn_count[call_id] = get_turn(call_id) + 1


# =============================
# HEALTH CHECK
# =============================
@app.route("/", methods=["GET"])
def home():
    return "AI CALL AGENT RUNNING ✅"


# =============================
# VOICE WEBHOOK (TWILIO ENTRY)
# =============================
@app.route("/voice", methods=["POST", "GET"])
def voice():
    response = VoiceResponse()

    try:
        call_id = request.form.get("CallSid", "default")
        phone = request.form.get("From", "unknown")

        if call_id not in call_state:
            call_state[call_id] = get_state(call_id)

        student_phone[call_id] = phone

        gather = Gather(
            input="speech",
            action="/process",
            method="POST",
            timeout=10,
            speechTimeout="auto",
            language="en-IN"
        )

        gather.say(
            "Hello! Welcome to our AI institute. Are you interested in courses?",
            voice="Polly.Aditi"
        )

        response.append(gather)
        return str(response)

    except Exception as e:
        print("VOICE ERROR:", e)
        response.say("System error. Please try later.")
        return str(response)


# =============================
# MAIN PROCESSING ENDPOINT (ONLY ONE)
# =============================
@app.route("/process", methods=["POST"])
def process():
    response = VoiceResponse()

    try:
        call_id = request.form.get("CallSid", "default")
        user_input = request.form.get("SpeechResult", "").strip()

        state = get_state(call_id)

        print("USER:", user_input)

        gather = Gather(
            input="speech",
            action="/process",
            method="POST",
            timeout=10,
            speechTimeout="auto",
            language="en-IN"
        )

        # ❌ no input
        if not user_input:
            response.say("Sorry, I didn't hear you. Please repeat.")
            response.append(gather)
            return str(response)

        # log
        add_history(call_id, "Student", user_input)
        increment_turn(call_id)

        # =============================
        # SIMPLE FLOW FIRST (NO COMPLEX LOGIC)
        # =============================

        if state["stage"] == "intro":
            response.say("Great! Which course are you interested in?")
            state["stage"] = "course"

        elif state["stage"] == "course":
            state["course_selected"] = user_input
            response.say(f"Nice choice! You selected {user_input}. Do you want a demo class?")

            state["stage"] = "demo"

        elif state["stage"] == "demo":
            if "yes" in user_input.lower():
                response.say("Great! Please tell your preferred date and time.")
                state["stage"] = "booking"
            else:
                response.say("Okay no problem. Thank you for calling.")
                response.hangup()
                return str(response)

        elif state["stage"] == "booking":
            response.say("Your demo is noted. Our team will contact you.")
            response.hangup()
            return str(response)

        update_state(call_id, state)

        response.append(gather)
        return str(response)

    except Exception as e:
        print("PROCESS ERROR:", e)
        r = VoiceResponse()
        r.say("System error occurred")
        return str(r)


# =============================
# RUN SERVER
# =============================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)