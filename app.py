# importing libraries
import pickle
from sklearn.pipeline import Pipeline
from flask_restful import Api, Resource
from flask import Flask, jsonify, request





with open('ChatBot.pkl', 'rb') as f:
    clf = pickle.load(f)
    

app = Flask(__name__)
api = Api(app)


def checkPostedData(postedData, functionName):
    if (functionName == "add"):
        if "x" not in postedData:
            return 301 #Missing parameter
        else:
            return 200

class Add(Resource):
    def post(self):
        
        postedData = request.get_json()
        #Steb 1b: Verify validity of posted data
        status_code = 200
        #status_code = checkPostedData(postedData, "add")
        if (status_code!=200):
            retJson = {
                "Message": "An error happened",
                "Status Code":status_code
            }
            return jsonify(retJson)

        #If i am here, then status_code == 200
        x = postedData["x"]
        # giving ans with classifier
        Ans = clf.predict([x])[0]
        
        retMap = {
            'Message':Ans ,
            'Status Code': 200
        }
        return jsonify(retMap)


api.add_resource(Add, "/add")

@app.route('/')
def hello_world():
    return "Hello World!"


if __name__=="__main__":
    app.run(debug=True)


