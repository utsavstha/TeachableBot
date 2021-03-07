from flask import Flask, request, Response
import json
import Visionari
import Bot
app = Flask(__name__)


@app.route('/cancel_subscription', methods=['POST'])
def cancel():
    kickUserForEmails(getEmails(request.json))
    return Response(status=200)


@app.route("/")
def index():
    return "Hello World!"


@app.route('/transaction_refund', methods=['POST'])
def refund():
    kickUserForEmails(getEmails(request.json))
    return Response(status=200)


@app.route('/unenrolled', methods=['POST'])
def unenrolled():
    kickUserForEmails(getEmails(request.json))
    return Response(status=200)


@app.route('/account_disabled', methods=['POST'])
def disabled():
    kickUserForEmails(getEmails(request.json))
    return Response(status=200)


def getEmails(jsonData):
    emails = []
    for item in jsonData:
        obj = item["object"]
        user = obj["user"]
        emails.append(user["email"])
    return emails


def kickUserForEmails(teachableEmails):
    visionari = Visionari.Visionari()
    phones = visionari.getPhone()
    emails = visionari.getEmail()
    kickPhones = []
    for i in range(len(teachableEmails)):
        for j in range(len(emails)):
            if teachableEmails[i] == emails[j]:
                print(f"kick {phones[j]}")
                print(j)
                visionari.remove(j+2)
                # kickPhones.append(phones[j])
                bot.kickUser(phones[j])


# def findUsernameForPhones(phones):
#     bot = Bot.Bot()
#     telegram_channel_users = bot.getUsers()
#     for phone in phones:
#         for users in telegram_channel_users:
#             if phone == users.phone
#             return


if __name__ == "__main__":
    app.run(host="0.0.0.0")
