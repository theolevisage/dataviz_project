FROM python:3
COPY scripts/ /scripts/
RUN chmod +x ./scripts/init.sh
RUN ./scripts/init.sh
RUN apt update -y
RUN apt install -y python3-pip
RUN pip3 install mysql-connector-python
EXPOSE 65432
CMD ["python", "./scripts/main.py"]
