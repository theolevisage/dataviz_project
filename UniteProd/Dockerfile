FROM python:3
WORKDIR /scripts
COPY ./scripts .
RUN chmod +x init.sh
RUN ./init.sh
CMD ["python", "./main.py"]
EXPOSE 65432