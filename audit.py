from flask import Flask
from random import shuffle
from flask import request
from datetime import datetime

app = Flask(__name__)

audit_list = []

dt = datetime.now()
ts = datetime.timestamp(dt)
date_time = datetime.fromtimestamp(ts)
str_date_time = date_time.strftime("%d-%m-%Y, %H:%M:%S")


def audit_log(api, payload):
  if (len(audit_list) >= 10):
    audit_list.pop(0)
  audit_list.append({'api': api, 'payload': payload, 'timestamp': str_date_time})


#Jumble word


@app.route("/jumble", methods=['GET'])
def jumble():
  args = request.args
  word = args.get('word')
  if word is not None and word.isalnum():
    audit_log('jumble', {'word': word})
  else:
    return { 'err': "Please send a valid request" }, 400

  if (len(word) <= 0):
    return { 'result': "" }, 200

  split_word = [c for c in word]
  shuffle(split_word)
  result = ''.join([c for c in split_word])
  return { 'result': result }, 200


@app.route("/audit", methods=['GET'])
def getAudit():
  return { 'result':  tuple(audit_list)}, 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
