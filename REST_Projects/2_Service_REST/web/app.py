"""
Registration of user
Each user gets 10 tokens
Store a sentense on our database for 1 token
Retrieve his stored sentence on our database for 1 token
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt as bc

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client["SentencesDB"]
users = db["Users"]

def verify_pass(username, password):
    hashed_pw = users.find_one({
        "Username": username
    })["Password"]

    return bc.checkpw(password.encode('utf8'), hashed_pw)

def countTokens(username):
    tokens = users.find_one({
        "Username": username
    })["Tokens"]

    return tokens

class Register(Resource):
    def post(self):
        data = request.get_json()

        username = data["username"]
        password = data["password"]

        hashed_pass = bc.hashpw(password.encode('utf8'), bc.gensalt())
        users.insert_one({
            "Username": username,
            "Password": hashed_pass,
            "Sentence": "",
            "Tokens": 10
        })

        retJson = {
            "status": 200,
            "msg": "You successfully signed up for the API"
        }

        return retJson
    
class Store(Resource):
    def post(self):
        data = request.get_json()
        
        username = data["username"]
        password = data["password"]
        sentence = data["sentence"]

        correct_pw = verify_pass(username, password)
        if not correct_pw:
            return jsonify({
                "status": 302, 
                "msg": "Invalid password"
            })
        
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            return jsonify({
                "status": 301,
                "msg": "Not enough tokens"
            })
        
        users.update_one({
            "Username": username
        }, {
            "$set": {
                "Sentence": sentence,
                "Tokens": num_tokens - 1
            }
        })

        return jsonify({
            "status": 200,
            "msg": "Sentence saved successfully"
        })

class GetData(Resource):
    def get(self):
        data = request.get_json()

        username = data["username"]
        password = data["password"]

        correct_pw = verify_pass(username, password)
        if not correct_pw:
            return jsonify({
                "status": 302, 
                "msg": "Invalid password"
            })
        
        num_tokens = countTokens(username)
        if num_tokens <= 0:
            return jsonify({
                "status": 301,
                "msg": "Not enough tokens"
            })
        else:
            users.update_one({
                "Username": username
            }, {
                "$set" : {
                    "Tokens": num_tokens - 1
                }
            })
        
        sentence = users.find_one({
            "Username": username
        })["Sentence"]

        return jsonify({
            "status": 200,
            "sentence": sentence
        })


api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(GetData, '/get')

if __name__ == "__main__":
    app.run(host='0.0.0.0')