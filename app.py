from flask import Flask, render_template, request
import os

app = Flask(__name__, template_folder="template")

BASE_PATH = os.getcwd()
UPLOAD_PATH = os.path.join(BASE_PATH, 'static/upload/')

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        upload_file = request.files['image_name']  # Fix typo here
        filename = upload_file.filename
        path_save = os.path.join(UPLOAD_PATH, filename)
        upload_file.save(path_save)
        
        return render_template('index.html')
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
