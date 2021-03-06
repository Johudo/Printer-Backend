FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/Printer-Backend/app/static
COPY ./requirements.txt /var/www/Printer-Backend/requirements.txt
RUN pip install -r /var/www/Printer-Backend/requirements.txt
RUN mkdir /var/www/downloaded_files_printer
