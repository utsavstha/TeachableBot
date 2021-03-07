from telethon import TelegramClient, events, sync, Button
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

from telethon.tl.types import ChannelParticipantsSearch


class Bot:
    def __init__(self):
        self.api_id = 2513883
        self.api_hash = 'af250cc4b78b7a96994e21e1a9b742ed'
        self.client = TelegramClient(
            StringSession("1BVtsOHUBu8HRbpZESrzsRgQ-4PvP09zNN3eGWg-G8rubX4n-ZdR4KJfraaBo51xPoU-EWhb3PUsLhRaVNKAwTPBY2whlBU7Apb2pjqvhLo-gh2adD-_1ULMkLcz7uennqrOTUCRXgpt93Dgm8gHJeLGQsAygwWdJU7XfrM2FO94gnKA7dMcWqyW_3w04Ign5v94hDP65lLduQoeqDXXgsfxzs-PJuGLnML5sE6MV1HB5SWdiR9fmBH_2olpFx4olojpyArkRjnQ1RYalgDbHDgdADOJGHnIfnioz56-38lMf6EYxIo6CYBDF6atdRAEu2aLmeCzCsNwJ59S6rROku2YscJDe7lk="), self.api_id, self.api_hash)
        self.client.connect()
        self.channel_username = self.client.get_entity(
            'https://t.me/joinchat/VhKhawm8z_2Vi2SO')
        # contact = self.client.get_entity('393401578854')
        # self.kickUser(contact)
        # print(contact)
        # print(self.client.session.save())

    def getusername(self, phone):
        self.client.get_entity(phone)

    def getUsers(self):
        users = []
        offset = 0
        limit = 200
        my_filter = ChannelParticipantsSearch('')
        self.all_participants = []
        while_condition = True
        channel = self.client(GetFullChannelRequest(self.channel_username))
        while while_condition:
            participants = self.client(GetParticipantsRequest(
                channel=self.channel_username, filter=my_filter, offset=offset, limit=limit, hash=0))
            self.all_participants.extend(participants.users)
            offset += len(participants.users)
            if len(participants.users) < limit:
                while_condition = False
            for _user in participants.users:
                users.append(f"{_user.phone} {_user.username}")
        print(users)
        # self.client.disconnect()

        return self.all_participants

    def kickUser(self, user):
        # channel = self.client(GetFullChannelRequest(self.channel_username))
        self.client.edit_permissions(
            self.channel_username, user, view_messages=False)
