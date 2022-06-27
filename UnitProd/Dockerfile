FROM python:3
ARG NAME=setme
ARG MAIL=setmetoo
WORKDIR /scripts
COPY ./scripts .
RUN apt update -y
RUN apt install gettext-base
RUN apt install -y python3-pip

RUN chmod +x init.sh
RUN ./init.sh ${NAME} ${MAIL}

RUN pip3 install python-gnupg
RUN mkdir /jsonsavefiles
RUN mkdir /lastsequencenumber
EXPOSE 65432
CMD ["python", "./main.py"]