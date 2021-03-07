import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Visionari:
    def __init__(self):
        self.file_name = "VISIONARI-a390567d08d5.json"
        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            'VISIONARI-a390567d08d5.json', scope)
        client = gspread.authorize(creds)
        self.sheet = client.open(
            "Contatti Visionari Self Publishing").worksheet('Test Bot')

    def getPhone(self):
        return self.sheet.col_values(5)

    def remove(self, index):
        self.sheet.delete_row(index)

    def getEmail(self):
        return self.sheet.col_values(6)
