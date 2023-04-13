import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


WINDOWS = "C:/Users/user/Desktop/Python hah/ChatBOT/media/serviceAccountKey.json"
LINUX = "/home/dimas/Projects/ChatBOT/media/serviceAccountKey.json"

cred = credentials.Certificate(LINUX)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hakahaka2023-2a606-default-rtdb.firebaseio.com'
})

cards = db.reference('cards')
proff = db.reference('proff')


class Staff:
    def __init__(self, prof):
        self.prof = prof


class Post(Staff):
    def __init__(self, name, link, phone, prof):
        super().__init__(prof)
        self.name = name
        self.link = link
        self.phone = phone






