# Advanced Sales Intelligence for 10+ Years Experience Sales Person
# This module handles conversations like a seasoned institute sales person

from http.client import responses

from http.client import responses

from knowledge_base import COURSE_INFO, FAQS

class SalesIntelligence:
    """
    10+ years experienced institute sales person intelligence
    """
    
    def __init__(self):
        self.experience_level = "10+ years"
        self.style = "friendly_mentor"
    
    def get_introduction(self):
        """
        Warm introduction like experienced sales person
        """
        return (
            "హలో బ్రో! నేను అజయ్. Ten Thousand Coders నుండి calling. "
            "నాకు soft skills and technical training లో 10 years experience ఉంది బ్రో. "
            "ఇక్కడ మేము engineering students ని software engineers గా మార్చేస్తాము. "
            "ఇంటర్ నుండి ఉద్యోగం వరకు - మేము ఉన్నాము బ్రో. "
            "Technical course లో interest ఉంటే, నేను useful information ఇస్తాను బ్రో. "
            "Software engineer కాదా లేదా technical skills learn చేయాలనుకుంటున్నావా బ్రో?"
        )
    
    def get_interest_question(self):
        """
        Simple interest check in Telugu slang
        """
        return "Engineering student ఆవా లేదా technical skills learn చేయాలనుకుంటున్నావా బ్రో? Yes లేదా no చెప్పు బ్రో."
    
    def get_encouragement_response(self):
        """
        Response when student shows interest in Telugu slang
        """
        return (
            "That's great! I'm happy to hear you're interested. "
        "Our courses are designed with real projects, practical training, "
        "and job-ready skills. What would you like to know about the course?"
        )
    
    def get_rejection_response(self):
        """
        Respectful exit when student says no in Telugu slang
        """
        return (
            "సరే బ్రో, ఏ problem లేదు. తర్వాత నీకు interest వచ్చే తర్వాత call చేస్తూ ఉంటాను బ్రో. "
            "All the best నీ studies కి బ్రో. నీ bright future కి ఎలాంటి సమస్య ఉండదు. Thank you బ్రో!"
        )
    
    def get_mid_flow_answer_intro(self, question_type):
        """
        Introduction before answering mid-flow questions in professional English
        """

        responses = {
        "fees_and_discounts": "That's a great question. Let me explain the investment details clearly and transparently. ",
        
        "placement_guarantee": "That's an important question. Based on my experience, let me give you a clear and honest explanation. ",
        
        "course_timing": "We offer flexible schedules designed to suit your convenience. Let me explain how it works. ",
        
        "projects_real": "That's a very practical question. Let me walk you through the real projects our students work on. ",
        
        "prerequisite_skills": "I understand your concern. Let me clarify everything step by step for you. ",
        
        "what_is_full_stack": "Great question. Let me explain it with a simple example so it's easy to understand. ",
        
        "salary_expectations": "Let me give you an honest and realistic overview of expected salary ranges. ",
        
        "placement": "Let me share real success stories and placement outcomes from our students. "
        }
        return responses.get(question_type, "Let me clarify this for you in a simple and clear way. ")
    
    
    def get_after_answer_continuation(self):
        """
        Smart follow-up after answering questions
        """
        continuations = [
            "I hope that gives you a clear understanding. Is there anything else you'd like me to explain in more detail?",

            "Does that answer your question, or would you like me to walk you through it step by step?",

           "I want to make sure you have all the information you need to make the right decision. What else would you like to know?",

           "That's one of the most common questions students ask. Would you like to know how it applies to your career goals?",

           "I hope that helps. Are there any concerns or questions you'd like me to clarify further?",

           "Feel free to ask anything about the curriculum, fees, projects, internships, or placements. I'm here to help.",

          "Many students have similar questions before joining. Is there any specific area you'd like more information about?",

          "Would you like me to explain the practical benefits and career opportunities associated with this course?",

         "I want you to have complete clarity before making a decision. What would you like to discuss next?"
           
        ]
        return continuations[0]  # Can rotate these
    
    def get_demo_push_message(self, turn_number):
        """
        Smart demo push after multiple conversations
        """
        if turn_number >= 4:
            return (
                "తర్వాత నేను నీకు suggest చేస్తాను బ్రో - free demo class కి వెళ్లు బ్రో. "
                "అక్కడ నీరు live coding చూస్తాయ బ్రో, actual mentors తో కలిసేటాయ బ్రో, మరియు నీ doubts clear చేస్తాయ బ్రో. "
                "1 hour, completely free, no pressure బ్రో. మీకు ఆసక్తి ఉందా బ్రో?"
            )
        return None
    
    def get_closing_message(self):
        """
        Professional closing if call ends in Telugu slang
        """
        return (
            "ఇది చాలా nice conversation బ్రో. నీతో మాట్లాడటం చాలా బాగా ఉంది బ్రో. "
            "ఇక్కడ చెప్పిన విషయాలు consider చేసుకో బ్రో. "
            "తర్వాత నీకు questions ఉంటే, నా contact number వాడు బ్రో. "
            "నీ brilliant future కి all the best బ్రో! Thank you బ్రో!"
        )
    
    def get_objection_handler(self, objection_type):
        """
        Handle common objections like experienced sales person
        """
        handlers = {
            "expensive": (
                "నీకు fee చాలా ఎక్కువ అనిపిస్తుందా బ్రో? నేను చెప్తాను బ్రో - "
                "ఇది investment బ్రో, expense కాదు బ్రో. నీరు 6 months లో ఈ fee కు doubly earn చేస్తాయ బ్రో. "
                "ఇలాంటి training లేకుండా, నీరు 2-3 years waste చేస్తాయ బ్రో. Investment చెసుకో బ్రో!"
            ),
            "time": (
                "Time manage చేయాలనుకుంటున్నావా బ్రో? పీర్ బోధ బ్రో! "
                "మన course పూర్తిగా మీ schedule నుండి flexible బ్రో. "
                "పూర్తి-time job చేస్తూ కూడా, evening batches లో చేయవచ్చు బ్రో."
            ),
            "doubt": (
                "Doubt ఉందా బ్రో? అందుకే నేను ఉన్నాను బ్రో! "
                "చెల్లు బ్రో, నీరు try చేసుకో బ్రో. 30-day money back guarantee ఉంది బ్రో. "
                "ఉండకపోతే, complete refund బ్రో. Risk లేదు బ్రో!"
            ),
            "job_guarantee": (
                "నీరు placement guarantee అన్నారా బ్రో? నేను guarantee ఇవ్వను బ్రో - "
                "కానీ నీరు काम చేస్తే, 90% సంభావ్యత ఉంది బ్రో। "
                "మన 85% students ని personally నేను place చేసాను బ్రో. "
                "నీరు serious ఉండాలి బ్రో."
            )
        }
        return handlers.get(objection_type, "ఈ doubt గురించి మీరు చింతపడకండి. నీరు sure చేసుకోవచ్చు.")

# Create global instance
sales_person = SalesIntelligence()

def get_intro_message():
    return sales_person.get_introduction()

def get_interest_check():
    return sales_person.get_interest_question()

def get_yes_response():
    return sales_person.get_encouragement_response()

def get_no_response():
    return sales_person.get_rejection_response()

def get_answer_intro(q_type):
    return sales_person.get_mid_flow_answer_intro(q_type)

def get_after_answer():
    return sales_person.get_after_answer_continuation()

def get_demo_message(turn):
    return sales_person.get_demo_push_message(turn)

def get_close():
    return sales_person.get_closing_message()

def handle_objection(obj_type):
    return sales_person.get_objection_handler(obj_type)
