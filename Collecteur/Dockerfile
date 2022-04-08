FROM python:3
WORKDIR /scripts
COPY ./scripts .
RUN chmod +x init.sh
RUN ./init.sh
RUN apt update -y
RUN apt install -y python3-pip
RUN pip3 install mysql-connector-python
RUN pip3 install python-gnupg
EXPOSE 65432
CMD ["python", "./main.py"]
