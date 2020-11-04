from flask import Flask
from flask_cors import CORS

UPLOAD_FOLDER = r"c:\Users\dimaz\Desktop\Printer Project\printer_uploaded_files"

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# if __name__ == '__main__':
#     app.run()