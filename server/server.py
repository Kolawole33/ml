from flask import Flask, request
from flask import jsonify
import util
from flask_cors import CORS, cross_origin


app= Flask(__name__)
CORS(app)
cors= CORS(app, resources={
    r"/*":{
        "origin":"localhost"
    }
})

@app.route("/get_location_names", methods=["GET"])
def get_location_names():
    response= jsonify({
        "locations": util.get_location_names()
    })
    response.headers.add("Acess-Control-Allow-Origin","*")
    return response

@app.route("/predict_home_price", methods=["POST"])
def predict_home_price():

    total_sqft = float(request.form["total_sqft"])
    location = request.form["location"]
    bhk= int(request.form["bhk"])
    bath = int(request.form["bath"])

    response = jsonify({

        "estimated_price": util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    response.headers.add("Acess-Control-Allow-Origin", "*")
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server Home Price")
    util.get_location_names()
    util.load_saved_aritifacts()
    #util.predict_home_price()
    app.run(debug=True, host="0.0.0.0", port=9696)
