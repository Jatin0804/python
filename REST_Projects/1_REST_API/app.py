from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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

@app.route('/')
def calulator():
    return "REST API based calculator"

if __name__ == "__main__":
    app.run(debug = True)