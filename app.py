from flask import Flask, request, jsonify
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    try:
        # Get data from the form
        interval = request.form['interval']
        enable_screenshot = request.form['enable_screenshot']
        screenshot_type = request.form['screenshot_type']

        # Handle file uploads
        files = request.files.getlist('files')
        for file in files:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        # Log the data and send a response
        response = {
            'status': 'Files uploaded successfully',
            'interval': interval,
            'enable_screenshot': enable_screenshot,
            'screenshot_type': screenshot_type
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({'status': 'Error', 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
