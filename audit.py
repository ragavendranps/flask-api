from flask import Flask
from random import shuffle
from flask import request

app = Flask(__name__)

audit_list = []

#audit

def audit_log(api, payload):
  if (len(audit_list) >= 10):
    audit_list.pop(0)
  audit_list.append({'api': api, 'payload': payload})

#Jumble word

@app.route("/jumble", methods=['GET'])
def jumble():
  args = request.args
  word = args.get('word')
  if word is not None and word.isalnum():
    audit_log('jumble', {'word': word})
  else:
    return "Please send a valid request"

  if (len(word) <= 0):
    return ""

  split_word = [c for c in word]
  shuffle(split_word)
  return ''.join([c for c in split_word])

@app.route("/audit", methods=['GET'])
def getAudit():
  return audit_list
