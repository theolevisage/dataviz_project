FROM python:3
ADD main.py /
RUN apt update -y
RUN apt install -y python3-pip
RUN pip3 install mysql-connector-python
EXPOSE 65432
CMD ["python", "./main.py"]
