import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#Fetch the service account key JSON file contents
cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smartyblinds-default-rtdb.firebaseio.com/'
})

ref = db.reference('Values/')
data = ref.get()
print(data)
