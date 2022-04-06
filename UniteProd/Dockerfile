FROM python:3
COPY ./scripts/ /scripts/
RUN chmod +x ./scripts/init.sh
RUN ./scripts/init.sh
CMD ["python", "/scripts/main.py"]
EXPOSE 65432