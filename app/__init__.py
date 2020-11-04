from flask import Flask
from flask_cors import CORS

# DEVELOPMENT
UPLOAD_FOLDER = r"c:\Users\dimaz\Desktop\Printer Project\printer_uploaded_files"
# # PRODUCTION
# UPLOAD_FOLDER = "/var/www/downloaded_files_printer"

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views
