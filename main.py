from flask import Flask, request, Response
import json
app = Flask(__name__)

@app.route('/cancel_subscription', methods=['POST'])
def cancel():
    getEmails(request.json)
    return Response(status=200)

@app.route('/transaction_refund', methods=['POST'])
def refund():
    getEmails(request.json)
    return Response(status=200)

@app.route('/unenrolled', methods=['POST'])
def unenrolled():
    getEmails(request.json)
    return Response(status=200)

@app.route('/account_disabled', methods=['POST'])
def disabled():
    getEmails(request.json)
    return Response(status=200)

def getEmails(jsonData):
    emails = []
    for item in jsonData:
        obj = item["object"]
        user = obj["user"]
        emails.append(user["email"])
    return emails

if __name__ == "__main__":
    app.run(host="0.0.0.0")