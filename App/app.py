import streamlit as st
import json
from flask import Flask, request, jsonify
from threading import Thread

# Initialize Flask app
flask_app = Flask(__name__)

@flask_app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()  # Get the JSON data from the request
    return jsonify(data)  # Return the same data as a JSON response

def run_flask():
    flask_app.run(debug=True, port=5000, use_reloader=False)

# Start Flask app in a separate thread
flask_thread = Thread(target=run_flask)
flask_thread.start()

st.title("Echo Service with Flask Backend")

# Form to collect data from user
data = st.text_area("Enter data (in JSON format):")

if st.button("Send"):
    try:
        # Convert input data to JSON
        json_data = json.loads(data)
        
        # Send POST request to Flask server
        response = requests.post('http://127.0.0.1:5000/echo', json=json_data)
        
        if response.status_code == 200:
            st.success("Data sent successfully!")
            st.write("Response from server:")
            st.json(response.json())
        else:
            st.error(f"Server returned an error: {response.status_code}")
    
    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please enter valid JSON data.")
