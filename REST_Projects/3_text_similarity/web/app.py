from flask_restful import Resource, Api
from flask import Flask, request, jsonify
from pymongo import MongoClient
import bcrypt as bc
import spacy

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client["TextSimiliarityDB"]
users = db["Users"]

messages = {
    200: "User registered successfully",
    201: "Texts are similar",
    202: "Texts are not similar",
    203: "Refilled successfully",
    301: "Username or password is missing",
    302: "User already exists",
    303: "Password too short",
    304: "Invalid password",
    305: "Not enough tokens",
    306: "Missing additional data",
    307: "Invalid admin password",
}

def msg(status):
    return jsonify({
        "status": status,
        "msg": messages[status]
    })

def verify_data(username, password, *args):
    if not username or not password:
        return 301
    
    for arg in args:
        if not arg:
            return 306

    if not args:
        if users.find_one({"username": username}):
            return 302
        
        if len(password) < 6:
            return 303
    
def verify_pass(username, password):
    return bc.checkpw(password.encode("utf-8"), users.find_one({"username": username})["password"])

def countTokens(username):
    return users.find_one({"username": username})["tokens"]

class Register(Resource):
    def post(self):
        data = request.get_json()

        username = data["username"]
        password = data["password"]

        status = verify_data(username, password)
        if status:
            return msg(status)
        
        hashed_pass = bc.hashpw(password.encode("utf-8"), bc.gensalt())

        users.insert_one({
            "username":username,
            "password":hashed_pass,
            "tokens": 6
        })

        return msg(200)

class Detect(Resource):
    def post(self):
        data = request.get_json()

        username = data['username']
        password = data["password"]
        text1 = data["text1"]
        text2 = data["text2"]

        status = verify_data(username, password, text1, text2)
        if status:
            return msg(status)
        
        correct_pass = verify_pass(username, password)
        if not correct_pass:
            return msg(304)
        
        tokens = countTokens(username)
        if tokens <= 0:
            return msg(305)
        
        users.update_one({
            "username": username
        }, {
            "$set": {
                "tokens": tokens - 1
            }
        })
        
        nlp = spacy.load("en_core_web_sm")
        text1 = nlp(text1)
        text2 = nlp(text2)

        ratio = text1.similarity(text2)
        if ratio < 0.5:
            return msg(202)
        else:
            return jsonify({
                "status": 201,
                "msg": messages[201],
                "similarity": ratio,
                "tokens_left": tokens - 1
            })

class Refill(Resource):
    def post(Self):
        data = request.get_json()

        username = data["username"]
        password = data["ad_password"]
        refill = data["refill"]

        status = verify_data(username, password, refill)
        if status:
            return msg(status)
        
        admin_pass = "admin"
        if password != admin_pass:
            return msg(307)
        
        cur_tokens = countTokens(username)
        users.update_one({
            "username": username
        }, {
            "$set": {
                "tokens": cur_tokens + refill
            }
        })
        
        return jsonify({
            "status": 203,
            "msg": messages[203],
            "tokens_left": cur_tokens + refill
        })

        

api.add_resource(Register, "/register")
api.add_resource(Detect, "/detect")
api.add_resource(Refill, "/refill")

if __name__ == "__main__":
    app.run(host="0.0.0.0")