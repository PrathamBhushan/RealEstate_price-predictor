from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    # Return the list of locations
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all origins
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # Get data from the request
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Get the estimated price
    estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)

    # Return the response with estimated price
    response = jsonify({
        'estimated_price': estimated_price
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all origins
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Load the saved model and artifacts
    app.run(debug=True)  # Run the Flask app
