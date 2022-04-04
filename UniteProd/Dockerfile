FROM python:3
COPY main.py /
COPY ./init.sh /
COPY ./keygen-batch /
RUN chmod +x ./init.sh
RUN  ./init.sh
CMD ["python", "./main.py"]
EXPOSE 65432