from flask_cors import CORS
#from authorization.token_service import TokenServiceImpl
#from authorization.security import EndpointsSecurityService
from mongo_orm import mongo_db
from flask import Flask, request

import settings
app = Flask(__name__)
# token_service = TokenServiceImpl()
# security_service = EndpointsSecurityService()

CORS(app)
from db_methods_user_data_service import service as service_s

#launch print
print("App runs")

user_data_service = service_s.UserDataService(
        mongo_db.MongoRepository(
            settings.DB_CONNECTION_STRING, "QR_code_app_DB", "user_data_collection"))



test_user = {
        "id": "0",
        "name": "TestName",
        "surname": "TestSurname",
        "login": "TestLogin",
        "password": "password",
        "visit_frequency": 75,
        "valid_due": "10/11/25 12:00:00"
    }


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'login' not in data or 'password' not in data:
        return {"message": "Invalid input"}, 400

    login = data['login']
    password = data['password']


    if login == test_user['login'] and password == test_user['password']:
        test_user_info = {key: test_user[key] for key in ['id', 'name', 'surname', 'valid_due'] if key in test_user}
        return test_user_info, 200
    elif login != test_user['login']:
        return {"message": "User not found"}, 404
    else:
        return {"message": "Invalid password"}, 401

@app.route('/api/find-user', methods=['POST'])
def find_user():
    data = request.json
    user_id = data['id']
    if user_id == test_user['id']:
        if test_user:
            print("Sending test_user")
            return test_user, 200
        else:
            return {"error": "User not found"}, 404
    else: return {"error": "User not found"}, 404

if __name__ == '__main__':
    app.run()
