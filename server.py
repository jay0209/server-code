from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    gps_data = request.headers.get('gps_data')
    # Process GPS data here

    # Retrieve and process the received image data (multipart/form-data)
    image_data = request.files['image']
    # Process image data here

    # Add logic to determine when to send a "make_call" response
    if should_make_call():
        return "make_call"
    else:
        return "no_call"

def should_make_call():
    # Add your logic here to determine when a call should be made
    return True  # Modify this as needed

if __name__ == '__main__':
    app.run(host='106.194.207.115', port=80)
