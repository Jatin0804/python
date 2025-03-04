from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client["RESTAPI"] 

UserNum = db["UserNum"]
UserNum.insert_one({
    'num_of_users': 1
})

class Visit(Resource):
    def get(self):
        prev = UserNum.find_one({})[0]['num_of_users']
        new = prev + 1
        UserNum.update_many({}, {
            "$set": {
                'num_of_users': new
            }
        })
        return str("Hello user " + str(new))        

def checkData(postedData, functionName):
    if ('x' not in postedData or 'y' not in postedData):
        # Missing parameters
        return 301
    
    if functionName == "divide":
        if int(postedData['y']) == 0:
            # Dividing by 0
            return 302
        else:
            return 200
        
    return 200
    
def calc(operation):
    # get data from post request
    data = request.get_json()

    # verify the validity of data
    status_code = checkData(data, operation)
    if (status_code != 200):
        retJson = {
            'Message': 'An error happened',
            'Status Code': status_code
        }
        return jsonify(retJson)

    x = data['x']
    y = data['y']
    x = int(x)
    y = int(y)

    ops = {
        "add": x + y,
        "subtract": x - y,
        "multiply": x * y,
        "divide": x / y
    }

    res = ops[operation]
    retMap = {
        'Message': res,
        'Status Code': 200
    }

    # return the data
    return jsonify(retMap)

class Add(Resource):
    def post(self):
        return calc("add")

class Multiply(Resource):
    def post(self):
        return calc("multiply")

class Divide(Resource):
    def post(self):
        return calc("divide")

class Subtract(Resource):
    def post(self):
        return calc("subtract")

api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")
api.add_resource(Visit, "/visits")

@app.route('/')
def calulator():
    return "REST API based calculator"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)