import os
from flask import request
from flask_api import status
from app import app

@app.route('/files', methods=['GET', 'POST'])
def files_route():

    if request.method == 'POST':
        file = request.files['file']

        # --------------------------------------------------------
        # TODO: Add secure_filename or edit filename
        # filename = secure_filename(file.filename)
        # --------------------------------------------------------

        # Создание файла и последующая его перезапись
        f = open(os.path.join(app.config['UPLOAD_FOLDER'], file.filename), 'w')
        f.close()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))

        data = {
            'text': 'Ваш файл отправлен в очередь на печать'
        }

        return data, status.HTTP_201_CREATED

    else:
        dir_list = os.listdir(app.config['UPLOAD_FOLDER'])
        
        data = {
            'list': dir_list
        }

        return data, status.HTTP_200_OK

