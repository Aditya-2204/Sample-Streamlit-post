from flask import Flask, request, jsonify
import streamlit

app = Flask(__name__)

@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()  # Get the JSON data from the request
    return jsonify(data)  # Return the same data as a JSON response

if __name__ == '__main__':
    app.run(debug=True)
