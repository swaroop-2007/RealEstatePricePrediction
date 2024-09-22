from flask import Flask, jsonify, request 
import util
app = Flask(__name__)



@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    print(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    totalsqft = float(request.form['totalsqft'])
    location = request.form['location']
    bedrooms = int(request.form['bedrooms'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.getPrice(location,totalsqft, bedrooms,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response 


if __name__ == '__main__':
    print('Started the server')
    app.run()