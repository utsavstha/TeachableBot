import Visionari
import Bot

# Get list of phone numbers in google sheet
visionari = Visionari.Visionari()
sheet_phones = visionari.getPhone()
# print(sheet_phones)
# Get list of users in channel
bot = Bot.Bot()
users = bot.getUsers()


def phoneExists(phone, sheet):
    for s in sheet:
        if phone.find(s):
            return True
    return False


# Check if user exists in sheets
for user in users:
    if phoneExists(str(user.phone), sheet_phones):
        print(f"{user.phone} exists")
    else:
        print(f"{user.phone} not exists")
