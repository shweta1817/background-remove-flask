import cv2
import os
from rembg import remove
from PIL import Image
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'webp'])

# Create necessary directories
if 'static' not in os.listdir('.'):
    os.mkdir('static')

if 'uploads' not in os.listdir('static/'):
    os.mkdir('static/uploads')

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/remback', methods=['POST'])
def remback():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)

        rembg_img_name = filename.rsplit('.', 1)[0] + "_rembg.png"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], rembg_img_name)
        remove_background(input_path, output_path)

        return render_template('home.html', org_img_name=filename, rembg_img_name=rembg_img_name)
    return "Invalid file type"

# ✅ Important for Render or similar services
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use Render's provided port or default to 5000 locally
    app.run(debug=True, host='0.0.0.0', port=port)
