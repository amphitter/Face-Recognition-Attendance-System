import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-recognition-attenda-cbeba-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "238025":
        {
            "name": "",
            "major": "",
            "starting_year": ,
            "total_attendance": ,
            "standing": "",
            "year": 1,
            "last_attendance_time": ""
        }
}

for key, value in data.items():
    ref.child(key).set(value)
